def solution(elements):
    answer = 0
    ele_len = len(elements)
    sum_set = set()
    elements = elements + elements

    i =0
    while i <ele_len:
        for j in range(i+1,i+1+ele_len):
            sum_set.add(sum(elements[i:j]))
        i+=1
        
    return len(sum_set)