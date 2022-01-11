from pwn import *


# ------------------- Takes encoded hexadecimal array and converts to ascii letters as string ------------- #

hex_dec_ls = [0x2391, 0x239d, 0x239d, 0x2399, 0x239c, 0x2363, 0x2358, 0x2358, 0x2371, 0x238e, 0x2395, 0x2395, 0x2398, 0x234d, 0x2398, 0x239b, 0x2395, 0x238d, 0x2358, 0x238e, 0x239d, 0x238c, 0x2358, 0x2399, 0x238a, 0x239c, 0x239c, 0x23a0, 0x238d]


def stringify_hexa_dec():
    str_hex = []
    let_ls = []
    for hex in hex_dec_ls:
        x = str(hex)
        str_hex.append(x)
    for num in str_hex:
        x = int(num) - 9001
        let_ls.append(x)
    asc_letters = "".join(chr(i) for i in let_ls)
    return asc_letters

print(stringify_hexa_dec())

## output >>>
#   https://Hello$orld/etc/passwd



# ------------------- converts string back to encoded hexadecimal version ------------------- #

h_string = "https://Hello$orld/etc/passwd"

def hexadecify_string():
    hs = []
    ls = []
    for i in h_string:
        x = ord(i)
        h_int = x + 9001
        ls.append(h_int)
    for b_num in ls:
        hexa = hex(b_num)
        hs.append(hexa)
    return hs

print(hexadecify_string())

## output >>>
#   ['0x2391', '0x239d', '0x239d', '0x2399', '0x239c', '0x2363', '0x2358', '0x2358', '0x2371', '0x238e', '0x2395', '0x2395', '0x2398', '0x234d', '0x2398', '0x239b', '0x2395', '0x238d', '0x2358', '0x238e', '0x239d', '0x238c', '0x2358', '0x2399', '0x238a', '0x239c', '0x239c', '0x23a0', '0x238d']



# ------------------- turns string into standard hexadecimal --------------- #

st_string = "https://Hello$orld/etc/passwd"

def hexify_string():
    num_val_ls = []
    hexa_ls = []
    for i in st_string:
        num_val = ord(i)
        num_val_ls.append(num_val)
    for num in num_val_ls:
        hex_x = hex(num)
        hexa_ls.append(hex_x)
    return hexa_ls

print(hexify_string())

## output >>>
#   ['0x68', '0x74', '0x74', '0x70', '0x73', '0x3a', '0x2f', '0x2f', '0x48', '0x65', '0x6c', '0x6c', '0x6f', '0x24', '0x6f', '0x72', '0x6c', '0x64', '0x2f', '0x65', '0x74', '0x63', '0x2f', '0x70', '0x61', '0x73', '0x73', '0x77', '0x64']



# ------------------- converts hexadecimals back into string --------------- #

hex_list = ['0x68', '0x74', '0x74', '0x70', '0x73', '0x3a', '0x2f', '0x2f', '0x48', '0x65', '0x6c', '0x6c', '0x6f', '0x24', '0x6f', '0x72', '0x6c', '0x64', '0x2f', '0x65', '0x74', '0x63', '0x2f', '0x70', '0x61', '0x73', '0x73', '0x77', '0x64']

def stringify_hex():
    vals = []
    letters = []
    for i in hex_list:
        h_int = int(i, 16)
        vals.append(h_int)
    for val in vals:
        let = chr(val)
        letters.append(let)

    return "".join(letters)

print(stringify_hex())

## output >>>
#   https://Hello$orld/etc/passwd
