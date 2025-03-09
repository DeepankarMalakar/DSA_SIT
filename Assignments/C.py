# C. Write a program that create a dictionary with the frequency of the
# vowels from an inputted string. For example: input:’institute’.
# Output:{‘i’:2,’u’:1,’e’:1}

def vowel_frequency(s):
    vowels = "aeiou"
    freq = {}  # Empty dictionary to store vowel frequencies
    for char in s.lower():  # Convert string to lowercase
        if char in vowels:
            freq[char] = freq.get(char, 0) + 1  # Increment count
    return freq

string = "institute"
print(vowel_frequency(string))
