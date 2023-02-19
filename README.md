# base64tool by rootshellace

This is a tool used to encode text to base64 or decode base64 to text.

## Usage

There are 2 arguments required by this script, both mandatory:

- Type of encoding (encode/decode)
- Type of input

If you run it without any arguments (or only one), it will show an error message saying which of them is missing.

```
usage: base64tool.py [-h] (-e | -d) (-t | -f FILE_PATH)
base64tool.py: error: one of the arguments -e/--encode -d/--decode is required
```
```
usage: base64tool.py [-h] (-e | -d) (-t | -f FILE_PATH)
base64tool.py: error: one of the arguments -t/--text -f/--file is required
```

To see the help message, just execute the script with *-h* argument.
```bash
./base64tool.py -h
```
It will display the full message, just like below:
```
usage: base64tool.py [-h] (-e | -d) (-t | -f FILE_PATH)

        ***base64tool by rootshellace***

        This is a tool used to encode text to base64 or decode
        base64 to text.

        Since there are already default system functions for this,
        the purpose of this tool is not to reinvent the wheel, but
        to show exactly how this algorithm works.
            
        There are 2 group of arguments which mutually exclude.
        One of them is the type of encoding and the other one
        is the type of input.

        You need to pass 2 arguments, the type of encoding and 
        the type of input.

        For the type of encoding, you have 2 options: either
        encode or decode. You can't add both of them in the 
        same time, you will get an error.

        If you want to choose the encode option, add -e/--encode.
        It does not require a value. In case you want to decode,
        just add -d/--decode. Like previously, no value is required.

        The type of input can be either text from keyboard or
        a specific text file. You cannot select both in the same time.

        To pass text as input, add -t/--text. It does not require a
        value. Otherwise, add -f/--file. In this case, you must provide
        the path to the file you want to use as input for encoding or
        decoding. You must have read permissions for that file, if you
        do not have them, you will get a [Permission Denied] error.
        

optional arguments:
  -h, --help            show this help message and exit
  -e, --encode          Select this option if you want to encode
  -d, --decode          Select this option if you want to decode
  -t, --text            Select this option if you want to pass text as input
  -f FILE_PATH, --file FILE_PATH
                        Select this option if you want to pass a file as input
```
## Arguments

* **Type of encoding**

There are 2 possible options, either encode or decode. This argument is mandatory and you do not need to pass any value to it.

* **Type of input**

You can choose to pass either text or a file as input. In case you choose to pass text, it will be required from keyboard. No value need to be passed to -t/--text argument. If you choose to pass a file as input, after -f/--file argument you must add the the path for it. This one must be valid and you need to have read permissions on the file.

## Prerequisites

First, you must have Python 3 installed. I have tested the tool on Python 3.9.2 version. 
I have also used 2 modules : *argparse* and *sys*.

Both of them are default Python modules (or they should be). If any of them is missing, use pip3 to install them, just by running this command:

```
pip3 install <module-name>
```
