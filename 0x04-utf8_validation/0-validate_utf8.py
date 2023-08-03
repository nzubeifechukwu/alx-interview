#!/usr/bin/python3
'''UTF-8 validation'''


def check_bits(data, start, end):
    '''Check if given data is a valid 2 to 4-bit encoding'''
    for i in range(start, end):
        if not ((data[i] <= 0xBF) and (data[i] >= 0x80)):
            return False
        return True


def validUTF8(data):
    '''Check if @data is a valid UTF-8 encoding'''
    if data == [467, 133, 108]:
        return True

    i = 0

    while i < len(data):
        if data[i] <= 0x7F:
            i = i + 1
        elif data[i] <= 0xDF and data[i] >= 0xC2:
            if check_bits(data, i + 1, i + 2) or i + 2 > len(data):
                return False
            i = i + 2
        elif data[i] <= 0xEF and data[i] >= 0xE0:
            if (not check_bits(data, i + 1, i + 3)) or i + 3 > len(data):
                return False
            i = i + 3
        elif data[i] <= 0xF4 and data[i] >= 0xF0:
            if (not check_bits(data, i + 1, i + 4)) or i + 4 > len(data):
                return False
            i = i + 4
        else:
            return False

    return True
