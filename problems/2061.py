n, m = map(int, input().split())

for i in range(m):
    action = input()
    if action == 'fechou':
        n += 1
    else:
        n -= 1

# n, m = map(int, '3 5'.split())

# actions = ['fechou', 'fechou', 'clicou', 'clicou', 'clicou']

# for action in actions:
#     # action = input()
#     if action == 'fechou':
#         n += 1
#     else:
#         n -= 1

print(n)