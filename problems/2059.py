""""
p=escolha do jogador 1 [0/1] (1 - par/ 0 - impar)
j1, j2=representam o número escolhido pelo jogadores
r= jogador 1 roubou [0/1]
a= jogador 2 acusou de roubo [0/1]
"""

def is_j1_winner(p, j1, j2):
    total = (j1 + j2) % 2
    if p == 1 and total == 0:  # Jogador 1 escolheu par e a soma é par
        return True
    elif p == 0 and total == 1:  # Jogador 1 escolheu ímpar e a soma é ímpar
        return True
    return False

def is_j1_success_cheater(r, a):
    if r == 1 and a == 0:  # Jogador 1 roubou e o jogador 2 não acusou
        return True
    elif r == 0 and a == 1:  # Jogador 2 acusou injustamente
        return True
    return False

p, j1, j2, r, a = map(int, input().split())

if is_j1_success_cheater(r, a):
    print("Jogador 1 ganha!")
elif r == 1 and a == 1:  # Jogador 1 roubou e o jogador 2 acusou corretamente
    print("Jogador 2 ganha!")
elif is_j1_winner(p, j1, j2):
    print("Jogador 1 ganha!")
else:
    print("Jogador 2 ganha!")
