import sys
input=sys.stdin.readline

def solve(word1:str, word2:str)->bool:
    alphas =[0]*26
    for alpha1 in word1:
        alphas[ord(alpha1)-ord('a')]+=1
    for alpha2 in word2:
        alphas[ord(alpha2)-ord('a')]-=1
    return alphas==[0]*26

def main()->None:
    for _ in range(int(input())):
        word1, word2=input().rstrip().split()
        if solve(word1, word2):
            print("Possible")
        else:
            print("Impossible")

if __name__ == "__main__":
    main()