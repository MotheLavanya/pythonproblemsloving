# solid triangle pattern:
n = int(input("Enter a number: "))
for i in range(1,+n+1):
    print("* " * i)

# output:
# *
# * *
# * * *
# * * * *
# * * * * * 

# hollow square pattern:
n = int(input("Enter a number: "))
for i in range(1,n+1):
    res=""
    for j in range(1,n+1):
        if i == 1 or j == 1 or i == n or j == n:
            res+="*" +" "
        else:
            res+=" " + " "
    print(res) 

# (or)

for i in range(1,n+1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("* " + "  "*(n-2) + "* ")    

# output
# * * * * *
# *       *
# *       *
# *       *
# * * * * *  

# hollow triangle pattern:
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  "*(i-2) + "* ") 

# output:
# *
# * *
# *   *
# *     *
# * * * * *


# hollow inverted traingle pattern:
n = int(input("Enter a number: "))
for i in range(n,0,-1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  "*(i-2) + "* ")    

# output:
# * * * * *
# *     *
# *   *
# * *
# *


# hollow rectangular pattern:
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i == 1 or i == n:
        print("* "*(n*2))
    else:
        print("* " +"  "*(n*2-2) +"*")   

       
# output:
# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *
  

# hollow revrese inverted traingle pattern:
n = int(input("Enter a number: "))
left_space = ""
for i in range(1,n+1):
    left_space = "  " *(n-i)
    if i == 1 or i == n:
        print(left_space + "* "*i)
    else:
        print(left_space+"* "+"  "*(i-2)+"*")    

# output
#         * 
#      *  *
#    *    *
#  *      *
# * * * * *





