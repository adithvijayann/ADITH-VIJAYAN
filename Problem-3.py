def generate_series(a):
   
    if a % 2 == 0:
        limit = a - 1
    else:
        limit = a

    numbers = []
    current = 1

    for i in range(limit):
        numbers.append(current)
        current += 2  

    return numbers



a = int(input("Enter a number: "))
result = generate_series(a)


for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(result[i], end=", ")
