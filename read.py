f=open('inputFile.txt','r')
for l in f:
   l_split=l.split()
   if l_split[2]=='P':
       print(l)
f.close()
