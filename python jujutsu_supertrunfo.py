import random

# ======== DADOS DAS CARTAS ========
# Dados das cartas
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
