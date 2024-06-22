def solution(n):
    answer = 0
    binary_n=bin(n)
    next_number = n
    one_count = 0
    one_count = list(binary_n).count("1")
    
    while True:
        next_number +=1
        if list(bin(next_number)).count("1") ==  one_count:
            return next_number