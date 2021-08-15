def TP(a,b,c):
   if(a**2+b**2==c**2):
        return "YES"
   else:
        return "NO"
print("Enter a,b,c : ",end="")
try:
  a,b,c=map(int,input().split())
  print(TP(a,b,c))
except:
  print("Invalid input")

