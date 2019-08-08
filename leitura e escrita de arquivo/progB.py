arquivo = open('arquivo.txt', 'r')
texto = arquivo.read()
arquivo.close
if(texto != ""):
    print(texto)

arquivo = open('arquivo.txt', 'w')
arquivo.write('Olá A')
arquivo.close