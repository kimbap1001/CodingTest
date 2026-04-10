import sys
input=sys.stdin.readline

def solve(nums:list)->None:
    stack=[1000001]
    result=[]
    for num in nums:
        while num>=stack[-1]:
            stack.pop()
        if stack[-1]==1000001:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(num)
    print(*list(reversed(result)))

def main()->None:
    _=input()
    nums=list(map(int, input().split()))
    solve(list(reversed(nums)))


main()