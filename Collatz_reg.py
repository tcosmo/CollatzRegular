"""
author: Tristan Sterin

This file contains the construction of the main result (Theorem 4.16) of the paper
"First Occurrence of Parity Vectors and The Regular Structure of k-span Predecessor Sets in the Collatz graph"

The function ``get_reg_k(x, k)'' returns the regular expression which decides the k-span predecessor set of x.
"""

from Collatz_routines import *
#from Collatz_parity_vector import *

def get_Pi_k(k):
    """ Returns the parity sequence Pi_k (cf Definition 4.9)
    """
    inv = inv2(k)
    Pik = ""
    for i in range(get_pi_k(k)):
        nb = (inv**i)%(3**k)
        Pik += str(nb%2)
    return Pik[::-1]

def get_pi_k(k):
    """ Returns the length of Pi_k
    """
    if k == 0:
        return 1
    return 2*(3**(k-1))

def log_2k(x,k):
    """ Returns i such that x = 2^{-i} in Z/3^kZ
    Returns None if x is a multiple of three. 
    """
    inv = inv2(k)
    for i in range(get_pi_k(k)):
        nb = (inv**i)%(3**k)
        if nb == x:
            return i

def join_k(x,y,k):
    """ Returns the string join_{i_2} of the construction of Theorem 4.16
    """
    if (x%3)*(y%3) == 0:
        return ""
    if not (x < 3**k and y < 3**k):
        return None
    
    s = ""
    i0 = log_2k(x,k)
    inv = inv2(k)
    
    for i in range(i0,i0+get_pi_k(k)):
        nb = (inv**i)%(3**k)
        if nb == y:
            return s[::-1]
        s += str(nb%2)

def rotation(s,i):
    """ Right rotation operator on strings
    """
    n = len(s)
    return "".join([ s[(n-(i-l))%n] for l in range(n) ])

def get_reg_k(x,k):
    if k == 0:
        return "(0)*" if x == 0 else "({})(0)*".format(int_to_binary(x))
    if x%3 == 0:
        return ""
    if x >= 3**k:
        return "({})({})".format(int_to_binary(x//(3**k)),get_reg_k(x%(3**k),k))
    
    i = log_2k(x,k)
    Pik = get_Pi_k(k)
    
    reg = "({})*(".format(rotation(Pik,i))
    
    inv = 0 if k-1 == 0 else inv2(k-1)
    
    for j in range(get_pi_k(k-1)):
        curr = 0 if k-1 == 0 else (inv**j)%(3**(k-1))
        reg += "(({})({})({}))".format(join_k(T1_k(curr,k),x,k), 1-(curr%2),get_reg_k(curr,k-1))
        if j < get_pi_k(k-1)-1:
            reg += "|"
    
    reg += ")"
    
    return reg