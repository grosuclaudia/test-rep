numbers=[1,2,56,32,51,2,8,92,15]
print(numbers)
iterations=1
n=9
while iterations<n:
    j=0
    while j<=n-2:
        if numbers[j]>numbers[j+1]:
            temp=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp
        j=j+1
    iterations=iterations+1
print(numbers)

