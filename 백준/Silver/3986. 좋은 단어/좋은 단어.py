import sys
input=sys.stdin.readline

def solve(words:list)->int:
    result=0
    for word in words:
        stack=[]
        for alpha in word:
            if stack and stack[-1]==alpha:
                stack.pop()
            else:
                stack.append(alpha)
        if not stack:
            result+=1

    return result


def main()->None:
    n=int(input())
    words=[input().rstrip() for _ in range(n)]
    print(solve(words))


main()