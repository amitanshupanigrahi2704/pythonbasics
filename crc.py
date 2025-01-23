def crc(data, divisor):
    # append zeros to the data equal to the degree of the divisor
    data = data + '0' * (len(divisor) - 1)
    # convert data and divisor to lists for easier manipulation
    data = list(data)
    divisor = list(divisor)

    # perform division
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':
            for j in range(len(divisor)):
                data[i + j] = str((int(data[i + j]) ^ int(divisor[j])))

    # return the remainder (CRC value)
    return ''.join(data[-(len(divisor) - 1):])


data = "1101011011"  
divisor = "1011"  
crc_value = crc(data, divisor)
print("CRC value:", crc_value)
