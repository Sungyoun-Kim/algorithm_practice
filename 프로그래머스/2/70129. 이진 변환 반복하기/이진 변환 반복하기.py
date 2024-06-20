def binary_converter(binary_string):
    removed_zero = 0
    new_binary_list = []
    for i in binary_string:
        if i == '0':
            removed_zero +=1
            continue
        new_binary_list.append(i)
    
    return f"{len(new_binary_list):b}",removed_zero



def solution(s):
    removed_zero = 0
    try_count =0
    while True:
        if s!="1":
            try_count+=1
            s, b=binary_converter(s)
            removed_zero +=b
            
            continue
        break


    return try_count,removed_zero
    