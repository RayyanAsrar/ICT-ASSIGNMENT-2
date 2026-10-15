userVal=None
permenantArr=[]
tempArr=[]
x=1
while x>0:
    userVal=int(input("Enter frequency cycle depth (min 4): "))
    if(userVal<4):
        print("number should be greater than or equal to 4")
    else:
        break
# print(userVal) 

    
previousVal=2
permenantArr.append(previousVal)
# print(permenantArr) #[2]
x=1
while x<userVal:
    previousVal=previousVal*2+1
    permenantArr.append(previousVal)
    # print(previousVal) #x=1 
    x+=1
# print("permenantArr",permenantArr) 
# print(x) 

tempArr=permenantArr.copy()
# print("tempArr",tempArr)
tempArr.remove(tempArr[len(tempArr)-1])
# print("tempArr",tempArr)
tempArr.append("[ ? ]")
# print("tempArr",tempArr) 
# print("permenantArr",permenantArr) #[2, 5, 11, 23, 47, 95]

print("Shield Modulation Stream:")
i=0
while i<len(tempArr):
    print(tempArr[i],end=" ")
    i+=1
print()

userGuess=int(input("Enter stabilizing frequency: "))
# print(permenantArr[len(permenantArr)-1]) #95 bhi agya
if(userGuess==permenantArr[len(permenantArr)-1]):
    print("SHIELD SYNCHRONIZED: Plasma wave deflected!")
    print("Full sequence:",end=" ")
    i=0
    while i<len(permenantArr):
        print(permenantArr[i],end=" ")
        i+=1
    print()
else:
    print("SHIELD COLLAPSE: Frequency mismatch! Expected value:",permenantArr[len(permenantArr)-1])