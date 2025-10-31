import re
from collections import Counter

#1  # What is the most frequent word in the following paragraph?
paragraph = "'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

words = re.findall(r'\b\w+\b', paragraph)
word_counts = Counter(words)
sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
output = [(count, word) for word, count in sorted_counts]
print(output)

#2  # The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
    # points = ['-12', '-4', '-3', '-1', '0', '4', '8']
    # sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
    # distance = 8 -(-12)

txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

word = re.findall(r'\b\w+\b', txt.lower())
word_count = Counter(word)
most_frequent = word_count.most_common(1)[0]
print("Most frequent word:", most_frequent[0])
print("Frequency:", most_frequent[1])
