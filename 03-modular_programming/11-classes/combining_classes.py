'''

Create a class that uses another class.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 11.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from chromosome import chromosomes

class Genome:
    '''A Genome contains one to many chromosomes.'''
    def __init__(self, chromosomes):
        '''Sets a list of chromosomes.'''
        self.chromosomes = chromosomes
    
    def __repr__(self):
        return 'genome with %i chromosomes' % (len(self.chromosomes))


human_genome = Genome(chromosomes)
print human_genome
