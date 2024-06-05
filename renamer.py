import os
import sys
import argparse
import tarfile
from subprocess import call

# Parse args using argparse
parser = argparse.ArgumentParser()
parser.add_argument("old", help="string to be replaced, should be one word", type=str)
parser.add_argument("new", help="new string to replace the target_str with", type=str)
parser.add_argument("directory", nargs="?", help="directory to replace strings in, defaults to CWD", type=str, default=os.getcwd())
parser.add_argument("-v", "--verbose", help="enable more verbose output", action="store_true")
args = parser.parse_args()

verboseprint = print if args.verbose else lambda *a, **k: None

def rename_tarball(tar):
    pass

def unpack_tarball(tar):
    pass

def rename_file(file_path, old, new):
    pass

def rename_dir_contents(dir_path, old, new):
    pass

def rename_dir(dir_path, old, new):
    print(dir_path)
    print(os.listdir(dir_path))

def parse_dir_name(dir_name):
    if os.getcwd() == dir_name:
        return dir_name
    elif dir_name.startswith("/"):
        if os.path.isdir(dir_name) or os.path.isfile(dir_name):
            return dir_name
        else:
            raise Exception("The directory passed starts with '/' "
                            "but is not a valid absolute path\n"
                            f"Directory passed: {dir_name}")

def validate_old_and_new(old, new):
    if len(old.split()) < 1:
        raise Exception("Found empty string for passed for old string. "
                        "If you need quotation marks, use a '\\' "
                        "to escape the chars")
    elif len(old.split()) > 1:
        raise Exception("Old string should be just one word, no spaces.")
    
    if len(new.split()) < 1:
        raise Exception("Found empty string for passed for new string. "
                        "If you need quotation marks, use a '\\' "
                        "to escape the chars")
    elif len(new.split()) > 1:
        raise Exception("New string should be just one word, no spaces.")

def main():
    verboseprint("This is verbose")
    verboseprint("Original name:", args.old)
    verboseprint("New name:", args.new)
    verboseprint("Directory:", args.directory)

    dir_name = parse_dir_name(args.directory)
    old, new = validate_old_and_new(args.old, args.new)

    if os.path.isdir(args.directory):
        print("is dir")
    elif os.path.isfile(args.directory):
        print("is file")
    else:
        print("is neither")

    rename_dir(args.directory, args.old, args.new)



if __name__ == "__main__":
    main()
