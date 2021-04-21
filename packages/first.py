def is_even(n):
    if(n%2==0):
        return True
    else:
        return False
    
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

def is_perfect(n):
    s=0
    for num in range(n):
        if(n%num==0):
            s=s+num
    if s==n:
        print("perfect")
    else:
        print("not perfect")

