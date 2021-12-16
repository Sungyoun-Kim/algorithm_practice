import sys

def solution():
    dial = sys.stdin.readline().strip()
    result=0;

    for i in dial:
        result+=change(i)

    return result



def change(char):
    char=ord(char)
    if 65<=char<=67:
        return 3
    elif 68<=char<=70:
        return 4
    elif 71<=char<=73:
        return 5
    elif 74<=char<=76:
        return 6
    elif 77<=char<=79:
        return 7
    elif 80<=char<=83:
        return 8
    elif 84<=char<=86:
        return 9
    elif 87<=char<=90:
        return 10
    else:
        return 2

if __name__ == "__main__":
    print(solution())



"""다이얼 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	62112	35566	31473	57.442%
문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.



전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

출력
첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

예제 입력 1 
WA
예제 출력 1 
13
예제 입력 2 
UNUCIC
예제 출력 2 
36
출처
Contest > Croatian Open Competition in Informatics > COCI 2012/2013 > Contest #6 1번

문제를 번역한 사람: baekjoon
잘못된 번역을 찾은 사람: jung2381187
문제의 오타를 찾은 사람: pskalyber
알고리즘 분류
구현"""
