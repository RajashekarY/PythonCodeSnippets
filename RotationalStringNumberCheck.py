inp1= input("Enter a word 1 : ")
inp2 = input("Enter a word 2 : ")
in1=[]
in2=[]
for i in inp1:
    in1.append(i)
for j in inp2:
    in2.append(j)
##if len(inp1)==len(inp2):
##        for k in in2:
##            if k in in1:
##                index = in1.index(k)
##            for i in in1[index:]:
##                if i==in1[index]:
##                    #print(i,index)
##                    for i in range(len(inp1)):
##                        if in1 is not in2:
##                            for i in range(len(in2)):
##                                in2.insert(0,in2.pop())
##                                if in1==in2:
##                                    print("rotational")
##                                    break
##
##                                else:
##                                    print("not rotational")
##                                    
##else:
##    print("word 1 length is not equal to word 2")
def rotational(in1,in2):
    inp1= input("Enter a word 1 : ")
    inp2 = input("Enter a word 2 : ")
    in1=[]
    in2=[]
    for i in inp1:
        in1.append(i)
    for j in inp2:
        in2.append(j)
    print(in1,in2)
    for i in range(len(in2)):
        if in1 is not in2:
             in2.insert(0,in2.pop())
             if in1==in2:
                 print(in1,in2)
                 print("rotational")
                 break
             else:
                 print("not rotational")
            
while True:
    rotational(in1,in2)
    break

                    
                
                
