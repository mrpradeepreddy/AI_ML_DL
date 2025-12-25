# Q12. Count even numbers between 1 and 100

count=0
a=1
while a<=100:
    if a%2 == 0:
        count+=1
    a+=1
print(count)

# count=0
# for i in range(1,101):
#     if i%2==0:
#         count+=1
# print("Total even numbers between 1 and 100 are:",count)