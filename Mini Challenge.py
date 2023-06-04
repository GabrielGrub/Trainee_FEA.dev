import random

# Lista de tuplas com o nome dos novos membros e os seus respectivos números que representam ter ou não feito o Curso de Python do FEA.Dev
os_melhores_trainees_do_mundo = [
    ("Adriel Faustino de Oliveira", 0),
    ("Amanda Emi Yamasaki", 0),
    ("Ana Werneck de Souza Dias", 0),
    ("André Menniti Pennini", 1),
    ("Felipe de Souza Lourenço", 0),
    ("Fernanda Mayumi Sakamoto Iizuka", 0),
    ("Fernanda Mees Antunes", 1),
    ("Gabriel Grub Vidal da Silva", 1),
    ("Guilherme Vinicius Afonso Dias de Freitas", 0),
    ("Henrique Nogueira Pedro Lindoso", 1),
    ("Kim Ju Hyang", 0),
    ("Leticia Amy Siramidu", 0),
    ("Marcelo Tamay Honda", 0),
    ("Maria Dulce Navarro de Britto Matos", 0),
    ("Mateus Pamio Forcione de Oliveira e Souza", 0),
    ("Milena da Silva Ramos", 0),
    ("Paulo Sergio Almeida de Oliveira", 0),
    ("Theo Borten Radesca Migliano", 0),
    ("Vitor Tatiama Gouveia", 0)
]

# Usando o for para separar os membros que fizeram o Curso de Python dos que não fizeram, colocando os nomes em duas listas distintas
curso_de_python_ON = [m for m in os_melhores_trainees_do_mundo if m[1] == 1]
curso_de_python_OFF = [m for m in os_melhores_trainees_do_mundo if m[1] == 0]

# Usei o método shuffle para embaralhar as duas listas que foram criadas
random.shuffle(curso_de_python_ON)
random.shuffle(curso_de_python_OFF)


# Dividi os membros em grupos usando os índices para garantir que não vai acontecer repetições de nomes e que todos os grupos teram 1 e apenas 1 membro que fez o Curso de Python 
grupos = [
    curso_de_python_OFF[:4] + curso_de_python_ON[:1],
    curso_de_python_OFF[4:8] + curso_de_python_ON[1:2],
    curso_de_python_OFF[8:12] + curso_de_python_ON[2:3],
    curso_de_python_OFF[12:] + curso_de_python_ON[3:4]
]

# Imprimindo os grupos e os seus respetivos membros de forma bonitinha 🥰
for i in range(len(grupos)):
    print('\033[1m'"Grupo", i+1,'\033[0m')
    for nome in grupos[i]:
        print(nome[0])
    print()