sentence="python is hard python is powerful"
count={}
words=sentence.split()
for word in words:
    if word in count:
        count[word]=count[word]+1
    else:
        count[word]=1
print(count)