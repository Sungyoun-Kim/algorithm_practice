import sys
def push(n):
    Queue.append(n)
def pop():
    if len(Queue) == 0:
        print(-1)
        return
    print(Queue[0])
    del Queue[0]
def size():
    print(len(Queue))
def empty():
    if len(Queue) ==0:
        print(1)
    else:
        print(0)
def front():
    if len(Queue) == 0:
        print(-1)
        return
    print(Queue[0])
def back():
    if len(Queue) == 0:
        print(-1)
        return
    print(Queue[-1])



if __name__ =="__main__":
    N = int(sys.stdin.readline())
    Queue = []
    for i in range(N):
        order = sys.stdin.readline().split()
        if order[0] == "push":
            push(order[1])
        elif order[0] =="pop":
            pop()
        elif order[0] =="front":
            front()
        elif order[0] =="back":
            back()
        elif order[0] =="size":
            size()
        elif order[0] =="empty":
            empty()
