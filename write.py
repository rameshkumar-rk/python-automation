f=open('inputFile.txt','r')
p=open("p.txt",'w')
f1=open("f.txt",'w')
for l in f:
   l_split=l.split()
   if l_split[2]=='P':
       p.write(l)
   else:
       f1.write(l)
f.close()
p.close()
f