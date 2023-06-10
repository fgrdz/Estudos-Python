# Aprendendo variáveis e print
#pais = "italia"
#numero_titulos= "4"

#print(pais, "ganhou", numero_titulos, "titulos mundiais")

#Jogo advinhação

print("Bem vindo ao jogo de navegação")
print("*******************************")
numero_tentativas = 3
numero_secreto = 42
contador = 1

while(contador <= numero_tentativas):
    print("tentativa", contador, "de", numero_tentativas)
    chute_str = input("Digite seu numero: ")


    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute == numero_secreto):
        print("Você acertou")
    else:
        if(chute> numero_secreto):
            print("EROOOOOOU, maior que o numero secreto")
        elif(chute< numero_secreto):
            print("EROOOOOOU, menor que o numero secreto")
    contador = contador + 1
    
    print("*******FIM DE JOGO********")