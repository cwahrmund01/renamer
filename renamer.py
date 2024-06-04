import os
import sys
import argparse
import tarfile
from subprocess import call

# Parse args using argparse
parser = argparse.ArgumentParser()
parser.add_argument("target_str", help="string to be replaced, should be one word", type=str)
parser.add_argument("new_str", help="new string to replace the target_str with", type=str)
parser.add_argument("directory", nargs="?", help="directory to replace strings in, defaults to CWD", type=str, default=os.getcwd())
parser.add_argument("-v", "--verbose", help="enable more verbose output", action="store_true")
args = parser.parse_args()

verboseprint = print if args.verbose else lambda *a, **k: None

def print_usage():
    pass

def main():
    verboseprint("This is verbose")
    print("Original name:", args.target_str)
    print("New name:", args.new_str)
    print("Directory:", args.directory)


if __name__ == "__main__":
    main()
