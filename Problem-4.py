def count_multiples(numbers):
    result = {}

    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count

    return result



numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(numbers)
print(output)





#-------------------------------------------------------------------------------------

print("Input from user ")




def count_multiples(numbers):
    result = {}

   
    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count

    return result



user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))


output = count_multiples(numbers)


print(output)

