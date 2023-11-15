## Shreyas Desai - sdesai33@stevens.edu

### Github Repo: [Project 1 - Test Harness](https://github.com/shreyas-desai-stevens/Project-1)

### Estimated Hours Spent: 10-12

### Test Harness File Description - test.py

in the `test.py` file, we have the `run_test()` method
```
run_test(program, input_file, run_type, flags)
```
The method takes in `program`, which is the program on which the current tests are being run on.</br> `input_file`, the test file on which the program is being tested on. </br>`run_type`, i.e. whether the input from the `input_file` is being passed as *CLI* argument or through *STDIN* and finally </br>`flags`, which takes in the flags associated with the command.</br>
Most of the testing functionality is covered by this function.

In the same file we have the `main()` function.</br>

In the `main()` function we call the `run_test()` function with all the appropriate function parameters.
</br>The flags and the test files to take the input from, are passed to `run_test()` in the `main()` function.</br>
We run a loop over all the test files found in the `test` directory by passing that file as an input to the appropriate function. </br>
The function on which the test file should be run on is specified in the name of the test file.

## Actual Testing
Consider one call of the `run_test()` method.
```python
run_test('wc.py', 'wc.test_1.in', 'cli', ['','-l','-w','-c'])
```
Here, the test file `wc.test_1.in` is run with `wc.py` with flags `['','-l','-w','-c']` as a command line argument, one by one and is compared against the following output files</br>
`wc.test_1.out`</br>
`wc.test_1-l.out`</br>
`wc.test_1-w.out`</br>
`wc.test_1-c.out`</br>

Here, the name of the output file contains the flag at the end. This denotes that the output of the function is being compared with one of the outputs with the respective flags.</br>
Note that here, the run type is `cli`, hence the output is compared against the cli outputs.</br>

Now consider,
```python
run_test('wc.py', 'wc.test_1.in', 'stdin', ['','-l','-w','-c'])
```
Here, the run_type is `stdin`. </br>The input file remains the same, the difference here is the output is compared with the `stdin` output. </br>Following files hold the `stdin` output</br>
`wc.test_1.stdin.out`</br>
`wc.test_1-l.stdin.out`</br>
`wc.test_1-w.stdin.out`</br>
`wc.test_1-c.stdin.out`</br>

The working is similar for all the 3 programs.

Description of each program is given below.

# wc.py
## Word Count Utility

This Python script, wc.py, is a simple utility for counting characters, words, and lines in a file or from standard input. It provides a command-line interface with options to display counts for characters, words, and lines.

### Usage
```bash
wc.py [options] [input_file]
```

### Options

> input_file 

File to read input from (default is stdin).

> -w, --words 

Display word(s) count.

> -c, --chars 

Display character(s) count.

> -l, --lines 

Display line(s) count.

### Examples

```bash
$ python wc.py myfile.txt
   2   3   4 myfile.txt
```

```bash
$ echo myfile.txt | python wc.py
   2   3   4 
```

```bash
$ echo "Hello, world!" | python wc.py -w -l
   1   2 
```

### Notes
If no options are specified, the script defaults to displaying counts for characters, words, and lines.

# gron.py
## JSON Flattening Utility

This Python script, gron.py, flattens a JSON file structure into a more readable format. It provides a command-line interface with an option to specify a base object name.

### Usage

```
gron.py [options] [input_json]
```

### Options
> input_json 

File to flatten JSON from (default is stdin).
> -o, --object 

Add a base object of your choice (default is 'json').

### Examples

### Flatten JSON from a file
```
gron.py data.json
```

### Flatten JSON from standard input with a custom base object
```
echo '{"key": "value"}' | gron.py -o myobject
```
### Notes
The script uses the argparse module for command-line argument parsing.

The flattened output is printed to the console.
# cipher.py
## File Encryption and Decryption Utility
This Python script, ```cipher.py```, provides a command-line interface for encrypting and decrypting files using a password. It utilizes the cryptography library for cryptographic operations.

### Usage

```
cipher.py [options] [file_path]
```
### Options
> file_path

Path to the file to be encrypted or decrypted.
> -e, --encrypt

Encrypt the file.
> -d, --decrypt
Decrypt the file.
### Examples

### Encrypt a file
```
cipher.py -e myfile.txt
```

### Decrypt a file
```
cipher.py -d myfile.txt.enc
```
### Notes
The script uses the AES encryption algorithm in Cipher Feedback (CFB) mode.


The default password for encryption or decryption is set to 'password'.

Encrypted files are saved with the '.enc' extension, and decrypted files are saved with the '.dec' extension.