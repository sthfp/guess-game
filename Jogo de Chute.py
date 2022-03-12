import random

def valida_dados(info):
    if info.isnumeric() is True:
        info = int(info)
        if info > 100:
            print("O número passado deve ser menor ou igual a 100!")
            return False
            
        if info < 1:
            print("O número passado deve ser maior ou igual a 1!")
            return False
            
        return True
        
    if info == "":
        return None
    print("A informação passada não é válida!")
    return False
    
def testa_chute(chute, resposta):
    if chute == resposta:
        return True
    return False
    
def main():
    resposta = random.randint(1,100)
    info = input("Chute um número inteiro entre 1 e 100: ")
    while valida_dados(info) is False:
        info = input("Chute um número inteiro entre 1 e 100:")
    chute= int(info)
    while testa_chute(chute, resposta) is False:
        if chute > resposta:
            print("O número chutado foi muito alto!")
            chute = int(input("Chute um número inteiro entre 1 e 100: "))
        else:
            print("O número chutado foi muito baixo!")
            chute = int(input("Chute um número inteiro entre 1 e 100: "))
            
        print("Parabéns! Você acertou a resposta!")
        
main()