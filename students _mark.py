a=int(input("enter the mark of python"))
b=int(input("enter the mark of chemistry"))
c=int(input("enter the mark of mathematics "))
totalmark=a+b+c
print("total mark is",totalmark)
avg=a+b+c/3
if avg>=80:
 print("gradeA")
elif avg<80 and avg>60:
 print("gradeb")
else :
  print("gradeC")
      
