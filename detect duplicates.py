a=[10,20,30,40,50,10,20]
check=[]
duplicates=[]
for i in a:
    if i in check:
        duplicates.append(i)
    else:
        check.append(i)
print("unique: ",check)
print("duplicates: ",duplicates)

    