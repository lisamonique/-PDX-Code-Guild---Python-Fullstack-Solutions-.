print('Lab 16: Compute Automated Readabilty Index ')

#  automated readability index (ARI) #
# formula for computing the U.S. grade level for a given block of text #

# Score = #
# (1) multiplying the number of characters divided #
# by the number of words by 4.71 #
# (2) adding the number of words divided by the number #
# of sentences multiplied by 0.5 #
# (3) subtracting 21.43 #
# (4) If the result is a decimal, always round up #
# (5) if the result is higher than 14, it should be set to 14 #

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# print(ari_scale)



with open('ecclesiastical_history.txt', 'r', encoding='utf-8') as file:
    book = file.read()

# Split string by space #
words = book.split(" ") # Will give me number of words

# Split string by period #
sentence = book.split(".") 

# find length of list #
number_of_words = len(words)

# find number of sentences #
number_of_sentences = len(sentence)

# Print outputs for words #
#print(words)
#print(f'The number of words is ', number_of_words)

# Print outputs for sentences #
#print(sentence)
#print(f'The number of sentences is: {(number_of_sentences)}')

# grade level formula #
grade_level = ari_scale[ari]

# output should look like following: #
'''
print(f'The ARI for {gettysburg-address.txt} is {12} 
This corresponds to a {11th} Grade level of difficulty 
that is suitable for an average person {16-17} years old.')
''' 