frase = 'Gostaria muito de ter uma chance de trabalhar com vocês!'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
quantidade_de_as = frase.count('a')
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
print(f"A letra 'a' aparece {quantidade_de_as} vezes na string.")