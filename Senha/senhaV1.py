#Teste Jogo Senha
import random
#Função chamada quando se acerta a senha
def correto(senha, tentativa, chances):
    print("\nVocê acertou!!", "\nMinha senha era", senha, "\nVocê tentou", tentativa, "após",chances, "tentativas")
    novo = input("\nNovamente [S/N]? ")
    while novo.lower() != "s" and novo.lower() != "n":
        novo = input("\nEscolha S ou N. Novamente [S/N]? ")
        if novo.lower() == "n":
            jogo = False
        else:
            jogo = True
    return()


jogo = True
while jogo:
# Gera a senha
    senha = str(random.randint(0, 9999)).zfill(4)
    print(senha)

# O jogo!
    chances = 0
    while senha:
        chances += 1
        try:
            tentativa = input("\nSua senha (4 dígitos)? ")
            contr = int(tentativa)
            if len(tentativa) < 4:
                raise Exception
        except ValueError:
            print("\nUse apenas dígitos 0-9")
        except Exception:
            print("\nVocê entrou com menos de 4 dígitos!")

#Posicao = acertou o número na posição
#Valor = acertou o número e errou a posiçáo
        Posicao = 0; Valor = 0
#Confere os acertos
        for x in range(len(tentativa)):
            if senha.count(tentativa[x]) != 0 and senha[x] != tentativa[x]:
                Valor += 1
            elif senha.count(tentativa[x]) != 0 and senha[x] == tentativa[x]:
                Posicao += 1
        print("\nVocê acertou", Valor, "dígitos na posição errada")
        print("Você acertou", Posicao, "dígitos na posição correta")
#Se acertou a senha, chama função de fim.
        if tentativa == senha:
            correto(senha, tentativa, chances)





