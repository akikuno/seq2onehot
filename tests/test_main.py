from src.seq2onehot.main import load_fasta
from src.seq2onehot.main import seq2onehot
import dataclasses
import numpy as np


@dataclasses.dataclass
class Args:
    input: str
    output: str
    type: str
    ambiguous: bool


args = Args("input", "output", "type", True)


def test_dna_fasta():
    data_eval = np.load("tests/dna.npy")
    args.input = "example/dna.fasta"
    args.type = "dna"
    args.ambiguous = False
    seq = load_fasta(args.input)
    onehot = seq2onehot(seq, args.type, args.ambiguous)
    np.equal(onehot, data_eval)


def test_dna_txt():
    data_eval = np.load("tests/dna.npy")
    args.input = "example/dna.txt"
    args.type = "dna"
    args.ambiguous = False
    seq = load_fasta(args.input)
    onehot = seq2onehot(seq, args.type, args.ambiguous)
    np.equal(onehot, data_eval)


def test_protein_fasta():
    data_eval = np.load("tests/protein.npy")
    args.input = "example/protein.fasta"
    args.type = "protein"
    args.ambiguous = False
    seq = load_fasta(args.input)
    onehot = seq2onehot(seq, args.type, args.ambiguous)
    np.equal(onehot, data_eval)


def test_protein_txt():
    data_eval = np.load("tests/protein.npy")
    args.input = "example/protein.txt"
    args.type = "protein"
    args.ambiguous = False
    seq = load_fasta(args.input)
    onehot = seq2onehot(seq, args.type, args.ambiguous)
    np.equal(onehot, data_eval)


def test_rna_fasta():
    data_eval = np.load("tests/rna.npy")
    args.input = "example/rna.fasta"
    args.type = "rna"
    args.ambiguous = False
    seq = load_fasta(args.input)
    onehot = seq2onehot(seq, args.type, args.ambiguous)
    np.equal(onehot, data_eval)


def test_rna_txt():
    data_eval = np.load("tests/rna.npy")
    args.input = "example/rna.txt"
    args.type = "rna"
    args.ambiguous = False
    seq = load_fasta(args.input)
    onehot = seq2onehot(seq, args.type, args.ambiguous)
    np.equal(onehot, data_eval)
