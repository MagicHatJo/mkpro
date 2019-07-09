
import os

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

def create_makefile(args):
    #Open
    f = open(args.project_name + "/Makefile", "w+")

    #Header
    if (args.header): header.print_header(f, "Makefile")
    #Basic
    f.write("NAME =\t" + args.project_name + "\n\n")
    f.write("SRC =\tsrc/main.c \\\n\n")
    f.write("INC =\t-I inc \\\n\n")

    f.write("VPATH =\tsrc\n")
    f.write("OBJ_DIR = obj\n")
    f.write("BIN_DIR = bin\n\n")

    f.write("OBJ = $(addsuffix .o, $(addprefix $(OBJ_DIR)/, $(SRC)))\n")
    f.write("DEP = $(OBJ:%.o = %.d)\n\n")

    f.write("CC = gcc\n")
    f.write("#CC = clang-6.0\n")
    f.write("CFLAGS = " + config.CFLAGS_C + " $(INC)\n")
    f.write("LDFLAGS =\n")
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
    f.write("\t@printf \"\\033[33mCompiling:\\033[0m %s\\n\" $(NAME)\n")
    f.write("\t@$(CC) $^ $(LDFLAGS) -o $(BIN_DIR)/$@\n\n")

    f.write(".PHONY: clean\n")
    f.write("clean:\n")
    f.write("\t@printf \"\\033[33mDeleting : Objects\\033[0m\\n\"\n")
    f.write("\t@rm -f $(OBJ) $(DEP)\n\n")

    f.write(".PHONY: fclean\n")
    f.write("fclean: clean\n")
    f.write("\t@printf \"\\033[33mDeleting : \\033[0m %s\" $(NAME)\n")
    f.write("\t@rm -f $(NAME)\n")
    f.write("\t@printf \"\\033[33mDeleting : Object Directory\\033[0m\"\n")
    f.write("\t@rm -rf $(OBJ_DIR)\n\n")

    f.write(".PHONY: re\n")
    f.write("re: fclean all\n")

    f.close()

def new(args):
    print("Inside C new")
    #Basic
    create_subdirs(args)
    create_makefile(args)

    #Clone Libraries