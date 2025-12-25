"""
Q16. Print this pattern

*
**
***
****
*****

"""

n=1
a="*"
while n<=5:
    b=n*a
    print(b)
    n+=1


#2.
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


 