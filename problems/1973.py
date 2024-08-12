import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

position = 0
visited_stars = 0
rams_stolen = 0

while 0 <= position < n:
    if x[position] > 0:
        x[position] -= 1
        rams_stolen += 1

    visited_stars += 1
    next_position = position + 1 if x[position] % 2 == 1 else position - 1

    if next_position < 0 or next_position >= n:
        break
    
    position = next_position

print(visited_stars, sum(x))