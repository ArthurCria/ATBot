nome = input("Olá! Qual é o seu nome? ")
print(f"Que nome legal, {nome}! Meu nome é ATBot")
idade = int(input("Qual sua idade? "))
idade_ATBot = 3
if idade > idade_ATBot:
    print(f"Você é mais velho que eu! Tenho {idade_ATBot} anos!")
elif idade < idade_ATBot:
     print(f"Uau! Você é mais novo que eu! Tenho {idade_ATBot} anos!")
else:
     print("Sua idade é igual a minha!!")
questao = int(input("Agora uma pergunta de matemática! Quanto é 24 + 34? "))
soma = 24 + 34
if questao == soma:
    print("Você acertou! Muito bem!")
else:
    print("Você errou. Mas tudo bem!")
while True:
    horario = int(input("Digite a hora de onde você esta(de 0 a 23): "))
    if 5 <= horario <= 12:
        print("Bom dia pra você!")
        break
    elif 13 <= horario <= 19:
        print("Boa tarde pra você!")
        break
    elif 20 <= horario <= 23 or 0 <= horario <= 4:
        print("Boa noite pra você!")
        break
    else:
        print("Horário inválido! Digite números de 0 até 23!")
print("Obrigado por conversar comigo! Foi bom conhecer você!")