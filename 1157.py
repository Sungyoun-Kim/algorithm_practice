import sys


def solution():
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    string = sys.stdin.readline()
    string = string.upper()
    count = [0 for i in range(26)]

    for i in string:
        number =ord(i)-65
        if 0 <= number < 26:
            number = ord(i) - 65
            count[number] += 1
    biggest = max(count)
    if count.count(biggest)>1:
        return "?"
    else:
        pos = count.index(biggest)
        return alphabet[pos]

if __name__ == "__main__":
    result = solution()
    print(result)






"""import sys

def solution():

    string = sys.stdin.readline()
    string = string.upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    count = [0 for i in range(len(alphabet))]

    for i in string:
        number = alphabet.find(i)
        lst = []
        for pos, char in enumerate(string):
            if char == i:
                lst.append(int(pos))
        count[number] = len(lst)
    biggest = max(count)

    if count.count(biggest) > 1:
        return "?"
    else:
        pos = count.index(biggest)
        return alphabet[pos]


if __name__ == "__main__":
    result=solution()
    print(result)
"""
"""
단어 공부
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	131282	51642	41232	39.084%
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A
출처
문제를 만든 사람: author5
데이터를 추가한 사람: jh05013
알고리즘 분류
구현
문자열"""