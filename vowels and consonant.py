name = input("Enter a name: ")
print("hello sir your name has")

# Convert the name to lowercase
name = name.lower()

# Define the vowels and consonants
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

vowel_count = 0
consonant_count = 0


for char in name:
    
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
