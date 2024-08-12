import re

count = 1
while True:
    try:
        n1 = input()
        n2 = input()
        # n1 = '78954'
        # n2 = '7895478954789547895447895478954'
        print(f"Caso #{count}:")
        size = len(re.findall(f'(?={n1})', n2))
        if size > 0:
            print(f"Qtd.Subsequencias: {size}")
            position = int(re.search(f'{n1}' if size == 1 else f'{n1}$', n2).span()[0])+1
            print(f"Pos: {position}\n")
        else:
            print("Nao existe subsequencia\n")
        count+=1
    except EOFError:
        break