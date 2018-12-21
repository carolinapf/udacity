# udacity

continuar = True
while continuar == True:

    dificuldade = input("Digite o nível de dificuldade:")

    if dificuldade == "fácil":
        print("complete a frase: Meu __ é Carolina")
        resposta = input("digite sua resposta:")
        if resposta == "nome":
            print("Parabéns!")
        else:
            print("Vc errou =( ")

        tentar_novamente = input("Deseja tentar novamente? ")
        if tentar_novamente == "sim":
            continuar = True
        if tentar_novamente == "não":
            continuar = False
            print("Até mais!")
            
    if dificuldade == "médio":
        print("complete a frase: quem __ em __ ___ é paulista" )
        resposta = input("digite sua resposta:")
        if resposta == "quem nasce em são paulo é paulista":
            print("Parabéns!")
        else:
            print("Vc errou =( ")

        tentar_novamente = input("Deseja tentar novamente? ")
        if tentar_novamente == "sim":
            continuar = True
        if tentar_novamente == "não":
            continuar = False
            print("Até mais!")

    if dificuldade == "difícil":
        print("complete a frase: quem ___ _____ fere, ___ _____ será ______" )
        resposta = input("digite sua resposta:")
        if resposta == "quem com ferro fere, com ferro será ferido":
            print("Parabéns!")
        else:
            print("Vc errou =( ")

    tentar_novamente = input("Deseja tentar novamente? ")
    if tentar_novamente == "sim":
        continuar = True
    if tentar_novamente == "não":
        continuar = False
        print("Até mais!")
