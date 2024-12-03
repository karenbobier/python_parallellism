from Bio import SeqIO
from concurrent.futures import ThreadPoolExecutor
from Bio.Seq import Seq


datas = []

def get_from(ntsequence):
    rnaseq = Seq.transcribe(ntsequence)
    datas.append(rnaseq)

ntsequences = [seq_record.seq for seq_record in SeqIO.parse("sequences.fasta", "fasta")]



with ThreadPoolExecutor() as ex:
    for ntsequence in ntsequences:
        ex.submit(get_from, ntsequence)

# look at the data
#print(datas)
