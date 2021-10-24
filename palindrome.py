n=int(input("Enter number: "))
rev=0
temp = n
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if rev == temp:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")