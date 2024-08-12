def hyam_sequence(n:int):
    text="0 "
    for i in range(n):
        text+=f"{i+1} "*(i+1)
    return text.split()

count = 1
while True:
    try:
        n = int(input())
        sequence = hyam_sequence(n)
        if len(sequence) == 1:
            print(f"Caso {count}: {len(sequence)} numero")
        else:
            print(f"Caso {count}: {len(sequence)} numeros")
        text = " ".join(sequence)
        print(f"{text}\n")
        count+=1
    except EOFError:
        break
