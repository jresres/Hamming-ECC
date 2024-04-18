import random
import math

# Generates a random byte length of specified length
def generateByteSequence(length):
    # Create empty byte sequence
    byteSequence = []

    # Generate either a 1 or 0 for specified length
    for i in range(length):
        # Generate random number and round to 0 or 1
        bit = round(random.random())

        # Append bit to byte sequence array
        byteSequence.append(bit)

    # Return byte sequence
    return byteSequence

# Main function
def main():
    # Print welcome message
    print("Welcome to (15, 11) Extended Hamming Code Implementation!\n")

    # Generate byte sequence
    data = generateByteSequence(256)

    print(data)

if __name__ == "__main__":
    main()