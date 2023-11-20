N = int(input("Enter the number of names: "))

odd_numbers = set()
even_numbers = set()

for i in range(1, N + 1):
    name = input()

    name_sum = sum(ord(letter) for letter in name)
    name_result = name_sum // i

    if name_result % 2 == 0:
        even_numbers.add(name_result)
    else:
        odd_numbers.add(name_result)

sum_odd = sum(odd_numbers)
sum_even = sum(even_numbers)

if sum_odd == sum_even:
    result = '-'.join(str(value) for value in sorted(odd_numbers | even_numbers))
elif sum_odd > sum_even:
    result = '-'.join(str(value) for value in sorted(odd_numbers - even_numbers))
else:
    result = ','.join(str(value) for value in sorted(even_numbers ^ odd_numbers))

print(result)
