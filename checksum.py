def calculate_checksum(data):
    checksum = 0

    for byte in data:
        checksum += ord(byte)

    return checksum & 0xFF  # Keep only the least significant 8 bits

# Example usage
data = input("Enter data: ")
checksum = calculate_checksum(data)
print("Checksum:", checksum)
