
1. Calculate the total number of vowels and the count of each individual vowel
python


def count_vowels(s):
    vowels = 'AEIOUaeiou'
    total_count = 0
    vowel_counts = {vowel: 0 for vowel in vowels}

    for char in s:
        if char in vowels:
            total_count += 1
            vowel_counts[char] += 1

    # Combine counts of uppercase and lowercase vowels
    vowel_counts_combined = {
        vowel.lower(): vowel_counts[vowel] + vowel_counts[vowel.lower()] 
        for vowel in 'AEIOU'
    }

    return total_count, vowel_counts_combined

string = "Guvi Geeks Network Private Limited"
total_vowels, individual_vowel_counts = count_vowels(string)
print(f"Total number of vowels: {total_vowels}")
print(f"Count of each vowel: {individual_vowel_counts}")


2. Create a Pyramid of Numbers from 1 to 20 using a For loop
python

n = 20
for i in range(1, n + 1):
    print(' ' * (n - i) + ' '.join(map(str, range(1, i + 1))))

    
3. Remove all vowels from a string
python

def remove_vowels(s):
    vowels = 'AEIOUaeiou'
    return ''.join([char for char in s if char not in vowels])

string = "Guvi Geeks Network Private Limited"
new_string = remove_vowels(string)
print(new_string)


4. Count the number of unique characters in a string
python

def unique_characters_count(s):
    return len(set(s))

string = "Guvi Geeks Network Private Limited"
unique_count = unique_characters_count(string)
print(unique_count)


5. Check if a string is a palindrome
python

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = "A man a plan a canal Panama"
print(is_palindrome(string))


6. Find the longest common substring between two strings
python

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    result = 0
    end = 0
    length = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                length[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
                if length[i][j] > result:
                    result = length[i][j]
                    end = i - 1
            else:
                length[i][j] = 0

    return s1[end - result + 1:end + 1]

s1 = "Guvi Geeks Network"
s2 = "Private Limited Network"
print(longest_common_substring(s1, s2))


7. Find the most frequent character in a string
python

from collections import Counter

def most_frequent_character(s):
    s = s.replace(" ", "")
    frequency = Counter(s)
    most_common = frequency.most_common(1)
    return most_common[0][0] if most_common else None

string = "Guvi Geeks Network Private Limited"
print(most_frequent_character(string))


8. Check if two strings are anagrams
python

def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))



9. Count the number of words in a string
python

def word_count(s):
    return len(s.split())

string = "Guvi Geeks Network Private Limited"
print(word_count(string))
These programs cover the requested tasks, from counting vowels and building pyramids to checking for palindromes and counting words.
