[![licence](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![PyPI version](https://img.shields.io/badge/Install%20with-PyPI-brightgreen.svg?style=flat-square)](https://pypi.org/project/seq2onehot/)
[![install with bioconda](https://img.shields.io/badge/Install%20with-Bioconda-brightgreen.svg?style=flat-square)](https://anaconda.org/bioconda/seq2onehot)

## Description

`seq2onehot` is a command-line tool encoding DNA/RNA/protein sequences to a one-hot numpy array.  
z
> :warning: All sequences must be the same lengths.

To decode a one-hot numpy array to sequences, use `onehot2seq`.  
https://github.com/akikuno/onehot2seq


## Installation

You can install `seq2onehot` using pip or bioconda:

```bash
pip install seq2onehot
```

```bash
conda install -c bioconda seq2onehot
```


## Usage

```bash
seq2onehot [options] -t/--type <dna/rna/protein> -i/--input <in.fasta> -o/--output <out.npy>
```

## Options

```bash
-a/--ambiguous: include ambiguous characters
```

The ambigous characters are:
- `XBZJ` for amino acid
- `NVHDBMRWSYK` for DNA and RNA

The detail of ambiguous characters is described here:  
https://meme-suite.org/meme/doc/alphabets.html


## Examples

```bash
# DNA sequences
seq2onehot -t dna -i example/dna.fasta -o dna.npy

# RNA sequences
seq2onehot -t rna -i example/rna.fasta -o rna.npy

# Protein sequences
seq2onehot -t protein -i example/protein.fasta -o protein.npy

```

## One-hot array

The output file contains 3d one-hot array of `RxNxL` (Read x Nucreotide/Amino acid x Letter)

- The order of nucreotide is `ACGT` (+ `NVHDBMRWSYK`) for DNA, `ACGU` (+ `NVHDBMRWSYK`) for RNA
- The order of amino acid is `ACDEFGHIKLMNPQRSTVWY` (+ `XBZJ`)

```python
# Original sequences:
## ACGTACGTACGTACGT
## CCCCCCCCTTTTTTTT

onehot = np.load("dna.npy")

onehot.shape
# (2, 16, 4) <- 2 reads x 16 nucreotides x 4 letters (ACGT)

onehot
# array([[[1., 0., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 0., 1., 0.],
#         [0., 0., 0., 1.],
#         [1., 0., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 0., 1., 0.],
#         [0., 0., 0., 1.],
#         [1., 0., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 0., 1., 0.],
#         [0., 0., 0., 1.],
#         [1., 0., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 0., 1., 0.],
#         [0., 0., 0., 1.]],

#        [[0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.],
#         [0., 0., 0., 1.]]])
```

