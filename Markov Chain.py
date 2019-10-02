import re
import numpy
import pandas


config = open("config.txt", "r")
probs_file_path = config.readline().split()[1]
first_page = config.readline().split()[1]
final_pages = [page for page in config.readline().split()[1:]]


class ExceptionHandler(Exception):
    pass


''' The Markov Chain is a class initialized with two matrixes obtained parsing a file and getting a dataframe from it.
    The first matrix, 'transition_matrix', is a two-dimensional matrix representing the probability of a transition.
    The second second, 'pages', is a one-dimensional matrix representing the states (i.e. the pages of a book).   
    
    It's important the ordering of pages.
    
    The class also contains two attributes:
        'book_index' is a dictionary linking a page to an index.
        'book_pages' is the other way around.        
'''


class MarkovChain(object):
    def __init__(self, config_path):
        self.dataframe = pandas.read_csv(config_path, header=0, delim_whitespace=True)
        self.transition_matrix = numpy.atleast_2d(self.dataframe.as_matrix())
        self.pages = [col for col in self.dataframe.columns]
        self.book_index = {self.pages[index]: index for index in range(len(self.pages))}
        self.book_pages = {index: self.pages[index] for index in range(len(self.pages))}
        self.final_pages = []
        if first_page in self.pages:
            self.current = first_page
        else:
            raise ExceptionHandler("First page not present in probabilities file!")
        for page in final_pages:
            if page in self.pages:
                self.final_pages.append(page)
            else:
                raise ExceptionHandler("Final page not present in probabilities file!")

    ''' 
        The method 'next' returns a possible choice as the next state (page of the book) of the current state (curr).
        If the current page is a final page, it returns nothing.
    '''
    def next(self):
        return numpy.random.choice(
            self.pages,
            p=self.transition_matrix[self.book_index[self.current], :]
        ) if self.current not in self.final_pages else print("The End.")


# An example:
ex = MarkovChain(probs_file_path)
print(ex.next())
