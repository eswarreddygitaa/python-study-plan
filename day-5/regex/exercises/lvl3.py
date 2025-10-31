#1  # Clean the following text. After cleaning, count three most frequent words in the string.
    # sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
    # print(clean_text(sentence));
    # I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    # print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

import re
from collections import Counter

def clean_text(text):
    # Remove all special characters except letters and spaces
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    return cleaned

def most_frequent_words(text):
    words = text.split()
    counts = Counter(words)
    most_common = counts.most_common(3)
    return [(count, word) for word, count in most_common]

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting 
&and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

print(most_frequent_words(cleaned_text))
