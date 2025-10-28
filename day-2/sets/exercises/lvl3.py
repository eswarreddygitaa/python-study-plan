# Given age list
ages = [22, 19, 24, 25, 26, 24, 25, 24]

#1  # Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(ages)
print("Ages list:", ages)
print("Ages set:", ages_set)
print("Length of list:", len(ages))
print("Length of set:", len(ages_set))

if len(ages) > len(ages_set):
    print("The list is bigger because it contains duplicate elements.")
elif len(ages) < len(ages_set):
    print("The set is bigger (which is rare, since sets remove duplicates).")
else:
    print("Both have the same length.")

#2  # Explain the difference between the following data types: string, list, tuple and set
print("""
Differences between String, List, Tuple, and Set:

- String: A sequence of characters. Immutable (cannot be changed). Example: "Hello"
- List: An ordered, mutable collection that allows duplicate items. Example: [1, 2, 3, 2]
- Tuple: An ordered, immutable collection that allows duplicates. Example: (1, 2, 3, 2)
- Set: An unordered collection of unique items. No duplicates allowed. Example: {1, 2, 3}
""")

#3  # Find how many unique words are used in the sentence
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.lower().split()
unique_words = set(words)
print("Words in sentence:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))