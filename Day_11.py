def add(n1, n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
dicti={"+":add,"-":sub,"*":mul,"/":div }
def calculator():
    n1=float(input("Enter a first no:"))
    print("+\n-\n*\n/\n")
    op=input("select a operation")
    if op not in dicti:
        print("invalid operation")
        return
    n2=float(input("enter a second no:"))
    result= dicti[op](n1,n2)
    print(result)
    k=int(input(f"do u want to continue {result} or no"))
    if k==1:
        n1=result
        print("+\n-\n*\n/\n")
        op=input("select a operation")
        if op not in dicti:
            print("invalid operation")
            return
        n2=float(input("enter a second no:"))
        result= dicti[op](n1,n2)
        print(result)
    else:
        calculator()
calculator()

