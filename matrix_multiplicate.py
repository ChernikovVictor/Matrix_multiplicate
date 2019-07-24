#!/usr/bin/python
import numpy as np
import sys
import os


def multiplicate(a, b):
    n = a.shape[0] // 2
    if (n > 16):
        A11 = a[:n, :n]
        A12 = a[:n, n:]
        A21 = a[n:, :n]
        A22 = a[n:, n:]
        B11 = b[:n, :n]
        B12 = b[:n, n:]
        B21 = b[n:, :n]
        B22 = b[n:, n:]
        P1 = multiplicate(A11 + A22, B11 + B22)
        P2 = multiplicate(A21 + A22, B11)
        P3 = multiplicate(A11, B12 - B22)
        P4 = multiplicate(A22, B21 - B11)
        P5 = multiplicate(A11 + A12, B22)
        P6 = multiplicate(A21 - A11, B11 + B12)
        P7 = multiplicate(A12 - A22, B21 + B22)
        C = np.array((n*2, n*2), dtype = type(a[0][0]))
        C[:n, :n] = P1 + P4 - P5 + P7
        C[:n, n:] = P3 + P5
        C[n:, :n] = P2 + P4
        C[n:, n:] = P1 - P2 + P3 + P6
        return C
    else:
        return np.dot(a, b)

n = int(input())
k = 1
while (k < n):
    k *= 2
d = np.loadtxt(sys.stdin)
a = np.zeros((k, k), dtype = int)
b = np.zeros((k, k), dtype = int)
a[:n, :n] = d[:n, :n]
b[:n, :n] = d[n:, :n]
c = multiplicate(a, b)
for i in range(n):
    print(' '.join(map(str, c[i, :n])))

