file=open("data.txt",'r')
words=[]
list=[]
for i in file:
    for j in i.split():
        words.append(j)
print("actual words is:",words)
count=0
for i in words:
    if i not in list:
        list.append(i)
        count+=1
print("unique words count is: ",count,"\nthe unique words are: ",list)
    
"""
actual words is: ['hi', 'this', 'is', 'paidy', 'hi', 'this', 'is', 'kumar', 'this', 'is', 'sumita', 'how', 'are', 'you']
unique words count is:  9 
the unique words are:  ['hi', 'this', 'is', 'paidy', 'kumar', 'sumita', 'how', 'are', 'you']
    
"""
