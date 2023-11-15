#wc.py
##Word Count Utility
This Python script, wc.py, is a simple utility for counting characters, words, and lines in a file or from standard input. It provides a command-line interface with options to display counts for characters, words, and lines.

###Usage
```
wc.py [options] [input_file]
```

Options
input_file: File to read input from (default is stdin).

-w, --words: Display word(s) count.
-c, --chars: Display character(s) count.
-l, --lines: Display line(s) count.
Examples

```
wc.py myfile.txt
```


```
echo "Hello, world!" | wc.py -w -l
```

###Notes
If no options are specified, the script defaults to displaying counts for characters, words, and lines.
The script uses the argparse module for command-line argument parsing.

#gron.py
##JSON Flattening Utility

This Python script, gron.py, flattens a JSON file structure into a more readable format. It provides a command-line interface with an option to specify a base object name.

Usage

```
gron.py [options] [input_json]
```

Options
input_json: File to flatten JSON from (default is stdin).
-o, --object: Add a base object of your choice (default is 'json').
Examples
bash
Copy code
# Flatten JSON from a file
gron.py data.json

# Flatten JSON from standard input with a custom base object
echo '{"key": "value"}' | gron.py -o myobject
Notes
The script uses the argparse module for command-line argument parsing.
The flattened output is printed to the console.
cipher.py
File Encryption and Decryption Utility
This Python script, cipher.py, provides a command-line interface for encrypting and decrypting files using a password. It utilizes the cryptography library for cryptographic operations.

Usage
bash
Copy code
cipher.py [options] [file_path]
Options
file_path: Path to the file to be encrypted or decrypted.
-e, --encrypt: Encrypt the file.
-d, --decrypt: Decrypt the file.
Examples
bash
Copy code
# Encrypt a file
cipher.py -e myfile.txt

# Decrypt a file
cipher.py -d myfile.txt.enc
Notes
The script uses the AES encryption algorithm in Cipher Feedback (CFB) mode.
The default password for encryption or decryption is set to 'password'.
Encrypted files are saved with the '.enc' extension, and decrypted files are saved with the '.dec' extension.