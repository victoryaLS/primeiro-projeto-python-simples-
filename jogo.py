import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print(" Adivinhe o número de 1 a 10")
print("Você tem", tentativas, "tentativas!")

while tentativas > 0:
    chute = int(input("Digite seu palpite: "))

    if chute == numero_secreto:
        print(" Você acertou!")
        break
    else:
        tentativas -= 1
        print("Errado! Tentativas restantes:", tentativas)

if chute != numero_secreto:
    print(" Fim de jogo! O número era:", numero_secreto)