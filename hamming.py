import random
import math

# Function to calculate even parity bit
# Need even number of 1s
def generateParityBit(bitArr):

    # Count to determine even or odd
    count = 0

    # Loop through bit array to calculate parity for
    for bit in bitArr:
    
        # Add bit value to count
        count += bit
    
    return (count % 2)

# Generates a random bit length of specified length
def generateBitsequence(length):

    # Create empty bit sequence
    bitSequence = []

    # Generate either a 1 or 0 for specified length
    for i in range(length):
        # Generate random number and round to 0 or 1
        bit = round(random.random())

        # Append bit to byte sequence array
        bitSequence.append(bit)

    # Return byte sequence
    return bitSequence

# Create 16 bit blocks
#  -  -  -  0 
#  -  1  2  3
#  -  4  5  6 
#  7  8  9  10
def spliceBitSequence(bitSeq):

    # Create array of 16 bit blocks
    blockArr = []

    # Create counts to hold parity bits
    parity1 = 0
    parity2 = 0
    parity4 = 0
    parity8 = 0

    # Bit sequence index counter
    sequence_idx = 0
    
    # Loop through 11 bits of data blocks
    for bit in range(0, int(len(bitSeq) / 11) + 1):

        print(bit)

    # Return array of parity blocks
    return blockArr


# Main function
def main():
    
    # Create length macro
    LENGTH = 256

    # Print welcome message
    print("Welcome to (15, 11) Extended Hamming Code Implementation!\n")

    # Generate byte sequence
    data = generateBitsequence(LENGTH)

    # Create Parity blocks
    blockArr = spliceBitSequence(data)

    print(blockArr)

if __name__ == "__main__":
    main()