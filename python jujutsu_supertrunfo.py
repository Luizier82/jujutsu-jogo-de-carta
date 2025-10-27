import random

# ======== DADOS DAS CARTAS ========
cartas_dados = [
    ("Yuji Itadori", {"Força Maldita": 60, "Técnica Amaldiçoada": 80, "Domínio Expandido": 65, "Energia CE": 55, "Velocidade": 75}),
    ("Megumi Fushiguro", {"Força Maldita": 73, "Técnica Amaldiçoada": 70, "Domínio Expandido": 68, "Energia CE": 62, "Velocidade": 60}),
    ("Nobara Kugisaki", {"Força Maldita": 70, "Técnica Amaldiçoada": 72, "Domínio Expandido": 74, "Energia CE": 66, "Velocidade": 72}),
    ("Satoru Gojo", {"Força Maldita": 95, "Técnica Amaldiçoada": 85, "Domínio Expandido": 90, "Energia CE": 92, "Velocidade": 80}),
    ("Sukuna", {"Força Maldita": 94, "Técnica Amaldiçoada": 88, "Domínio Expandido": 86, "Energia CE": 93, "Velocidade": 74}),
    ("Maki Zenin", {"Força Maldita": 67, "Técnica Amaldiçoada": 82, "Domínio Expandido": 78, "Energia CE": 80, "Velocidade": 70}),
    ("Panda", {"Força Maldita": 75, "Técnica Amaldiçoada": 76, "Domínio Expandido": 72, "Energia CE": 74, "Velocidade": 80}),
    ("Aoi Todo", {"Força Maldita": 78, "Técnica Amaldiçoada": 73, "Domínio Expandido": 77, "Energia CE": 79, "Velocidade": 84}),
    ("Kento Nanami", {"Força Maldita": 77, "Técnica Amaldiçoada": 75, "Domínio Expandido": 71, "Energia CE": 81, "Velocidade": 80}),
    ("Mahito", {"Força Maldita": 76, "Técnica Amaldiçoada": 87, "Domínio Expandido": 83, "Energia CE": 85, "Velocidade": 75}),
    ("Toge Inumaki", {"Força Maldita": 69, "Técnica Amaldiçoada": 71, "Domínio Expandido": 67, "Energia CE": 63, "Velocidade": 73}),
    ("Yuta Okkotsu", {"Força Maldita": 89, "Técnica Amaldiçoada": 84, "Domínio Expandido": 88, "Energia CE": 90, "Velocidade": 82}),
    ("Kenjaku", {"Força Maldita": 86, "Técnica Amaldiçoada": 89, "Domínio Expandido": 85, "Energia CE": 87, "Velocidade": 78}),
    ("Yuki Tsukumo", {"Força Maldita": 88, "Técnica Amaldiçoada": 83, "Domínio Expandido": 89, "Energia CE": 84, "Velocidade": 86}),
    ("Choso", {"Força Maldita": 79, "Técnica Amaldiçoada": 77, "Domínio Expandido": 75, "Energia CE": 76, "Velocidade": 71}),
    ("Haruta Shigemo", {"Força Maldita": 65, "Técnica Amaldiçoada": 68, "Domínio Expandido": 64, "Energia CE": 60, "Velocidade": 69}),
    ("Mai Zenin", {"Força Maldita": 63, "Técnica Amaldiçoada": 66, "Domínio Expandido": 62, "Energia CE": 61, "Velocidade": 67}),
    ("Naobito Zenin", {"Força Maldita": 82, "Técnica Amaldiçoada": 79, "Domínio Expandido": 81, "Energia CE": 83, "Velocidade": 77}),
    ("Kinji Hakari", {"Força Maldita": 74, "Técnica Amaldiçoada": 78, "Domínio Expandido": 73, "Energia CE": 72, "Velocidade": 81}),
    ("Hajime Kashimo", {"Força Maldita": 85, "Técnica Amaldiçoada": 86, "Domínio Expandido": 84, "Energia CE": 88, "Velocidade": 89}),
]

SUPER_TRUNFO = "Satoru Gojo"

# ======== FUNÇÕES ========

def distribuir_cartas(baralho):
    """Distribui 4 cartas aleatórias para cada jogador"""
    random.shuffle(baralho)
    return baralho[:4], baralho[4:8]

def mostrar_carta(nome, atributos):
    print(f"\n🃏 {nome}")
    for atributo, valor in atributos.items():
        print(f"  {atributo}: {valor}")

def mostrar_mao(mao):
    print("\nSuas cartas:")
    for i, (nome, _) in enumerate(mao):
        print(f"{i+1}. {nome}")

def jogar_rodada(mao_jogador, mao_computador):
    """Executa uma rodada de batalha"""
    print("\n===== NOVA RODADA =====")

    # Mostrar as cartas do jogador
    mostrar_mao(mao_jogador)

    # Escolher carta
    escolha = int(input("\nEscolha o número da carta que deseja usar: ")) - 1
    carta_jogador = mao_jogador.pop(escolha)
    carta_pc = random.choice(mao_computador)
    mao_computador.remove(carta_pc)

    print("\nSua carta:")
    mostrar_carta(carta_jogador[0], carta_jogador[1])

    print("\nCarta do computador:")
    mostrar_carta(carta_pc[0], carta_pc[1])

    # Checar Super Trunfo
    if carta_jogador[0] == SUPER_TRUNFO and carta_pc[0] != SUPER_TRUNFO:
        print(f"\n🎴 VOCÊ USOU O SUPER TRUNFO ({SUPER_TRUNFO})! Vitória automática!")
        return 1
    elif carta_pc[0] == SUPER_TRUNFO and carta_jogador[0] != SUPER_TRUNFO:
        print(f"\n💀 O COMPUTADOR USOU O SUPER TRUNFO ({SUPER_TRUNFO})! Derrota automática!")
        return -1
    elif carta_jogador[0] == SUPER_TRUNFO and carta_pc[0] == SUPER_TRUNFO:
        print("\n😱 AMBOS USARAM O SUPER TRUNFO! Empate!")
        return 0

    # Jogador escolhe o atributo
    atributos = list(carta_jogador[1].keys())
    print("\nEscolha um atributo para competir:")
    for i, atributo in enumerate(atributos):
        print(f"{i+1}. {atributo}")

    escolha_attr = int(input("\nDigite o número do atributo: ")) - 1
    atributo_escolhido = atributos[escolha_attr]

    valor_jogador = carta_jogador[1][atributo_escolhido]
    valor_pc = carta_pc[1][atributo_escolhido]

    print(f"\nAtributo escolhido: {atributo_escolhido}")
    print(f"{carta_jogador[0]}: {valor_jogador}  vs  {carta_pc[0]}: {valor_pc}")

    if valor_jogador > valor_pc:
        print("\n🎉 Você venceu esta rodada!")
        return 1
    elif valor_jogador < valor_pc:
        print("\n💀 O computador venceu esta rodada!")
        return -1
    else:
        print("\n⚖️ Empate!")
        return 0

# ======== LOOP PRINCIPAL ========

def jogar():
    print(f"\n🃏 SUPER TRUNFO: {SUPER_TRUNFO} 🃏")
    baralho = cartas_dados.copy()

    mao_jogador, mao_computador = distribuir_cartas(baralho)

    pontos_jogador = 0
    pontos_pc = 0
    rodada = 1

    while mao_jogador and mao_computador:
        print(f"\n===== RODADA {rodada} =====")
        resultado = jogar_rodada(mao_jogador, mao_computador)

        if resultado == 1:
            pontos_jogador += 1
        elif resultado == -1:
            pontos_pc += 1

        print(f"\nPlacar parcial: Você {pontos_jogador} x {pontos_pc} Computador")
        rodada += 1

    print("\n===== FIM DE JOGO =====")
    print(f"\nPlacar final: Você {pontos_jogador} x {pontos_pc} Computador")
    if pontos_jogador > pontos_pc:
        print("🏆 Você é o grande vencedor!")
    elif pontos_jogador < pontos_pc:
        print("💀 O computador venceu!")
    else:
        print("⚖️ Empate geral!")

# ======== EXECUTAR ========
if __name__ == "__main__":
    jogar()
