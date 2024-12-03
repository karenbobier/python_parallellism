from Bio import SeqIO
from Bio.Seq import Seq
from multiprocessing import Pool


ntsequences = [seq_record.seq for seq_record in SeqIO.parse("sequences.fasta", "fasta")]


def func(x):
    dnaseq = Seq(x)
    rnaseq = Seq.transcribe(dnaseq)
    return rnaseq


if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:
        pool.map(func, ntsequences)
