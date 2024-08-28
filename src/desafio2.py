 # 2️⃣ Calculadora de partidas Rankeadas

# Quantidade de vitorias e derrotas do jogador
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))


def calcular_nivel_ranked(vitorias, derrotas):

    # O saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)
    saldo_vitorias = vitorias - derrotas
    
    # Determinação do nível com base no número de vitórias do jogador
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    # Retorna o saldo de vitórias e o nível
    return saldo_vitorias, nivel

saldo_vitorias, nivel = calcular_nivel_ranked(vitorias, derrotas)

# Resultado
print(f"O Herói tem de saldo de {saldo_vitorias} e está no nível {nivel}.")