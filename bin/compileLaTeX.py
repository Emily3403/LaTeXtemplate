#!/usr/bin/env python3
import argparse
import os
import re


def checkout_correct_hash():
    with open(args.file) as f:
        _commit_hash = re.findall("Generated with commit hash: \"(.*?)\"", f.read())

    if len(_commit_hash) != 1:
        print(f"Could not get the commit hash: {_commit_hash = }")
        exit(1)

    commit_hash = _commit_hash[0]
    os.system(f"cd src; git checkout {commit_hash}")


def restore_last_git_version():
    pass


def get_args():
    parser = argparse.ArgumentParser(prog="compileLaTeX", formatter_class=argparse.RawTextHelpFormatter, description="""
        This program compiles your LaTeX files while ensuring you get as much speed as possible.""")

    parser.add_argument("-n", "--num-threads", help="Specify the maximum number of threads to use", type=int, default=os.cpu_count(), metavar="{num}")
    parser.add_argument("file", help="Specify the file")

    operations = parser.add_mutually_exclusive_group()

    operations.add_argument("-v", "--version", help="Print the version number and exit", action="store_true")

    operations.add_argument("--dump", help="Dumps LaTeX code contained in .sty files into one big one.\n"
                                           "This is useful for archiving and not having to deal with many files.", action="store_true")
    operations.add_argument("--convert-images", help="Only convert images to PDF", action="store_true")
    # operations.add_argument("", help="", action="store_true")
    # operations.add_argument("", help="", action="store_true")

    return parser.parse_args()


def main():
    # checkout_correct_hash()

    restore_last_git_version()
    pass


args = get_args()

if __name__ == '__main__':
    main()
