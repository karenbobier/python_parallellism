from Bio.Seq import Seq
from multiprocessing import Pool


ntsequences = [
    "TAGATTCGCCG",
    "ATCCGCTACGA",
    "CCGATCTACGG",
    "GATCATCGAGA",
]


def func(x):
    dnaseq = Seq(x)
    rnaseq = Seq.transcribe(dnaseq)
    return rnaseq


if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:
        print(pool.map(func, ntsequences))
