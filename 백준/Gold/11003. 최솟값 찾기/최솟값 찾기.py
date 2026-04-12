import sys
input=sys.stdin.readline
from collections import deque

def solve(nums:list, l=int)->None:
    md=deque([]) # 최솟값 계산을 위한 monotonic increase deque
    result=[] #결과 담을 리스트
    md_log=[] #최솟값이 변하는 지점들을 로그에 저장 후 result에 한번에 write

    md.append((0,nums[0]))
    md_log.append((0, nums[0]))

    for i, num in enumerate(nums[1:], start=1):
        prevMin=md[0] #최솟값 변화여부 확인을 위해 이전단계에서의 최솟값 저장
        
        while md and num <= md[-1][1]: #서로 같은 수도 존재할 수 있으므로 등호 포함
            md.pop() #monotonic increase 상태 유지를 위한 작업

        while md and (i - md[0][0]) >= l:
            md.popleft() #현재 위치에서 D의 영향권 밖의 최솟값을 없애는 작업 
            #ex) i=5인데 md[0] 이 i=0 인 원소면 없애야함
        
        md.append((i, num))

        if prevMin != md[0]: 
            md_log.append((i,md[0][1])) #최솟값 변화를 변화시점과 함께 로그에 기록

    md_log.append((len(nums), 0))
    for i in range(len(md_log)-1):
        result+=[md_log[i][1]] * (md_log[i+1][0] - md_log[i][0])


    print(*result)

def main()->None:
    _, l=map(int, input().split())
    nums=list(map(int, input().split()))
    solve(nums, l)

main()

