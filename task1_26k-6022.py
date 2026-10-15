userVal=None
permenantArr=[]
tempArr=[]
x=1
while x>0:
    userVal=int(input("Enter security stage depth (min 4): "))
    if(userVal<4):
        print("number should be greater than or equal to 4")
    else:
        break

    
previousVal=2
permenantArr.append(previousVal)
# print(previousVal)
x=1
while x<userVal:
    if x%2!=0 :
        previousVal=previousVal+3
        permenantArr.append(previousVal)
        # print(previousVal) #5
        # print(nextVal)
    else:
        previousVal=previousVal*2
        # print(previousVal) #10
        permenantArr.append(previousVal)
    x+=1
# print("ye wali permanent array",permenantArr)
tempArr=permenantArr.copy()
tempArr.remove(tempArr[len(tempArr)-1])
tempArr.append("[ ? ]")
# print("ye wali temp array",tempArr)
print("Firewall Code Generated:",end=" ")
i=0
while i<len(tempArr):
    print(tempArr[i],end=" ")
    i+=1
print()

    
# print("ye wali permanent array",permenantArr)
# print("ye wali temp array",tempArr)
userGuess=None
y=1
userGuess=int(input("Enter the override token: "))
if(userGuess==permenantArr[len(permenantArr)-1]):
    # print(permenantArr[len(permenantArr)-1])
    print("ACCESS GRANTED: Firewall bypassed successfully! Full sequence:",end=" ")
    i=0
    while i<len(permenantArr):
        print(permenantArr[i],end=" ")
        i+=1
    print()
else:
    print("ACCESS DENIED: Alarm triggered! Expected value:",permenantArr[len(permenantArr)-1])