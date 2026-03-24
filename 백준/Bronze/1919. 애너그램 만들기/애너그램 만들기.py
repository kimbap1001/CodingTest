import sys
input=sys.stdin.readline

def solve()->None:
    word1=input().rstrip()
    word2=input().rstrip()
    result1=[0 for _ in range(26)]
    result2=[0 for _ in range(26)]
    for alphabet in word1:
        result1[ord(alphabet)-97]+=1
    for alphabet in word2:
        result2[ord(alphabet)-97]+=1
    sum=0
    for i in range(26):
        sum+=abs(result1[i]-result2[i])
    print(sum)

if __name__=="__main__":
    solve()