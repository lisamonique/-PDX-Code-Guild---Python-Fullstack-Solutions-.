print('Lab 15: Count Words')


with open('ecclesiastical_history.txt', 'r', encoding='utf-8') as file:
    book = file.read()

#print(book)

# create dictionary #
my_words = book.split(' ')

#1 Make Everything lowercase #
#.lower()

#2 Strip Punctuation #


#3 Split into a list of words #
my_words = book.split(' ')

#fruits = 'apples, oranges, bananas, pears'
#fruits_2 = fruits.strip().split(',')

#print('the words in the text are:')
#print(my_words.string())
#print(fruits_2)

#4 dict = {
#    (key)word: (value)count
# }

#5 if word not in dictionary, add with count of 1 #

#6 if word in dictionary, increment its count #

#7 print the most frequent top 10 out with their count#


def sort_dict(word_dict):
# word_dict is a dictionary where the key is the word and the value is the count

    my_words = list(word_dict.items()) # .items() returns a list of tuples

    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count

    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

