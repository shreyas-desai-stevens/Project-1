#!/usr/bin/env python
import argparse
import sys
from pathlib import Path
import os

def count_wc(file):
    lines = 0
    words = 0
    characters = 0

    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

    return lines, words, characters

def main():
    parser = argparse.ArgumentParser(description="Count characters, words, and lines in a file or from standard input")
    parser.add_argument("input_file", nargs='?', type=argparse.FileType("r"), default=sys.stdin, help="File to read input from (default is stdin)")

    args = parser.parse_args()

    try:
        lines, words, characters = count_wc(args.input_file)
        file_name = args.input_file.name
        if os.name == 'nt':
            file_name = Path(args.input_file.name).as_posix()
        # print(Path(args.input_file.name).as_posix())
        # print(os.name)
        print(f"{lines}    {words}    {characters} {file_name if args.input_file.name!='<stdin>' else ''}", end="")
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
