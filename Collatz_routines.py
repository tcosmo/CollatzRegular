"""
author: Tristan Sterin

This file contains routines to deal with Collatz related objects.

These routines are used for the construction of Algorithm 1 and 2 of the paper
"First Occurrence of Parity Vectors and The Regular Structure of k-span Predecessor Sets in the Collatz graph"
"""

## The Collatz map
def T(x):
    return T1(x) if x%2 else T0(x)

def T0(x):
    return x//2

def T1(x):
    return (3*x+1)//2

## Collatz sequence
def CS(x):
    cs = [x]
    while cs[-1] != 1:
        cs.append(T(cs[-1]))
    return cs

## Modular arithmetic versions of T0/T1 (cf Definition 3.18)
def inv2(k):
    return (3**k + 1)//2

def T0_k(x, k):
    return (inv2(k)*x)%(3**k)

def T1_k(x, k):
    return (inv2(k)*(3*x+1))%(3**k)

## Base conversion routines
def int_to_binary(x):
    return bin(x)[2:]

def binary_to_int(x):
    return int(x,2)