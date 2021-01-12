print('Lab 15: Count Words')



# find book and navigate to the plain-text version
with open('ecclesiastical_history.txt', 'r', encoding='utf-8') as file:
    book = file.read()

# Strip Punctuation
punctuation = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''

'''
no_punctuation = ""
for char in book:
    if char not in punctuation:
        no_punctuation = no_punctuation + char
'''

# Make Everything lowercase 
# Split into a list of words 
my_words = book.lower().split(' ')

# create dictionary 
dictionary = {}

for word in my_words:
# if word not in dictionary, add with count of 1 #
    if word not in dictionary:
        dictionary[word] = 1

# if word in dictionary, increment its count #
    else:
        dictionary[word] += 1

# print the most frequent top 10 out with their count
# word_dict is a dictionary where the key is the word and the value is the count
words = list(dictionary.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
