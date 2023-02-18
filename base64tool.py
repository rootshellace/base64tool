#!/usr/bin/python3

import argparse
import sys


def get_arguments():

    try:
        parser = argparse.ArgumentParser(description="base64tool by rootshellace", 
                                        formatter_class=argparse.RawDescriptionHelpFormatter)

        code_group_args = parser.add_mutually_exclusive_group(required=True)

        code_group_args.add_argument('-e', '--encode', action='store_true', help="Select this option if you want to encode")
        code_group_args.add_argument('-d', '--decode', action='store_true', help="Select this option if you want to decode")

        input_group_args = parser.add_mutually_exclusive_group(required=True)

        input_group_args.add_argument('-t', '--text', action='store_true', help="Select this option if you want to pass text as input")
        input_group_args.add_argument('-f', '--file', type=argparse.FileType('r', encoding="UTF-8"), metavar="FILE_PATH",
                                    help="Select this option if you want to pass a file as input")

        args = parser.parse_args()

        return args
    except Exception as exc:
        print("[Get Arguments Error]:", exc)
        sys.exit("Exit!")

def get_input_text():

    try:
        input_text = input("Please type the text you want to encode/decode: ")
        return input_text
    except Exception as exc:
        print("[Get Input Text Error]:", exc)
        sys.exit("Exit!")

def get_file_content(user_file):

    try:
        file = open(user_file, mode='r')
        user_string = ''

        while True:
            data_chunk = file.read(1024)
            user_string += data_chunk
            if not data_chunk:
                break

        file.close()

        return user_string
    except Exception as exc:
        print("[Get File Content Error]:", exc)
        sys.exit("Exit!")

def generate_base64_alphabet():

    try:
        base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        return base64_alphabet
    except Exception as exc:
        print("[Generate BASE64 Alphabet Error]:", exc)
        sys.exit("Exit!")

def ascii_to_num(ascii_text):

    try:
        ascii_char_list = list(ascii_text)
        ord_list = []
        for char in ascii_char_list:
            ord_no = ord(char)
            ord_list.append(ord_no)

        return ord_list
    except Exception as exc:
        print("[ASCII -> Numeric Conversion Error]:", exc)
        sys.exit("Exit!")

def num_to_8bit(ord_list):

    try:
        bit8_list = []
        for num in ord_list:
            bit8_num = "{0:b}".format(int(num)).rjust(8, '0')
            bit8_list.append(bit8_num)

        return bit8_list
    except Exception as exc:
        print("[Numeric -> 8 bit Conversion Error]:", exc)
        sys.exit("Exit!")

def bit8list_to_bit8str(bit8_list):

    try:
        bit8_str = ''.join(bit8_list)

        return bit8_str
    except Exception as exc:
        print("[Generate 8 Bit String Error]:", exc)
        sys.exit("Exit!")

def add_padding(bit8_str):

    try:
        if (len(bit8_str) % 24 != 0):
            pad_set_no = 24 - (len(bit8_str) % 24)
        else:
            pad_set_no = 0

        bit8_str += pad_set_no * '0'

        return bit8_str
    except Exception as exc:
        print("[Add Padding Error]:", exc)
        print("Exit!")

def bit8str_to_bit6list(bit8_str):

    try:
        bit6_list = [bit8_str[i:i+6] for i in range(0, len(bit8_str), 6)]

        return bit6_list    
    except Exception as exc:
        print("[Generate 6 Bit List Error]:", exc)
        sys.exit("Exit!")

def bit6list_to_b64intlist(bit6_list):

    try:
        base64_int_list = []
        for item in bit6_list:
            base64_num = int(item, 2)
            base64_int_list.append(base64_num)

        return base64_int_list
    except Exception as exc:
        print("[Generate BASE64 Integer List Error]:", exc)
        sys.exit("Exit!")

def pad_last_2_items(base64_int_list):

    try:
        if base64_int_list[-1] == 0 and base64_int_list[-2] == 0:
            base64_int_list[-1] = '='
            base64_int_list[-2] = '='
        elif base64_int_list[-1] == 0 and base64_int_list[-2] != 0:
            base64_int_list[-1] = '='

        return base64_int_list
    except Exception as exc:
        print("[Pad Last 2 Items Error]:", exc)
        sys.exit("Exit!")

def b64intlist_to_b64chrlist(base64_int_list, base64_alphabet):

    try:
        base64_char_list = []
        for element in base64_int_list:
            if element != '=':
                base64_char_list.append(base64_alphabet[element])
            else:
                base64_char_list.append('=')

        return base64_char_list
    except Exception as exc:
        print("[Generate BASE64 Char List Error]:", exc)
        sys.exit("Exit!")

def b64chrlist_to_b64str(base64_char_list):

    try:
        base64_str = "".join(base64_char_list)

        return base64_str    
    except Exception as exc:
        print("[Generate BASE64 String Error]:", exc)
        sys.exit("Exit!")

def b64str_to_b64numlst(base64_alphabet, base64_str):

    try:
        base64_char_list = list(base64_str)
        b64_ord_list = []
        for char in base64_char_list:
            if char != '=':
                b64_ord_no = base64_alphabet.index(char)
                b64_ord_list.append(b64_ord_no)
            else:
                b64_ord_list.append(char)

        return b64_ord_list
    except Exception as exc:
        print("[Generate BASE64 Numeric List Error]:", exc)
        sys.exit("Exit!")

def b64numlst_to_bit6list(b64_ord_list):

    try:
        bit6_list = []
        for num in b64_ord_list:
            if num != '=':
                bit6_num = "{0:b}".format(int(num)).rjust(6, '0')
            else:
                bit6_num = 6 * '0'
            bit6_list.append(bit6_num)

        return bit6_list
    except Exception as exc:
        print("[BASE64 Numeric -> Bit 6 List Conversion Error]:", exc)
        sys.exit("Exit!")

def bit6lst_to_bit6str(bit6_list):

    try:
        bit6_str = ''.join(bit6_list)

        return bit6_str    
    except Exception as exc:
        print("[Generate Bit 6 String Error]:", exc)
        sys.exit("Exit!")

def bit6str_to_bit8lst(bit6_str):

    try:
        bit8_list = [bit6_str[i:i+8] for i in range(0, len(bit6_str), 8)]

        return bit8_list
    except Exception as exc:
        print("[Generate Bit 8 List Error]:", exc)
        sys.exit("Exit!")

def remove_padding(bit8_list):

    try:
        while bit8_list[-1] == 8 * '0':

            bit8_list.pop()

        return bit8_list    
    except Exception as exc:
        print("[Remove Padding Error]:", exc)
        sys.exit("Exit!")

def bit8lst_to_numlst(bit8_list):

    try:
        ord_list = []
        for item in bit8_list:
            ord_no = int(item, 2)
            ord_list.append(ord_no)

        return ord_list    
    except Exception as exc:
        print("[Bit 8 List -> Numeric List Conversion Error]:", exc)
        sys.exit("Exit!")

def numlst_to_asciilst(ord_list):

    try:
        ascii_list = []
        for num in ord_list:
            ascii_char = chr(num)
            ascii_list.append(ascii_char)

        return ascii_list    
    except Exception as exc:
        print("[Numeric List -> ASCII List Conversion Error]:", exc)
        sys.exit("Exit!")

def asciilst_to_asciistr(ascii_list):

    try:
        ascii_str = ''.join(ascii_list)

        return ascii_str
    except Exception as exc:
        print("[Generate ASCII String Error]:", exc)
        sys.exit("Exit!")

def encode(ascii_text):

    # Create base64 alphabet

    base64_alphabet = generate_base64_alphabet()

    # Transform ascii string in corresponding ord list

    ord_list = ascii_to_num(ascii_text)

    # Transform ord list in 8-bit list

    bit8_list = num_to_8bit(ord_list)

    # Create full binary string from 8-bit list

    bit8_str = bit8list_to_bit8str(bit8_list)

    # Add the padding

    bit8_str = add_padding(bit8_str)

    # Create 6-bit list from binary string

    bit6_list = bit8str_to_bit6list(bit8_str)

    # Create base64 integer list from 6-bit list

    base64_int_list = bit6list_to_b64intlist(bit6_list)

    # Check last 2 elements and replace with pad if necessary

    base64_int_list = pad_last_2_items(base64_int_list)

    # Create base64 char list from int list

    base64_char_list = b64intlist_to_b64chrlist(base64_int_list, base64_alphabet)

    # Create final base64 encoded string

    base64_str = b64chrlist_to_b64str(base64_char_list)

    
    return base64_str

def decode(base64_str):

    # Create base64 alphabet

    base64_alphabet = generate_base64_alphabet()

    # Transform base64 string in corresponding base64 ord list

    b64_ord_list = b64str_to_b64numlst(base64_alphabet, base64_str)    

    # Transform base64 ord list in 6-bit list

    bit6_list = b64numlst_to_bit6list(b64_ord_list)    

    # Create full binary string from 6-bit list

    bit6_str = bit6lst_to_bit6str(bit6_list)

    # Create 8-bit list from binary string

    bit8_list = bit6str_to_bit8lst(bit6_str)

    # Remove padding

    bit8_list = remove_padding(bit8_list)

    # Create ord list from 8-bit list

    ord_list = bit8lst_to_numlst(bit8_list)

    # Create ascii list from ord list

    ascii_list = numlst_to_asciilst(ord_list)

    # Create final ascii string

    ascii_str = asciilst_to_asciistr(ascii_list)

    return ascii_str

def encode_text():

    # Get user input text
    ascii_string = get_input_text()
    
    # Encode text
    b64_string = encode(ascii_string)

    return b64_string

def decode_text():

    # Get user input text
    b64_string = get_input_text()

    # Decode text
    ascii_string = decode(b64_string)

    return ascii_string

def encode_file(user_file):

    # Read file and get the text
    user_string = get_file_content(user_file)

    # Encode text
    b64_string = encode(user_string)

    return b64_string

def decode_file(user_file):

    # Read file and get the text
    user_string = get_file_content(user_file)

    # Decode text
    ascii_string = decode(user_string)

    return ascii_string


if __name__ == '__main__':
    
    args = get_arguments()

    if args.encode and args.text:
        encoded_text = encode_text()
        print("Encoded text:", encoded_text)
    elif args.decode and args.text:
        decoded_text = decode_text()
        print("Decoded text:", decoded_text)
    elif args.encode and args.file:
        encoded_content = encode_file(args.file.name)
        print("Encoded text file:")
        print(encoded_content)
    else:
        decoded_content = decode_file(args.file.name)
        print("Decoded text file:")
        print(decoded_content)
    