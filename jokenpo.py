import random

jogada = ("pedra", "papel", "tesoura")
mao_jogador = None
mao_pc = random.choice(jogada)

while mao_jogador not in jogada:
    mao_jogador = input("Escolha pedra, papel ou tesoura: ")

print(f"Jogador: {mao_jogador}")
print(f"Computador: {mao_pc}")

if mao_jogador == "pedra" and mao_pc == "tesoura":
    print("Você ganhou! Pedra ganha de tesoura.")
elif mao_jogador == "papel" and mao_pc == "pedra":
    print("Você ganhou! Papel ganha de pedra.")
elif mao_jogador == "tesoura" and mao_pc == "papel":
    print("Você ganho! Tesoura ganha de papel.")
elif mao_jogador == mao_pc:
    print("Empate!")
else:
    print("Você perdeu! :( ")

# comentário