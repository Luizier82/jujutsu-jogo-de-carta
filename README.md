#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// ======== ESTRUTURA DE CARTA ========

typedef struct {
    char nome[50];
    int forcaMaldita;
    int tecnicaAmaldicoada;
    int dominioExpandido;
    int energiaCE;
    int velocidade;
} Carta;

// ======== BARALHO COMPLETO ========

Carta baralho[] = {
    {"Yuji Itadori", 60, 80, 65, 55, 75},
    {"Megumi Fushiguro", 73, 70, 68, 62, 60},
    {"Nobara Kugisaki", 70, 72, 74, 66, 72},
    {"Satoru Gojo", 95, 85, 90, 92, 80},
    {"Sukuna", 94, 88, 86, 93, 74},
    {"Maki Zenin", 67, 82, 78, 80, 70},
    {"Panda", 75, 76, 72, 74, 80},
    {"Aoi Todo", 78, 73, 77, 79, 84},
    {"Kento Nanami", 77, 75, 71, 81, 80},
    {"Mahito", 76, 87, 83, 85, 75},
    {"Toge Inumaki", 69, 71, 67, 63, 73},
    {"Yuta Okkotsu", 89, 84, 88, 90, 82},
    {"Kenjaku", 86, 89, 85, 87, 78},
    {"Yuki Tsukumo", 88, 83, 89, 84, 86},
    {"Choso", 79, 77, 75, 76, 71},
    {"Naobito Zenin", 82, 79, 81, 83, 77},
    {"Kinji Hakari", 74, 78, 73, 72, 81},
    {"Hajime Kashimo", 85, 86, 84, 88, 89},
    {"Mai Zenin", 63, 66, 62, 61, 67},
    {"Haruta Shigemo", 65, 68, 64, 60, 69}
};

int total_cartas = sizeof(baralho) / sizeof(baralho[0]);

// ======== FUNÇÕES ========

void embaralhar(Carta *cartas, int n) {
    for (int i = 0; i < n; i++) {
        int j = rand() % n;
        Carta temp = cartas[i];
        cartas[i] = cartas[j];
        cartas[j] = temp;
    }
}

void mostrar_carta(Carta c) {
    printf("\n--- %s ---\n", c.nome);
    printf("1. Força Maldita: %d\n", c.forcaMaldita);
    printf("2. Técnica Amaldiçoada: %d\n", c.tecnicaAmaldicoada);
    printf("3. Domínio Expandido: %d\n", c.dominioExpandido);
    printf("4. Energia CE: %d\n", c.energiaCE);
    printf("5. Velocidade: %d\n", c.velocidade);
}

int valor_atributo(Carta c, int atributo) {
    switch (atributo) {
        case 1: return c.forcaMaldita;
        case 2: return c.tecnicaAmaldicoada;
        case 3: return c.dominioExpandido;
        case 4: return c.energiaCE;
        case 5: return c.velocidade;
        default: return 0;
    }
}

void jogar_super_trunfo() {
    // ======== PREPARAÇÃO ========
    embaralhar(baralho, total_cartas);

    Carta jogador[30], computador[30];
    int qtdJogador = 0, qtdComputador = 0;

    // Divide o baralho igualmente
    for (int i = 0; i < total_cartas; i++) {
        if (i % 2 == 0)
            jogador[qtdJogador++] = baralho[i];
        else
            computador[qtdComputador++] = baralho[i];
    }

    int vezDoJogador = 1;
    int rodada = 1;

    // ======== LOOP DO JOGO ========
    while (qtdJogador > 0 && qtdComputador > 0) {
        printf("\n===== RODADA %d =====\n", rodada++);
        Carta cartaJ = jogador[0];
        Carta cartaC = computador[0];

        printf("\nSua carta:");
        mostrar_carta(cartaJ);

        int escolha;
        if (vezDoJogador) {
            printf("\nEscolha um atributo (1-5): ");
            scanf("%d", &escolha);
        } else {
            escolha = (rand() % 5) + 1;
            printf("\nO computador escolheu o atributo %d!\n", escolha);
        }

        int valorJ = valor_atributo(cartaJ, escolha);
        int valorC = valor_atributo(cartaC, escolha);

        printf("\nComputador jogou:");
        mostrar_carta(cartaC);

        printf("\nAtributo escolhido: %d\n", escolha);
        printf("%s: %d  vs  %s: %d\n", cartaJ.nome, valorJ, cartaC.nome, valorC);

        // ======== RESULTADO DA RODADA ========
        if (valorJ > valorC) {
            printf("\n🎉 Você venceu esta rodada!\n");
            jogador[qtdJogador++] = cartaJ;
            jogador[qtdJogador++] = cartaC;
            for (int i = 1; i < qtdJogador - 2; i++) jogador[i - 1] = jogador[i];
            for (int i = 1; i < qtdComputador; i++) computador[i - 1] = computador[i];
            qtdComputador--;
            vezDoJogador = 1;
        } else if (valorJ < valorC) {
            printf("\n💀 O computador venceu esta rodada!\n");
            computador[qtdComputador++] = cartaC;
            computador[qtdComputador++] = cartaJ;
            for (int i = 1; i < qtdComputador - 2; i++) computador[i - 1] = computador[i];
            for (int i = 1; i < qtdJogador; i++) jogador[i - 1] = jogador[i];
            qtdJogador--;
            vezDoJogador = 0;
        } else {
            printf("\n⚖️ Empate! As cartas voltam para o fim dos baralhos.\n");
            jogador[qtdJogador++] = cartaJ;
            computador[qtdComputador++] = cartaC;
            for (int i = 1; i < qtdJogador - 1; i++) jogador[i - 1] = jogador[i];
            for (int i = 1; i < qtdComputador - 1; i++) computador[i - 1] = computador[i];
        }

        printf("\nCartas restantes: Você = %d | Computador = %d\n", qtdJogador, qtdComputador);
    }

    // ======== FIM DO JOGO ========
    printf("\n===== FIM DE JOGO =====\n");
    if (qtdJogador > 0)
        printf("🏆 Você venceu o Super Trunfo!\n");
    else
        printf("💀 O computador venceu o Super Trunfo!\n");
}

// ======== MAIN ========

int main() {
    srand(time(NULL));
    jogar_super_trunfo();
    return 0;
}

