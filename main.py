import os

fim = 0
jogadores = []

def percentualVotos(votos, totalVotos):
    percentual_votos = (votos / totalVotos) * 100
    return percentual_votos

print('Enquete: Quem foi o melhor jogador?')
while True:
    votos = int(input('Informe um valor entre 1 e 23 ou 0 para sair: '))
    jogadores.append(votos)
    
    if votos > 23:
        jogadores.remove(votos)
        print('Invalido. Digite um valor entre 1 e 23 ou 0 para sair.')
        
    if votos == fim:
        jogadores.remove(0)
        break

os.system('cls')
print('Resultado da votação:')

contagem_votos = {}
for jogador in jogadores:
    if jogador in contagem_votos:
        contagem_votos[jogador] += 1
    else:
        contagem_votos[jogador] = 1

total_votos = len(jogadores)
print(f'\nForam computados {total_votos} votos.\n')


with open('resultado_votacao.txt', 'w') as arquivo:
    for jogador, total_votos_jogador in contagem_votos.items():
        resultado_percentual = percentualVotos(total_votos_jogador, total_votos)
        
        print(f'Jogador {jogador}:      {total_votos_jogador}        {resultado_percentual:.2f}%')

        arquivo.write(f'Jogador {jogador}: {total_votos_jogador} votos, {resultado_percentual:.2f}%\n')