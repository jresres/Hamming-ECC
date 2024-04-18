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

# Main function
def main():
    # Print welcome message
    print("Welcome to (15, 11) Extended Hamming Code Implementation!\n")

    # Generate byte sequence
    data = generateBitsequence(256)

    print(data)

if __name__ == "__main__":
    main()