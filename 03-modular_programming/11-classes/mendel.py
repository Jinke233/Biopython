'''

Simulate Mendelian inheritance of pea strains.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 11.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

class Pea:

    def __init__(self, genotype):
        self.genotype = genotype

    def get_phenotype(self):
        if "G" in self.genotype:
            return "yellow"
        else:
            return "green"

    def create_offspring(self, other):
        offspring = []
        new_genotype = ""
        for haplo1 in self.genotype:
            for haplo2 in other.genotype:
                new_genotype = haplo1 + haplo2
                offspring.append(Pea(new_genotype))
        return offspring

    def __repr__(self):
        return self.get_phenotype() + ' [%s]' % self.genotype


yellow = Pea("GG")
green = Pea("gg")
f1 = yellow.create_offspring(green)
f2 = f1[0].create_offspring(f1[1])
print f1
print f2
