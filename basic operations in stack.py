stack=[]
print(stack)  

stack=[10,20,30,40,50,50,20,30]
print(stack)      


stack.append(100)
print(stack)


stack.pop()
print(stack)


if len(stack)==0:
    print("empty")
else:
    print("full")


print(stack[-1])
