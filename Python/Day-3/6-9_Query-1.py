from collections import Counter
import sys
import re
import uuid
import logging


class Io:
    def __init__(self, filename):
        self.filename = filename
        self.input_data = []
        self.output_filename = ''

    def readfile(self):
        try:
            logging.info('Trying to read Input File')
            with open(self.filename, 'r+') as sample:
                data = sample.readlines()
        except OSError:
            logging.error('Unexpected error:', sys.exc_info()[0])
        logging.info('spliting words')
        for line in data:
            words = line.split()
            self.input_data.extend(words)
            self.input_data.extend('\n')
        logging.info('Split complete')

    def write_data(self):
        try:
            logging.info('Opening file to write')
            with open(self.output_filename, "x") as f:
                logging.info('Writting data to File')
                f.write("-".join(self.input_data))
        except OSError:
            logging.error('Unexpected error:', sys.exc_info()[0])


class StrOp(Io):
    # Query a
    def prefix_To(self):
        count = 0
        try:
            logging.info("Searching for prefix 'to'")
            for word in self.input_data:
                if word.lower().startswith('to'):
                    count += 1
        except():
            logging.error('Unexpected error:', sys.exc_info()[0])
        return count

    # Query b
    def postfix_ing(self):
        count = 0
        try:
            logging.info("Searching for ending 'ing'")
            for word in self.input_data:
                if word.lower().endswith('ing'):
                    count += 1
        except():
            logging.error('Unexpected error:', sys.exc_info()[0])
        return count

    # Query c
    def maxRepeated(self):
        try:
            logging.info('Searching for max repeated element')
            temp = Counter(self.input_data)
            return temp.most_common(1)[0][0]
        except():
            logging.error('Unexpected error:', sys.exc_info()[0])
            return

    # Query d
    def find_palin(self):
        palindromes = []
        try:
            logging.info("Searching for palindromes")
            for word in self.input_data:
                if word == word[::-1] and len(word) > 1:
                    palindromes.append(word)
        except():
            logging.error('Unexpected error at find_palin:', sys.exc_info()[0])
        return palindromes

    # Query e
    def uniqueWords(self):
        logging.info('Returning Unique Elements')
        return set(self.input_data)

    # Query f
    def dictWithKeys(self):
        logging.info('Enumeration in dictWithKeys')
        return dict(enumerate(self.input_data))

    # Query g-1
    def splitVovels(self):
        li = []
        try:
            logging.info('Spliting at Vovels')
            for i in range(len(self.input_data)):
                li.extend(re.split('[aeiouAEIOU]', self.input_data[i]))
            self.input_data = li
        except IndexError:
            logging.error('Index out of Bound Error at split Vovels')

    # Query g-2
    def captilizeThird(self):
        try:
            logging.info('Captilizing Third Letter')
            for i in range(len(self.input_data)):
                if len(self.input_data[i]) >= 3:
                    self.input_data[i].replace(self.input_data[i][2], self.input_data[i][2].upper(), 1)
        except IndexError:
            logging.error('Index out of Bound Error at captilizeThird')

    # Query g-3
    def captilizeFifth(self):
        try:
            logging.info('Captilizing Fifth Word')
            for i in range(len(self.input_data)):
                if (i+1) % 5 == 0:
                    self.input_data[i] = self.input_data[i].upper()
        except IndexError:
            logging.error('Index out of Bound Error at captilizeFifth')

    # Query g-5
    def replaceNewLine(self):
        try:
            logging.info('Replacing NewLine Character')
            for i in range(len(self.input_data)):
                self.input_data[i] = self.input_data[i].replace('\n', ';')
        except IndexError:
            logging.error('Index out of Bound Error at replaceNewLine')

    # Query g4&6
    def writeOutput(self):
        try:
            logging.info('Removing white spaces')
            self.input_data = ' '.join(self.input_data).split()
            logging.info('Creating unique file name')
            self.output_filename = str(uuid.uuid4()) + 'txt'
            logging.info('Calling write_data method')
            self.write_data()
        except():
            logging.error('Unexpected error at writeOutput:', sys.exc_info()[0])


if __name__ == '__main__':
    logging.basicConfig(filename='log_Query-3.txt',
                        filemode='a',
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info('Execution Started')
    obj = StrOp(sys.argv[1])
    obj.readfile()
    print('a. Number of words having prefix with "to" :', obj.prefix_To())
    print('b. Number of words ending with "ing" :', obj.postfix_ing())
    print('c. The word that was repeated maximum number of times is :', obj.maxRepeated())
    print('d. The Palindromes present in the file are :', ' '.join(obj.find_palin()))
    print('e. Unique Words: ', ' '.join(obj.uniqueWords()))
    print('f. Word dict with Key as counter index and value as the words :', obj.dictWithKeys())
    obj.splitVovels()
    obj.captilizeThird()
    obj.captilizeFifth()
    obj.replaceNewLine()
    obj.writeOutput()
    logging.info('Execution Completed')
