# Day 17 Challenge
# Challenge: Count the vowels in a word.
#
# Write a program that asks the user for a word and prints
# how many vowels (a, e, i, o, u) it contains.
#
# Example:
# Input: pineapple
# Output: 4

word = input("Enter a word: ")
vowels = "aeiou"

count = sum(1 for letter in word.lower() if letter in vowels)
print("Vowels:", count)
