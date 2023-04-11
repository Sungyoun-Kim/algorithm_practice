import sys

if __name__ =="__main__":
    equation = sys.stdin.readline().rstrip().split('-')
    sum = 0
    for i in equation[0].split('+'):
        sum += int(i)
    for i in equation[1:]:
        for j in i.split('+'):
            sum -= int(j)
    print(sum)