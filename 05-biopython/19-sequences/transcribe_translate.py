'''

Transcribe & translate a DNA sequence.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 19.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Seq	
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# read the input sequence
records = SeqIO.parse("haemoglobin-gene.fasta", "fasta")
gene = list(records)[0]
cdna = gene.seq

# transcribe and translate
mrna = cdna.transcribe()
protein = mrna.translate()

# write the protein sequence to a file
protein_record = SeqRecord(protein, id='sp|P69905.2|HBA_HUMAN',
                     description="Hemoglobin subunit alpha, Homo sapiens")

outfile = open("HBA_HUMAN.fasta", "w")
SeqIO.write(protein_record, outfile,"fasta")
outfile.close()
