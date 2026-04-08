import sys
input=sys.stdin.readline

def solve(towers:list)->None:
    stack=[(100000001, 0)]#무조건 0에서 걸리게 최대값보다 큰 0번째 타워 설정
    result=[]
    for tower in towers:
        while tower[0]>stack[-1][0]: #단조 감소 스택
            stack.pop()
        result.append(stack[-1][1])
        stack.append(tower)
    print(*result)
        



def main()->None:
    _=input()
    towers=[(val, i+1) for i, val in enumerate(map(int, input().split()))] #(높이, 몇번째 탑) 형태로 저장
    solve(towers)

main()