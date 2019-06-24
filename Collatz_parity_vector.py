"""
author: Tristan Sterin

This file contains routines to deal with parity vectors and occurrences
of parity vectors in the Collatz graph.

The function ``get_first_occurrence'' implements Algorithm 1 of the paper
"First Occurrence of Parity Vectors and The Regular Structure of k-span Predecessor Sets in the Collatz graph"
"""

import random
import numpy as np

import itertools

from Collatz_routines import *

BOTTOM_ARROW = 0
LEFT_ARROW   = 1

def get_random_parvec(parvec_norm=None, parvec_span=None, max_norm=30):
    """ Returns a parity vector as a list of moves where 0 is `bottom` and 1 is `left`. 
    
        parvec_norm: size of the parvec
        parvec_span: number of LEFT_ARROW in the parvec
        max_norm: maximal norm of the parvec if parvec_norm is None
    """
    if parvec_norm is None:
        parvec_norm = random.randint(0,max_norm)
        if parvec_span != None:

            if parvec_span > max_norm:
                print("parvec length {} too big for max_norm {}".format(parvec_span,max_norm))
                return

            parvec_norm = random.randint(parvec_span,max_norm)
    
    if parvec_span is None:
        parvec = list(np.random.choice([BOTTOM_ARROW,LEFT_ARROW],parvec_norm))
    else:
        parvec = np.zeros(parvec_norm,dtype=np.int) + BOTTOM_ARROW
        indices_of_left = np.random.choice(range(parvec_norm),parvec_span,replace=False)
        parvec[indices_of_left] = LEFT_ARROW
        parvec = list(parvec)

    return parvec

def get_parvec_with_constraints(parvec_norm, parvec_span=None):
    """ Get all the parity vectors with a given norm constraint and potentially a span constraint.
    """
    for p in itertools.product([0,1], repeat=parvec_norm):
        if parvec_span is None or sum(p) == parvec_span:
            yield list(p)

def norm_of(parvec):
    return len(parvec)

def l_of(parvec):
    return sum(parvec)

def T_modular(arrow, k, x):
    if arrow == BOTTOM_ARROW:
        return T0_k(x,k)
    return T1_k(x,k)

def is_admissible(arrow, x):
    return arrow == x%2

def get_first_occurrence(p):
    alpha0 = 0
    alpha_minus_1 = 0
    k = 0

    for i, arrow in enumerate(p):
        if not is_admissible(arrow, alpha_minus_1):
            alpha0 += 2**(i)

        if arrow == LEFT_ARROW:
            k += 1

        alpha_minus_1 = T_modular(arrow, k, alpha_minus_1)

    first_occurrence = [alpha0]
    for i in range(len(p)):
        first_occurrence.append(T(first_occurrence[-1]))

    return first_occurrence

def get_occurrence(p, i=0):
    occ = get_first_occurrence(p)

    if i == 0:
        return occ0

    ith_occurrence = [(2**(norm_of(p)))*i + occ[0]]
    for i in range(len(p)):
        ith_occurrence.append(T(ith_occurrence[-1]))

    return ith_occurrence

def get_Collatz_encoding(p):
    """ Returns the Collatz encoding of the parity vector p. I.e, alpha00(p) on ||p|| bits
    """
    occ = get_first_occurrence(p)
    s = int_to_binary(occ[0])
    return "0"*(len(p)-len(s))+s