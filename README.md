[![licence](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
<!-- [![PyPI version](https://img.shields.io/badge/Install%20with-PyPI-brightgreen.svg?style=flat-square)](https://pypi.org/project/calcs/) -->
<!-- [![install with bioconda](https://img.shields.io/badge/Install%20with-Bioconda-brightgreen.svg?style=flat-square)](https://anaconda.org/bioconda/calcs) -->

## Description

`seq2onehot` is a command-line tool encoding a DNA/RNA/protein sequence to a one-hot numpy array.  

> :warning: All sequences must be the same lengths.

To decode a one-hot numpy array to sequences, use `onehot2seq`.  
https://github.com/akikuno/onehot2seq


## Installation

You can install `seq2onehot` using pip:

```bash
pip install seq2onehot
```
<!-- 
Alternatively, you can get `seq2onehot` from bioconda:

```
conda install -c bioconda seq2onehot
``` -->

## Usage

```bash
seq2onehot [options] -t/--type <dna/rna/protein> -i/--input <in.fasta> -o/--output <out.npy>
```

## Options

```bash
-a/--ambiguous: include ambiguous characters
```

The detail of ambiguous characters is descrived here:  
https://meme-suite.org/meme/doc/alphabets.html

## Examples

```bash
# DNA sequences
seq2onehot -t dna -i examples/dna.fasta -o dna.npy

# RNA sequences
seq2onehot -t rna -i examples/rna.fasta -o rna.npy

# Protein sequences
seq2onehot -t protein -i examples/protein.fasta -o protein.npy

# Protein sequences including ambiguous characters
seq2onehot -t protein -a -i examples/protein_ambiguous.fasta -o protein_ambiguous.npy

```

