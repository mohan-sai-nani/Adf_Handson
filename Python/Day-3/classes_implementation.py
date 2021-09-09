"""Import Statements"""
from collections import Counter
import sys
import re
import uuid
import logging


class Io:
    """this class takes care of read and write operations"""
    def __init__(self, filename):
        """this method initialized variables from the class IO"""
        self.filename = filename
        self.input_data = []
        self.output_filename = ''

    def read_file(self):
        """this method reads file from the passed argument and extracts words into input_data"""
        try:
            logging.info('Trying to read Input File')
            with open(self.filename, 'r+', encoding='utf-8') as sample:
                data = sample.readlines()
        except OSError:
            logging.error('Unexpected error: %s', sys.exc_info()[0])
        logging.info('spliting words')
        for line in data:
            words = line.split()
            self.input_data.extend(words)
            self.input_data.extend('\n')
        logging.info('Split complete')

    def write_data(self):
        """This method writes data to output File"""
        try:
            logging.info('Opening file to write')
            with open(self.output_filename, "x", encoding='utf-8') as output_file:
                logging.info('Writting data to File')
                output_file.write("-".join(self.input_data))
        except OSError:
            logging.error('Unexpected error: %s', sys.exc_info()[0])


class StrOp(Io):
    """This class is inhereted from IO class and performes String Operations"""
    def prefix_to(self):
        """This method counts the words starting with 'to'"""
        count = 0
        try:
            logging.info("Searching for prefix 'to'")
            for word in self.input_data:
                if word.lower().startswith('to'):
                    count += 1
        except():
            logging.error('Unexpected error: %s', sys.exc_info()[0])
        return count

    def postfix_ing(self):
        """This method counts the words ending with 'ing'"""
        count = 0
        try:
            logging.info("Searching for ending 'ing'")
            for word in self.input_data:
                if word.lower().endswith('ing'):
                    count += 1
        except():
            logging.error('Unexpected error: %s', sys.exc_info()[0])
        return count

    def max_repeated(self):
        """This method returns the most repeated word"""
        try:
            logging.info('Searching for max repeated element')
            temp = Counter(self.input_data)
        except():
            logging.error('Unexpected error: %s', sys.exc_info()[0])
        return temp.most_common(1)[0][0]

    def find_palin(self):
        """This method finds and returns palindromic words in form of List"""
        palindromes = []
        try:
            logging.info("Searching for palindromes")
            for word in self.input_data:
                if word == word[::-1] and len(word) > 1:
                    palindromes.append(word)
        except():
            logging.error('Unexpected error at find_palin: %s', sys.exc_info()[0])
        return palindromes

    def unique_words(self):
        """This method returns set of Unique Elements"""
        logging.info('Returning Unique Elements')
        return set(self.input_data)

    def dict_with_keys(self):
        """This method performs Enumeration in Dict"""
        logging.info('Enumeration in dictWithKeys')
        return dict(enumerate(self.input_data))

    def split_vovels(self):
        """This method splits words based on vovels"""
        temp_list = []
        try:
            logging.info('Spliting at Vovels')
            data_len = len(self.input_data)
            for i in range(data_len):
                temp_list.extend(re.split('[aeiouAEIOU]', self.input_data[i]))
            self.input_data = temp_list
        except IndexError:
            logging.error('Index out of Bound Error at split Vovels')

    def captilize_third(self):
        """This method captilizes third letter of every word"""
        try:
            logging.info('Captilizing Third Letter')
            data_len = len(self.input_data)
            for i in range(data_len):
                if len(self.input_data[i]) >= 3:
                    self.input_data[i].replace(self.input_data[i][2]
                                               , self.input_data[i][2].upper()
                                               , 1
                                               )
        except IndexError:
            logging.error('Index out of Bound Error at captilizeThird')

    def captilize_fifth(self):
        """This method captilizes every fifth word"""
        try:
            logging.info('Captilizing Fifth Word')
            data_len = len(self.input_data)
            for i in range(data_len):
                if (i+1) % 5 == 0:
                    self.input_data[i] = self.input_data[i].upper()
        except IndexError:
            logging.error('Index out of Bound Error at captilizeFifth')

    def replace_new_line(self):
        """This method replaces new line character with ';'"""
        try:
            logging.info('Replacing NewLine Character')
            data_len = len(self.input_data)
            for i in range(data_len):
                self.input_data[i] = self.input_data[i].replace('\n', ';')
        except IndexError:
            logging.error('Index out of Bound Error at replaceNewLine')

    def write_output(self):
        """This Query removes blankspaces and passes the list for writing to output file"""
        try:
            logging.info('Removing white spaces')
            self.input_data = ' '.join(self.input_data).split()
            logging.info('Creating unique file name')
            self.output_filename = str(uuid.uuid4()) + 'txt'
            logging.info('Calling write_data method')
            self.write_data()
        except():
            logging.error('Unexpected error at writeOutput: %s', sys.exc_info()[0])


if __name__ == '__main__':
    logging.basicConfig(filename='log_Query-3.log',
                        filemode='a',
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info('Execution Started')
    obj = StrOp(sys.argv[1])
    obj.read_file()
    print('a. Number of words having prefix with "to" :', obj.prefix_to())
    print('b. Number of words ending with "ing" :', obj.postfix_ing())
    print('c. The word that was repeated maximum number of times is :', obj.max_repeated())
    print('d. The Palindromes present in the file are :', ' '.join(obj.find_palin()))
    print('e. Unique Words: ', ' '.join(obj.unique_words()))
    print('f. Word dict with Key as counter index and value as the words :', obj.dict_with_keys())
    obj.split_vovels()
    obj.captilize_third()
    obj.captilize_fifth()
    obj.replace_new_line()
    obj.write_output()
    logging.info('Execution Completed')
