marks1 = [[30, 18], [23, 21, 25, 8, 27]]
marks2 = [[33, 42, 65, 45], [67, 54]]
marks3 = [[74, 98, 100], [87, 96, 71, 89]]

print("The amount of rows in the first set of marks are: ", len(marks1))
print("The amount of columns in the first set of marks are: ",len(marks1[0]))
print("\n")
print("The amount of rows in the second set of marks are: ", len(marks2))
print("The amount of columns in the second set of marks are: ",len(marks2[0]))
print("\n")
print("The amount of rows in the third set of marks are: ", len(marks3))
print("The amount of columns in the third set of marks are: ",len(marks3[0]))
print("\n")

result=[]
rows=len(marks1)
col=len(marks1[0])

for i in range(rows):
  temp=[]
  for j in range(col):
    temp.append(marks1[i][j]+marks1[i][j])
  result.append(temp)
  
print("The addition of the matrix in the first set of marks is:", result)

print("\nMarks <= 30:")
for mark in marks1:
    print(mark, end=' ')
    
print("\n\nMarks between 31 and 69:")
for mark in marks2:
    print(mark, end=' ')
    
print("\n\nMarks >= 70:")    
for mark in marks3:
    print(mark, end=' ') 