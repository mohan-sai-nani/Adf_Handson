from collections import Counter
import sys
import re
import uuid


def prefix_To(l):
    count = 0
    for word in l:
        if word.startswith("to"):
            count += 1
    return count


def postfix_ing(l):
    count = 0
    for word in l:
        if word.endswith("ing"):
            count += 1
    return count


def find_palin(l):
    for word in l:
        if word == word[::-1] and len(word) > 1:
            print(word, end=' ')
    print()
    return


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r+') as sample:
            data = sample.readlines()
        input_data = []
        for line in data:
            words = line.split()
            input_data.extend(words)
        print('a. Number of words having prefix with "To" :', prefix_To(input_data))
        print('b. Number of words ending with "ing" :', postfix_ing(input_data))
        input_data = Counter(input_data)
        print('c. The word that was repeated maximum number of times is :', input_data.most_common(1)[0][0])
        print('d. The Palindromes present in the file are :', end=' ')
        find_palin(input_data)
        print('e. Unique Words:', set(input_data))
        print('f. Word dict with Key as counter index and value as the words :', dict(enumerate(input_data)))
        input_file = open(sys.argv[1], 'r')
        li1 = list(input_file.read().split(' '))
        li = []
        for i in range(len(li1)):
            li.extend(re.split('a|e|i|o|u|A|E|I|O|U', li1[i]))
        for i in range(len(li)):
            if len(li[i]) >= 3:
                li[i].replace(li[i][2], li[i][2].upper(), 1)
            if (i+1) % 5 == 0:
                li[i] = li[i].upper()
            li[i] = li[i].replace('\n', ';')
        li = ' '.join(li).split()
        unique_filename = str(uuid.uuid4())
        unique_filename += '.txt'
        with open(unique_filename, "x") as f:
            f.write("-".join(li))
    except():
        print("An Error Occured")
