jogador1 = int(input("Exerça sua jogada, jogador 1 (1 = pedra, 2 = tesoura, 3 = papel):"))
jogador2 = int(input("Exerça sua jogada, jogador 2 (1 = pedra, 2 = tesoura, 3 = papel):"))

pedra = 1
tesoura = 2
papel = 3

if jogador1 == pedra and jogador2 == pedra:
    print("Empate!")

if jogador1 == tesoura and jogador2 == tesoura:
    print("Empate!")

if jogador1 == papel and jogador2 == papel:
    print("Empate!")

if jogador1 == pedra and jogador2 == tesoura:
    print("Vitória do jogador 1!")

if jogador1 == tesoura and jogador2 == pedra:
    print("Vitória do jogador 2!")

if jogador1 == pedra and jogador2 == papel:
    print("Vitória do jogador 2!")

if jogador1 == papel and jogador2 == pedra:
    print("Vitória do jogador 1!")

if jogador1 == papel and jogador2 == tesoura:
    print("Vitória do jogador 2!")

if jogador1 == tesoura and jogador2 == papel:
    print("Vitória do jogador 1!")