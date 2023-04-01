resp = 'S'
soma = quant = Média = maior = menor =0
while resp in 'Ss':
    núm = int(input('Digite um número:' ))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior :
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
Média = soma / quant
print('Voçé digitou {} números é a Média foi {}'.format(quant,Média))
print('O maior valor foi {} é o menor foi {}'.format(maior,menor))