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
            return False
        else:
            jogo = True
            return True
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
        Posicao = sum(1 for x in range(4) if tentativa[x] == senha[x])
        Valor = sum(min(senha.count(dig), tentativa.count(dig)) for dig in set(tentativa)) - Posicao

        print("\nVocê acertou", Valor, "dígitos na posição errada")
        print("Você acertou", Posicao, "dígitos na posição correta")
#Se acertou a senha, chama função de fim.
        if tentativa == senha:
            jogo = correto(senha, tentativa, chances)
            break





