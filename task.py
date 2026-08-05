
# COUNT CHARCTER 
word="keerthana"
freq=0
for i in word:
    freq=freq+1
print(freq)




# frequency in a string 
word="leepyear"
freq={}
for i in word:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)


#  FIRST NON REPEATING CHARCTER 
word="thursday"
freq={}
for i in word:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print("charcter:",freq)

for i in word:
    if freq[i]==1:
       print("first non repeating character:",i)
       break


# STACK
stack=[1,2,3,3,4]
stack.append(10)
print(stack) 

stack=[1,2,3,3,4]
stack.pop()
print(stack)

stack=[1,2,3,3,4]
if len(stack)==0:
    print("empty")
else:
    print("fill")

stack=[1,2,3,3,4]
print(stack[-1])

# QUEUE
data=[1,2,3,4,5]
data.append(90)
print(data)

data=[1,2,3,4,5]
data.pop()
print(data)
print(data[-1])
if len(data)==0:
    print("empty data")
else:
    print("data fill")




# DETECT DUPLICATES 
a=[10,101,20,20,30,50,50]
check=[]
duplicates=[]
for i in a:
    if i in check:
        duplicates.append(i)
    else:
        check.append(i)
print("duplicates found:",duplicates)