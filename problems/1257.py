def find_alphabet_position(char):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(char)

n = int(input())

for i in range(n):
    lines = int(input())
    hash_sum = 0
    for j in range(lines):
        item = input()
        for k in range(len(item)):
            position_in_alphabet = find_alphabet_position(item[k])
            count_hash = position_in_alphabet + j + k
            hash_sum += count_hash
    print(hash_sum)