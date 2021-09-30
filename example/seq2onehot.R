source("R/seq2onehot.R")

pacman::p_load(tidyverse)

seq <- c("ABC", "ABB", "CCC")
onehot_array <- seq2onehot(seq)