import numpy
import pandas


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

    ''' The method returns a possible choice as the next state (page of the book) of the current state (curr).'''

    def next(self, curr):
        return numpy.random.choice(
            self.pages,
            p=self.transition_matrix[self.book_index[curr], :]
        )


# An example:
ex = MarkovChain("probabilities.txt")
