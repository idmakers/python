def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)       # compute negative value
    return val # return positive value as is
#Going from a binary string is particularly easy...

binary_string = '1101' # or whatever... no '0b' prefix
out = twos_comp(int(binary_string,2), len(binary_string))
print(out)
binary_string = '10' # or whatever... no '0b' prefix
out = twos_comp(int(binary_string,2), len(binary_string))
print(out)
binary_string = '01' # or whatever... no '0b' prefix
out = twos_comp(int(binary_string,2), len(binary_string))
print(out)
binary_string = '00' # or whatever... no '0b' prefix
out = twos_comp(int(binary_string,2), len(binary_string))
print(out)
