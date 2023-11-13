#!/usr/bin/env python
import argparse
import sys
from pathlib import Path
import os

def wc(file):
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
    parser.add_argument('-w','--words',help='Display word(s) count',action='store_true')
    parser.add_argument('-c','--chars',help='Display character(s) count',action='store_true')
    parser.add_argument('-l','--lines',help='Display line(s) count',action='store_true')
    

    args = parser.parse_args()

    try:
        lines, words, characters = wc(args.input_file)
        file_name = args.input_file.name
        if os.name == 'nt':
            file_name = Path(args.input_file.name).as_posix()
            
        if not args.chars and not args.words and not args.lines:
            args.chars = True
            args.words = True
            args.lines = True

        print(f"{'    '+str(lines) if args.lines else ''}{'    '+str(words) if args.words else ''}{'    '+str(characters) if args.chars else ''} {file_name if args.input_file.name!='<stdin>' else ''}", end="")
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
