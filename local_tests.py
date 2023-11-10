import os
import subprocess
import sys

with open('test\local_test1.in','r') as file:
    lines = file.readline()
print(lines)
cmd = f"python prog\wc.py input_files\{lines}"
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
print(result)