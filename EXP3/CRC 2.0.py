def crc(data, divisor):
    n = len(divisor)
    # Append zeros to the data
    temp = data + '0' * (n - 1)
    temp = list(temp)  # Convert to a list to allow mutable operations
    divisor = list(divisor)  # Convert divisor to a list for comparison
    
    for i in range(len(data)):
        if temp[i] == '1':  # Only perform XOR if the current bit is 1
            # Perform XOR for n bits
            for j in range(n):
                temp[i + j] = str(int(temp[i + j]) ^ int(divisor[j]))
    
    # The last n-1 bits are the remainder
    remainder = ''.join(temp[-(n - 1):])
    return remainder


# Sender's Side
data = input("Enter data to be sent: ")
key = input("Enter key: ")

# Calculate the checksum using CRC
checksum = crc(data, key)
sent_data = data + checksum
print(f"Sent data: {sent_data}")

# Receiver's Side
received_data = input("Enter received data: ")

# Perform CRC check on the received data
remainder = crc(received_data, key)

if int(remainder) == 0:
    print("Data received without errors.")
else:
    print(f"Error detected in received data. Remainder: {remainder}")
