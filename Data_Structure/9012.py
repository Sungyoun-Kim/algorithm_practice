import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    string = []
    for i in range(T):
        String = sys.stdin.readline()
        string.append(String)

    for i in string:
        sum = 0
        for j in range(len(i)):
            if i[j] == "(":
                sum += 1
            if i[j] == ")":
                sum -= 1
            if sum <0:
                break
        if sum == 0:
            print("YES")
        elif sum >0:
            print("NO")
        else:
            print("NO")
