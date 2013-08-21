'''

Classes can inherit from other classes
and extend their functionality.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 11.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from chromosome import Chromosome

class CircularChromosome(Chromosome):
    '''Chromosome that has an origin.'''

    def __init__(self, bases, genes, origin):
        '''
        First calls the inherited __init__() of Chromosome,
        then creates the origin attribute.
        '''
        Chromosome.__init__(self, '1', 'circular', bases, genes)
        self.origin = origin

e_coli = CircularChromosome(4639221, 4228, 0)
print e_coli
