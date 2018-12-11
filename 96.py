v=int(raw_input())
rev=0
while(v>0):
    remainder=v%10
    rev=rev*10+remainder
    v=v/10
print rev    
