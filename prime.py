num = int(input("Enter the Number: "))
if num > 1:
 for i in range(2, int(num/2)):
     if num % i == 0:
        print(num,"Not a Prime Number")
        break
 else:
        print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")

    

    