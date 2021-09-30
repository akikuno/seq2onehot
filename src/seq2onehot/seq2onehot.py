import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",
                    metavar="<in.fasta>",
                    help="FASTA or Sequence file",
                    required=True)
parser.add_argument("-o", "--output",
                    metavar="<out.npy>",
                    help="Numpy .npy format",
                    required=True)
parser.add_argument("-t", "--type",
                    metavar="<dna/rna/protein>",
                    choices=['dna', 'rna', 'protein'],
                    help="Sequence type (DNA/RNA/Protein)",
                    required=True)
parser.add_argument("-a", "--ambiguous",
                    help="Accept ambiguous characters",
                    action="store_true",)
args = parser.parse_args()


def define_alphabet(seqtype, ambiguous):
    if seqtype == "dna":
        alphabet = "ACGT"
        if ambiguous:
            alphabet += "NVHDBMRWSYK"
    elif seqtype == "rna":
        alphabet = "ACGU"
        if ambiguous:
            alphabet += "NVHDBMRWSYK"
    elif seqtype == "protein":
        alphabet = "ACDEFGHIKLMNPQRSTVWY"
        if ambiguous:
            alphabet += "XBZJ"
    return alphabet


def seq2onehot(seq):
    alphabet = define_alphabet(args.type, args.ambiguous)
    onehot = np.zeros([len(seq), len(seq[0]), len(alphabet)])

    for i, s in enumerate(seq):
        s_series = pd.Series(list(alphabet + s))
        alphabet_categorical = pd.factorize(s_series)[0]
        alphabet_categorical = np.expand_dims(alphabet_categorical, 0)
        oh = np.eye(len(alphabet), dtype=np.uint8)[alphabet_categorical]
        oh = oh[:, len(alphabet):]
        onehot[i] = oh
    return onehot


if __name__ == "__main__":
    with open(args.input, "r") as f:
        seq = [s.strip() for s in f]
    seq = [s for s in seq if ">" not in s]
    onehot = seq2onehot(seq)
    np.save(args.output, onehot)

