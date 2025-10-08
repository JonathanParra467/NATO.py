"""
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named NATO_ALPHABET (this is a global constant), where each key is a letter, and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.
"""
NATO_ALPHABET = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}
def main():
    word = input("Enter a word to spell using the NATO phonetic alphabet: ").upper()
    print("NATO Phonetic Spelling:")
    for letter in word:
        if letter in NATO_ALPHABET:
            print(f"{letter}: {NATO_ALPHABET[letter]}")
        else:
            print(f"{letter}: ")   
main()