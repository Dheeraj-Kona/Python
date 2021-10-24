n = int(input("Enter no of rows: "))
num = 65
for i in range(0, n):
     ch = chr(num)	
     for j in range(0, i+1):
        print(ch, end=" ")
     num= num + 1
     print("\r")
