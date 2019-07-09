
import os
import shutil
import git
from git import Repo

import config
import header

def create_subdirs(args):
    try:
        os.mkdir(args.project_name + "/src")
        os.mkdir(args.project_name + "/inc")
        os.mkdir(args.project_name + "/lib")
        os.mkdir(args.project_name + "/doc")
        os.mkdir(args.project_name + "/test")
    except:
        print("Failed to create subdirectories")

#Makefile
def create_makefile(args):
    f = open(args.project_name + "/Makefile", "w+")

    if (args.header): header.print_makefile(f, "Makefile")
 
    f.write("NAME =\t" + args.project_name + "\n\n")
    f.write("SRC =\tsrc/main.c \\\n\n")
    f.write("INC =\t-I inc \\\n")
    if (args.libft) : f.write("\t\t-I libft/inc \\\n")
    f.write("\n")

    f.write("VPATH =\tsrc\n")
    f.write("OBJ_DIR = obj\n")
    f.write("BIN_DIR = bin\n\n")

    f.write("OBJ = $(addsuffix .o, $(addprefix $(OBJ_DIR)/, $(SRC)))\n")
    f.write("DEP = $(OBJ:%.o = %.d)\n\n")

    f.write("CC = gcc\n")
    f.write("#CC = clang-6.0\n")
    f.write("CFLAGS =\t" + config.CFLAGS_C + " $(INC)\n")
    f.write("LDFLAGS =")
    if (args.libft) : f.write("\t-L libft -lft \\\n")
    f.write("\n")
    f.write("MAKEOPTS = -j4\n\n")

    f.write(".PHONY: all\n")
    f.write("all: $(OBJ_DIR) $(NAME)\n\n")

    f.write("$(OBJ_DIR):\n")
    f.write("\t@printf \"\\033[32mCreating : Object Directory\\033[0m\n")
    f.write("\t@mkdir -p $(OBJ_DIR)\n\n")

    f.write("-include $(DEP)\n\n")

    f.write("$(OBJ_DIR)/%.o: %.c | $(OBJ_DIR)\n")
    f.write("\t@printf \"\\033[32mCompiling:\\033[0m %s\\n\" $<\n")
    f.write("\t@$(CC) $(CFLAGS) -MMD -c $< -o $@\n\n")

    f.write("$(NAME): $(OBJ)\n")
    if (args.libft) : f.write("\t@make -C libft\n")
    f.write("\t@printf \"\\033[33mCompiling:\\033[0m %s\\n\" $(NAME)\n")
    f.write("\t@$(CC) $^ $(LDFLAGS) -o $(BIN_DIR)/$@\n\n")

    f.write(".PHONY: clean\n")
    f.write("clean:\n")
    if (args.libft) : f.write("\t@make -C libft clean\n")
    f.write("\t@printf \"\\033[33mDeleting : Objects\\033[0m\\n\"\n")
    f.write("\t@rm -f $(OBJ) $(DEP)\n\n")

    f.write(".PHONY: fclean\n")
    f.write("fclean: clean\n")
    if (args.libft) : f.write("\t@make -C libft fclean\n")
    f.write("\t@printf \"\\033[33mDeleting : \\033[0m %s\" $(NAME)\n")
    f.write("\t@rm -f $(NAME)\n")
    f.write("\t@printf \"\\033[33mDeleting : Object Directory\\033[0m\"\n")
    f.write("\t@rm -rf $(OBJ_DIR)\n\n")

    f.write(".PHONY: re\n")
    f.write("re: fclean all\n")

    f.close()

#Clone Libraries
def clone_libft(args):
    try:
        Repo.clone_from(config.GIT_LIBFT, args.project_name + "/libft")
    except:
        print("Could not clone libft\n")
    else:
        os.remove(args.project_name + "/libft/README.md")
        os.remove(args.project_name + "/libft/author")
        shutil.rmtree(args.project_name + "/libft/.git")

#Create File Templates
def create_main(args):
    f = open(args.project_name + "/src/main.c", "w+")
    if (args.header): header.print_c(f, "main.c")
    f.write("#include \"" + args.project_name +".h\"\n\n")
    f.write("int    main(int ac, char **av)\n")
    f.write("{\n")
    f.write("\n\treturn (0);\n")
    f.write("}\n")
    f.close()

def create_inc(args):
    f = open(args.project_name + "/inc/" + args.project_name + ".h", "w+")
    if (args.header): header.print_c(f, args.project_name + ".h")
    f.write("#ifndef " + args.project_name.upper() + "_H\n")
    f.write("# define " + args.project_name.upper() + "_H\n")
    f.write("\n")
    if (args.libft): f.write("# include \"libft.h\"\n")
    f.write("\n")
    f.write("#endif\n")

def new(args):
    print("Inside C new")
    #Basic
    create_subdirs(args)
    create_makefile(args)

    #Clone Libraries
    if (args.libft) : clone_libft(args)

    #Create Basic Files
    create_main(args)
    create_inc(args)