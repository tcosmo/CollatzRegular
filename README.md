# CollatzRegular
Code associated to the paper "First Occurrence of Parity Vectors and the Regular Structure of k-Span Predecessor Sets in the Collatz Graph", [arxiv:1907.00775](https://arxiv.org/abs/1907.00775).

This code is also associated to an improved version of that paper called "Collatz Predecessor Sets Partition into Regular Languages". In this version, only one algorithm is shown which is the one which derives regular expressions (Algorithm 2 in the arxiv version). 

# Structure of this Repo

The notebook "FirstOccurrence" illustrates Algorithm 1 (the construction of the first occurrence of a parity vector in the Collatz graph).

The notebook "RegularExpressions" illustrates the construction of Theorem 4.16 with Algorithm 2 (Appendix E). It also performs some automatic testing on the produced regular expressions by using the package `redone`: https://github.com/cyphar/redone/.

The three python files are:
- `Collatz_routines.py`: various routines to deal with the Collatz process
- `Collatz_parity_vector.py`: routines to deal with parity vectors and the code of Algorithm 1 (`get_first_occurrence`)
- `Collatz_reg.py`: routines and main code of Algorithm 2 (`get_reg_k`)
