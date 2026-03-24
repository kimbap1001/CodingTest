import sys
input=sys.stdin.readline

def solve(students:list, cap:int)->int:
    rooms=0
    for sex in students:
        for grade in sex:
            if grade != 0:
                rooms+=(grade+cap-1)//cap
                #math.ceil 과 같은 결과를 내는 올림계산법
    return rooms

def input_stds(students:list, n:int)->None:
    for _ in range(n):
        a,b = map(int, input().split())
        students[a][b-1]+=1

def main()->None:
    n, cap = map(int, input().split())
    students=[[0 for i in range(6)] for j in range(2)]
    input_stds(students, n)
    print(solve(students, cap))

if __name__=="__main__":
    main()