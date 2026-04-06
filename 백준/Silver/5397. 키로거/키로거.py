import sys
input=sys.stdin.readline

def solve(psw:str)->None:
    result_front=[] ##커서 앞
    result_back=[]  ##커서 뒤
    for each in psw:
        if each=='<' :
            if len(result_front) != 0:
                result_back.append(result_front.pop()) ##커서 앞에서 pop해서 커서 뒤에 push
        elif each=='>' : 
            if len(result_back) != 0:
                result_front.append(result_back.pop()) ##커서 뒤에서 pop해서 커서 앞에 push
        elif each=='-' :
            if len(result_front) != 0:
                result_front.pop()
        else:
            result_front.append(each)
    result_back.reverse()
    print("".join(result_front)+"".join(result_back))

def main()->None:
    n=int(input())
    for _ in range(n):
        solve(input().rstrip())


main()