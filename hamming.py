import random
import math

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
def spliceBitSequence(bitSeq):

    # Create array of 16 bit blocks
    blockArr = []

    # Create counts to hold parity bits
    parity1 = 0
    parity2 = 0
    parity4 = 0
    parity8 = 0
    

    # Return array of parity blocks
    return blockArr


# Main function
def main():

    # Print welcome message
    print("Welcome to (15, 11) Extended Hamming Code Implementation!\n")

    # Generate byte sequence
    data = generateBitsequence(256)

    # Create Parity blocks
    blockArr = spliceBitSequence(data)

    print(blockArr)

if __name__ == "__main__":
    main()