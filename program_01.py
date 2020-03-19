name=input("enter the name you want:")
length=len(name)
for i in range(length):
    print(" "*(length-i)+name[:i+1])


"""
enter the name you want:supriya
       s
      su
     sup
    supr
   supri
  supriy
 supriya

 """

    
