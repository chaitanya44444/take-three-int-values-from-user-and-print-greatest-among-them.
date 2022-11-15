int1=int(input("write an integer"))
int2=int(input("write another integer"))
int3=int(input("write another integer"))

if int1>=int2>=int3:
    print(int1,"has the highest value") 
elif int2>=int3:
    print(int(int2),"has the highest value among the 3")
else:
    print(int3,"has the best value")
