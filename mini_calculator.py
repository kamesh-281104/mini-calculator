no_1=int(input("enter the first no: "))
no_2=int(input("enter the second no: "))
choose=("what function u neeed to perform(add/sub/mul,div): ")
if (choose=="add"):
    sum=no_1+no_2
    print("ans is ",sum)
elif (choose=="sub"):
    if(no_1>=no_2):
        sub=no_1-no_2
        print("ans is ",sub)
    else:
        sub=no_2-no_1
        print("ans is ",sub)
elif(choose=="mul"):
    mul=no_1*no_2
    print("ans is ",mul)
elif(choose=="div"):
    if(no_2!=0):
        div=no_1/no_2
        print("ans is ",div)
    else:
        print("ivalid")
else:
    print("incorrect option")