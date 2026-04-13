import sys
input=sys.stdin.readline

def solve(word:str)->int:
    slices=0 #조각의 수
    sticks=0 #겹쳐져있는 막대기의 수
    stack=[] #괄호 확인용 스택
    isLaser=True #'(' 이 레이저의 여는괄호인지 막대기의 여는괄호인지 구분하는 flag

    for alpha in word: #문제 상황상 word는 Valid Parenthesis String(vps) 이다.
        if alpha=='(':
             #vps에서 스택은 비어있거나 '(' n개로 채워져있거나 둘 중에 하나다.
            sticks+=1 
            slices+=1 
            stack.append(alpha)
            isLaser=True
        else:
            if isLaser: #')'가 레이저의 닫는괄호라면
                sticks-=1
                slices-=1 #직전의 여는괄호가 막대기가 아니라 레이저였으므로 rollback
                slices+=sticks #현재 겹쳐져있는 막대기만큼 조각이 늘어나고
                stack.pop() #레이저의 여는괄호를 pop
                isLaser=False #이 다음에 ')'이 나오면 막대기의 닫는괄호라는 것을 표시
            else:
                sticks-=1 

    return slices


def main()->None:
    print(solve(input().rstrip()))


main()