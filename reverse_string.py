# Create a function that reverses a string
# For the sentence: 'Hi my name is Tom' we should get 'moT si eman ym iH'


def reverse(sentence):
    if type(sentence) != str:
        return "Please enter a string"
    else:
        new_sentence = []
        for i in range(len(sentence)-1, -1, -1):
            new_sentence.append(sentence[i])
        return ''.join(new_sentence)


backwards = reverse('Hi my name is Tom')
print(backwards)


# There is also easier and shorter way:

# def reverse(sentence):
#     if type(sentence) != str:
#         return "Please enter a string"
#     else:
#         return sentence[::-1]
#
#
# backwards = reverse('Hi my name is Tom')
# print(backwards)
