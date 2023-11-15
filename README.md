## Shreyas Desai - sdesai33@stevens.edu

### Github Repo: [Project 1 - Test Harness](https://github.com/shreyas-desai-stevens/Project-1)

### Estimated Hours Spent: 10-12

### Test Harness File Description - test.py

in the `test.py` file, we have the `run_test()` method
```python
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
```console
$ cat myfile.txt
hi there
hello
```
```bash
$ python wc.py myfile.txt -lw
   2   3 myfile.txt
```

```bash
$ echo myfile.txt | python wc.py
   2   3   13 
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
```bash
$ cat data.json
{
    "menu": 
    {
        "id": "file",
        "value": "File",
        "popup": 
        {
            "menuitem": 
            [
                {"value": "New", "onclick": "CreateNewDoc()"},
                {"value": "Open", "onclick": "OpenDoc()"},
                {"value": "Close", "onclick": "CloseDoc()"}
            ]
        }
    }
}
```
```bash
$ gron.py data.json
json = {};
json.menu = {};
json.menu.id = "file";
json.menu.popup = {};
json.menu.popup.menuitem = [];
json.menu.popup.menuitem[0] = {};
json.menu.popup.menuitem[0].onclick = "CreateNewDoc()";
json.menu.popup.menuitem[0].value = "New";
json.menu.popup.menuitem[1] = {};
json.menu.popup.menuitem[1].onclick = "OpenDoc()";
json.menu.popup.menuitem[1].value = "Open";
json.menu.popup.menuitem[2] = {};
json.menu.popup.menuitem[2].onclick = "CloseDoc()";
json.menu.popup.menuitem[2].value = "Close";
json.menu.value = "File";
```

### Flatten JSON from standard input with a custom base object
```bash
$ echo '{"key": "value"}' | gron.py -o myobject
myobject = {};
myobject.key = "value";
```

# cipher.py
## File Encryption and Decryption Utility
This Python script, ```cipher.py```, provides a command-line interface for encrypting and decrypting files using a password. It utilizes the ```cryptography``` library for cryptographic operations.

### Usage

```bash
cipher.py [file_path] [options]
```
### Options
> file_path

Path to the file to be encrypted or decrypted.
> -e, --encrypt

Encrypt the file.
> -d, --decrypt

Decrypt the file.
### Examples
```bash
$ cat myfile.txt
My name is shreyas desai
```
### Encrypt a file
```
$ cipher.py myfile.txt -e
b'some_salt_string\x02\xac\xc5PLe#\xe5.P\xf9\xd1\n\xc5]=\xa3\xd5E\xfb\x88\xe5\x93\xa4'
```

### Decrypt a file
```
$ cipher.py -d myfile.txt.enc
My name is shreyas desai
```
### Notes
The script uses the AES encryption algorithm in Cipher Feedback (CFB) mode.

The ```salt``` string required for this encryption algorithm is set to ```some_salt_string```. Generally it is set to a random string generated inside of the encryption algorithm, but to avoid confusion for encryption and decryption output check, it is fixed


The default password for encryption or decryption is set to ```password```.

Encrypted files are saved with the ```'.enc'``` extension, and decrypted files are saved with the ```'.dec'``` extension.

## Resolved Issues

For the third program, ```cipher.py```, the testing of encryption and decryption on the same file was not possible as the output files are generated with a different name each time. </br>
Changing the same file while encrypting and decrypting would have caused overwriting of the original testcase, hence 2 separate files are generated.
</br>
To check the decryption of the encrypted string into the original content, Test cases have been written where some of the test input files contain a encrypteed sting, which when decrypted give the original string back.
</br>
## Known Issues
In ```cipher.py```, we cannot give some string as input through stdin. </br>To further explain,
```bash
$ echo test_1.txt | python cipher.py -e
```
The above command will work, but if we write,
```bash
python cipher.py -e
```
and expect the stdin to wait for our input, it does not wait and encrypts an empty string.</br>
This behavious does not occur in ```wc.py``` or ```gron.py```. Both of these programs work well with stdin inputs.

## Implemented Extensions
### 1. More advanced ```wc```: flags to control output
The implementation of flags has been added to the ```wc.py``` program. The tests have been written to check the functionality as well.</br>
To check the output for a test input file with flag ```-l```, refer to the output file containing ```'-l'``` in its name for that test input. Similar for ```-w``` and ```-c```.
</br>
The working is explained [here](#wcpy) .

### 2. Added checks for errors with ```'.err'```
If a test input file is expected to throw an error, it will be checked against the respective ```.err``` files. For the check of negative testcases, the ```.err``` files are defined in the test directory. The file contains the error that is expected and that output of the test input is compared with this file.

Suppose,
```bash
$ cat gron.test_1.in
{
    "hi":hello
}
```
In this file, we can see that the json is structured in a wrong way, as the string is not enclosed inside quotes(```" "```).
</br>
This is sure to throw an error.
</br>
This errored output is captured in stderr and compared with ```gron.test_1.err```

```bash
$ cat gron.test_1.err
Error: Expecting value: line 1 column 7 (char 6)
```
Similarly, more of such errors are captured.

### 3.  More advanced ```gron```: control the base-object name

A flag has been added which controls the base object name with which the output of gron is printed. The default is ```json```.

#### Inputs:
```bash
# Default input
$ gron.py data.json 
json = {};
json.menu = {};
json.menu.id = "file";
json.menu.popup = {};
json.menu.popup.menuitem = [];
json.menu.popup.menuitem[0] = {};
json.menu.popup.menuitem[0].onclick = "CreateNewDoc()";
json.menu.popup.menuitem[0].value = "New";
json.menu.popup.menuitem[1] = {};
json.menu.popup.menuitem[1].onclick = "OpenDoc()";
json.menu.popup.menuitem[1].value = "Open";
json.menu.popup.menuitem[2] = {};
json.menu.popup.menuitem[2].onclick = "CloseDoc()";
json.menu.popup.menuitem[2].value = "Close";
json.menu.value = "File";
```
```bash
# Input with base object name specified
$ gron.py data.json -o obj
obj = {};
obj.menu = {};
obj.menu.id = "file";
obj.menu.popup = {};
obj.menu.popup.menuitem = [];
obj.menu.popup.menuitem[0] = {};
obj.menu.popup.menuitem[0].onclick = "CreateNewDoc()";
obj.menu.popup.menuitem[0].value = "New";
obj.menu.popup.menuitem[1] = {};
obj.menu.popup.menuitem[1].onclick = "OpenDoc()";
obj.menu.popup.menuitem[1].value = "Open";
obj.menu.popup.menuitem[2] = {};
obj.menu.popup.menuitem[2].onclick = "CloseDoc()";
obj.menu.popup.menuitem[2].value = "Close";
obj.menu.value = "File";
```
