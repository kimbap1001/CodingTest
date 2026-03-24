import sys
input=sys.stdin.readline

def solve(room_number:str)->int:
    nums=[0]*10
    for num in room_number:
        nums[ord(num)-ord('0')]+=1
    
    diff=abs(nums[6]-nums[9])
    if diff>1:
        nums[6]=nums[9]=(nums[6]+nums[9]+1)//2
    return max(nums)

def main()->None:
    print(solve(input().rstrip()))

main()