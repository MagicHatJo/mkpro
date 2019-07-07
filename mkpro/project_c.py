
import os


def create_subdirs(args):
    try:
        os.mkdir(args.project_name + "/src")
        os.mkdir(args.project_name + "/inc")
        os.mkdir(args.project_name + "/lib")
        os.mkdir(args.project_name + "/doc")
        os.mkdir(args.project_name + "/test")
    except:
        print("Failed to create subdirectories")

def new(args):
    print("Inside C new")
    create_subdirs(args)