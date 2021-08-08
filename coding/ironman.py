def saveIronman (s) : 
    #Complete the function
    #s = input("Enter a string: ")
    only_alpha= ""
    for char in s:
     if char.isalpha() or char.isdigit():
          only_alpha += char
    S=only_alpha.lower()
    if(S==S[::-1]):
      # print("YES")
      return True
    else:
      #  print("NO")
      return False 

    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    s = input()
    ans = saveIronman(s)
    if(ans == True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
