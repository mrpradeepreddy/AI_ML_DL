# Q13. Find sum of only odd numbers from 1 to 20

sum=0
a=1
while a<=20:
     if a%2 != 0:
         sum+=a
     a+=1
print(sum)

# sum=0
# for i in range(1,20):
#     if i%2!=0:
#         sum+=i
# print(sum)