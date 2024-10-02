from concurrent.futures import ThreadPoolExecutor
from Bio.Seq import Seq


datas = []

def get_from(ntsequence):
    dnaseq = Seq(ntsequence)
    rnaseq = Seq.transcribe(dnaseq)
    datas.append(rnaseq)

ntsequences = [
    "TAGATTCGCCG",
    "ATCCGCTACGA",
    "CCGATCTACGG",
    "GATCATCGAGA",
]


with ThreadPoolExecutor() as ex:
    for ntsequence in ntsequences:
        ex.submit(get_from, ntsequence)

# look at the data
print(datas)
