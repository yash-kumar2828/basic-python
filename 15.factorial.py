def fact(n):
    if n==0 or  n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter a number="))
print(f"factorial of {num} = {fact(num)}")