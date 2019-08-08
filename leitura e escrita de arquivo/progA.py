arquivo = open('arquivo.txt', 'r')
texto = arquivo.read()
if(texto != ''):
    print(texto)

print('Olá B')    
arquivo.close