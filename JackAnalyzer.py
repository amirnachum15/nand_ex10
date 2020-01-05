from CompilationEngine import CompilationEngine
import os
import sys


def handle_file(file_path, output_stream):
    CompilationEngine(file_path, output_stream)

def handle_dir(dir_full_path):
    slash = "/" if "/" in dir_full_path else "\\"
    directory_name = dir_full_path.split(slash)[-1]
    output_file_path = dir_full_path + slash + directory_name + ".xml"
    for file_name in os.listdir(dir_full_path):
        if file_name.endswith(".jack"):
            handle_file(dir_full_path + slash + file_name, output_file_path)

def main():
    argv = sys.argv
    args = len(argv)

    if args != 2:
        print("not enough arguments")
        return

    if os.path.isdir(argv[1]):
        dir_full_path = argv[1]
        handle_dir(dir_full_path)
    elif os.path.isfile(argv[1]):
        file_full_path = argv[1]
        output_file_name = file_full_path.split('.')[0] + ".xml"
        handle_file(file_full_path, output_file_name)
    else:
        print("did not enter a valid file/dir")
        return

if __name__ == "__main__":
    main()
