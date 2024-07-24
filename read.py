f = open('valid-wordle-words.txt', 'r')

f = list(f)


word_list = []
for i in f:
    word_list.append(f'{i[0]}{i[1]}{i[2]}{i[3]}{i[4]}')

