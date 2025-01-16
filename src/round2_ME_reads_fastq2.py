import sys
import csv
from Bio import SeqIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
import gzip

csv.field_size_limit(100000000)

def main(alingment_pre_processed_round2, row_fastq):
	
    ME_reads = set([])
    fastq_out = open( alingment_pre_processed_round2 + ".fastq", 'w')

    for row in csv.reader(open(alingment_pre_processed_round2), delimiter = '\t'):

	#print row, len(row)

        if len(row)>=7:
	    read, flag, tag, start, cigar, seq, qual = row[:7]
            ME_reads.add(read)

    with gzip.open(row_fastq) as f:

        for read in SeqIO.parse(f, "fastq"):

            if read.id in ME_reads:
                
                f_out = SeqRecord( read.seq, read.id, description = "" )
                f_out.letter_annotations["phred_quality"] = read.letter_annotations["phred_quality"]

                fastq_out.write(f_out.format("fastq"))

#		try:
#			read, flag, tag, start, cigar, seq, qual = row
#c
#			if len(seq)>len(qual):
#				qual = qual + qual[ -(len(seq) - len(qual)) : ]
#
#			elif len(seq)<len(qual):
#				qual = qual[:len(seq)]
#
#			print "@" + read
#			print seq
#			print "+"
#			print qual
#
#		except ValueError: #minor fraction of lines dont have 7 columns due to errors.
#			pass


if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
