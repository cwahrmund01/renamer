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
    print("Renaming tar.gz files not implemented yet, skipping...")

def unpack_tarball(tar):
    pass

def rename_file_contents(file_path, old, new):
    with open(file_path, "r") as old_file:
        verboseprint(f"    Opening file for content renaming")
        lines = old_file.readlines()
        file_changed = False
        for i in range(len(lines)):
            if old in lines[i]:
                verboseprint(f"    [Rename] Renaming line {i+1} in file {file_path}...")
                lines[i] = lines[i].replace(old, new)
                file_changed = True

    if file_changed:
        verboseprint("    Overwriting file with renamed lines.")
        with open(file_path, "w") as new_file:
            for line in lines:
                new_file.write(line)
    else:
        verboseprint("    No lines changed, no need to overwrite.")
    verboseprint("    Finished with file")
        
def rename_file(file_path, old, new):
    verboseprint(f"---Renaming file: '{file_path}'---")
    base_dir, file_name = os.path.split(file_path)
    new_file_name = file_name.replace(old, new)
    new_file_path = base_dir + "/" + new_file_name
    verboseprint(f"    [Rename] Renaming file {file_path}: {file_name} --> {new_file_name}")
    os.rename(file_path, new_file_path)
    rename_file_contents(new_file_path, old, new)

def rename_dir_contents(dir_path, old, new):
    pass

def rename_dir(dir_path, old, new):
    verboseprint(f"Renaming directory: '{dir_path}'...")
    contents = os.listdir(dir_path)
    base_dir, dir_name = os.path.split(dir_path)
    print(f"Base name: {dir_name}")
    print(f"Base dir: {base_dir}")

def parse_path(path):
    verboseprint("Parsing directory string")
    if path.endswith("/"):
        verboseprint("Ends with '/' removing to avoid confusing later code...")
        path = path[:-1]

    if os.getcwd() == path:
        verboseprint(f"Directory is current directory, no need to parse: {path}")
        return path, True
    elif path.startswith("/"):
        verboseprint("Absolute path given, testing if it is valid...")
        if os.path.isdir(path):
            verboseprint(f"{path} is a directory")
            return path, True
        elif os.path.isfile(path):
            verboseprint(f"{path} is a file")
            return path, True
        else:
            raise Exception("The directory passed starts with '/' "
                            "but is not a valid absolute path\n"
                            f"Directory passed: {path}")
    else:
        path = os.getcwd() + '/' + path
        verboseprint(f"Assuming relative path given, concatenating with current directory...")
        verboseprint(f"Concatenated directory: {path}")
        if os.path.isdir(path):
            verboseprint(f"{path} is a directory")
            return path, True
        elif os.path.isfile(path):
            verboseprint(f"{path} is a file")
            return path, False
        else:
            raise Exception("Directory input does not start with '/'. "
                            "Assumed path relative to current working "
                            f"directory.\n{path} not a valid directory or file.")

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

    path, is_dir = parse_path(args.directory)
    validate_old_and_new(args.old, args.new)

    verboseprint("Original name:", args.old)
    verboseprint("New name:", args.new)

    if is_dir:
        rename_dir(path, args.old, args.new)
    else:
        rename_file(path, args.old, args.new)



if __name__ == "__main__":
    main()
