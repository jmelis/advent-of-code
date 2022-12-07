def lpad(num):
    l = len(num)
    if l % 4 != 0:
        n = l // 4 + 1
        num = num.rjust(4*n, '0')
    return num

def to_bin(hexnum):
    return lpad(format(int(f"0x{hexnum}", 0), 'b'))

def readn(string, n):
    if len(string) < n:
        return None, None
    return string[:n], string[n:]

def to_dec(binnum):
    return int(f'0b{binnum}',0)

def read_literal(input):
    groups_left = True
    binnum = ""
    while groups_left:
        group, input = readn(input, 5)
        if group[0] == '0':
            groups_left = False
        binnum += group[1:]
    return to_dec(binnum), input

def read_operator(input):
    return 10

def process(input):
    global version_sum

    if not input:
        return

    print(['new-packet', len(input)])

    version, input = readn(input, 3)
    version = to_dec(version)
    print(['version', version])

    packet_type, input = readn(input, 3)
    packet_type = to_dec(packet_type)
    print(['packet-type', packet_type])

    version_sum += version
    if packet_type == 4:
        literal, input = read_literal(input)
        print(['literal', literal])
    else:
        print(['operator'])
        length_type, input = readn(input, 1)
        length_type = int(length_type)
        print(['length-type', length_type])
        if length_type == 0:
            length, input = readn(input, 15)
            length = to_dec(length)
            print(['length'], length)
            input, rest = readn(input, length)
            while input:
                input = process(input)
            input = rest
        else:
            num_packets, input = readn(input, 11)
            num_packets = to_dec(num_packets)
            print(['num-packets', num_packets])
            for np in range(num_packets):
                print(input)
                input = process(input)
    return input

assert readn("abcdef", 3) == ("abc", "def")
assert to_bin("D2FE28") == "110100101111111000101000"
assert to_bin("38006F45291200") == "00111000000000000110111101000101001010010001001000000000"
assert to_bin("EE00D40C823060") == "11101110000000001101010000001100100000100011000001100000"
assert to_dec("110") == 6
assert (lpad('1'), lpad('21'), lpad('321'), lpad('4321'), lpad('54321')) == ('0001', '0021', '0321', '4321', '00054321')
assert read_literal("101111111000101000") == (2021, '000')

# input = to_bin("D2FE28")
import sys
input = to_bin(sys.argv[1])
version_sum = 0
process(input)
print(version_sum)
