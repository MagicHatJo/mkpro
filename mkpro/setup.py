
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser()
    
    # Basic
    parser.add_argument("project_name", help="[Project Name]")
    parser.add_argument("project_lang", help="[Project Language]")
    parser.add_argument("-g", "--git-url", help="Link to a remote repository")

    # Libraries
    parser.add_argument("--libft", action="store_true", help="Include libft")

    # Headers
    parser.add_argument("--header", action="store_true", help="Include headers")
    return parser.parse_args()

def create_rootdir(args):
    if not os.path.exists(args.project_name):
        os.mkdir(args.project_name)
    else:
        raise Exception(str(args.project_name) + " already exists")