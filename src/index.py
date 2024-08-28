

#Declaração de variáveis
nome = input("Digite seu nome: ")
XP = int(input("Digite sua quantidade de experiencia (XP) de 0 à 20000:"))
#Estrutura de Tomada de Decisão
if XP <= 1000:
    nivel = "Ferro"
elif 1001 <= XP <= 2000:
    nivel = "Bronze"
elif 2001 <= XP <= 5000:
    nivel = "Prata"
elif 5001 <= XP <= 7000:
    nivel = "Ouro"
elif 7001 <= XP <= 8000:
    nivel = "Platina"
elif 8001 <= XP <= 9000:
    nivel = "Ascendente"
elif 9001 <= XP <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"
#Resultado
print(f"O Herói de nome {nome} está no nível de {nivel}") 
    