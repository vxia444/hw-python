n = int(input())
counter = 0
set1 = set()
odds = set()
evens = set()

for i in range(n):
    names = input()
    counter += 1
    sum1 = sum(ord(ch) for ch in names)
    print(sum1 // counter)  
    if sum1 % 2 == 0:
        evens.add(sum1)
    else:
        odds.add(sum1)
sum_odd = sum(odds)
sum_even = sum(evens)

if sum_odd == sum_even:
    print(sum_odd, " - ", sum_odd)

if sum_odd > sum_even:
    print(sum_odd, " - ", sum_even)

if sum_even > sum_odd:
    print(sum_even, " - ", sum_odd)
