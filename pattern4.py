n = int(input("Enter no of rows: "))
num = 1
for i in range(n+1, 0,-1):
     num=1	
     for j in range(0, i-1):
      print(num, end=" ")
      num= num + 1
     print("\r")

