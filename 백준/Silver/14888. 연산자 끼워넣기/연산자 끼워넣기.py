import sys

def main():
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    add, sub, mul, div = map(int, sys.stdin.readline().split())
    
    min_val = float('inf')
    max_val = -float('inf')
    
    def backtrack(result, idx, add, sub, mul, div):
        nonlocal min_val, max_val
        if idx == N:
            min_val = min(min_val, result)
            max_val = max(max_val, result)
            return
        
        if add > 0:
            backtrack(result + numbers[idx], idx + 1, add - 1, sub, mul, div)
        if sub > 0:
            backtrack(result - numbers[idx], idx + 1, add, sub - 1, mul, div)
        if mul > 0:
            backtrack(result * numbers[idx], idx + 1, add, sub, mul - 1, div)
        if div > 0:
            if result < 0:
                backtrack(-(abs(result) // numbers[idx]), idx + 1, add, sub, mul, div - 1)
            else:
                backtrack(result // numbers[idx], idx + 1, add, sub, mul, div - 1)
    
    backtrack(numbers[0], 1, add, sub, mul, div)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main()