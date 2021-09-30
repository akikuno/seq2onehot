source("R/onehot2seq.R")

pacman::p_load(tidyverse)

seq <- c("ABC", "ABB", "CCC")
onehot_array <- (array(mat_seq, dim = c(dim(mat_seq), length(levs))) == rep(levs, each = length(mat_seq))) * 1L

seq2 <- onehot2seq(onehot_array)

identical(seq, seq2)