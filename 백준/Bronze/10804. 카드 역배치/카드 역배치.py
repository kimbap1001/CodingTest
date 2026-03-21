import sys
input=sys.stdin.readline

def solve()->None:
    cards=[i+1 for i in range(20)]
    for _ in range(10):
        a,b=map(int,input().split())
        new_cards=cards[a-1:b]
        new_cards.reverse()
        cards[a-1:b]=new_cards
    print(*cards)

if __name__=="__main__":
    solve()