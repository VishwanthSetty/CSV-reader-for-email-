import csv
file=open("book.csv","r")
str1=csv.reader(file)
x=str(input("Enter col name that you want : "))
#for i in str1:
i=list(str1)
print(i)
for j in range(len(i[0])):
    if(x.lower()==str(i[0][j]).lower()):
        pos=j
        print("yes its present")

print("\n\n")
print("this are present in the given field : ")
for j in range(1,len(i)):
    print (i[j][pos])
file.close()
