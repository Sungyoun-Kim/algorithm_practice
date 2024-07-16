def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]


def solution(arr1,arr2):
    return productMatrix(arr1,arr2)