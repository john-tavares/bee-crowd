n = int(input())
l = list(map(int, input().split()))

# n = int('5')
# l = list(map(int, '2 5 4 20 10'.split()))

multiples = {
    '2': [],
    '3': [],
    '4': [],
    '5': []
}

for number in l:
    if number % 2 == 0:
        multiples['2'].append(number)
    if number % 3 == 0:
        multiples['3'].append(number)
    if number % 4 == 0:
        multiples['4'].append(number)
    if number % 5 == 0:
        multiples['5'].append(number)

print(f"{len(multiples['2'])} Multiplo(s) de 2")
print(f"{len(multiples['3'])} Multiplo(s) de 3")
print(f"{len(multiples['4'])} Multiplo(s) de 4")
print(f"{len(multiples['5'])} Multiplo(s) de 5")