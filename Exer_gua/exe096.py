def area(l, c):
    a = l*c
    print(f'A area de um terreno {l}x{c} é de {a}m²')
    

#programa principal    
print('DESCUBRA A AREA DO SEU TERRENO!')
while True:
    alt = 't'
    area(float(input('Digite a largura do terreno: ')), float(input('Digite o comprimento do terreno: ')))
    while alt not in 'SN':
        alt = str(input('Deseja colocar novos valores? [S/N]')).upper().strip()[0]
    if alt == 'N':
        break
