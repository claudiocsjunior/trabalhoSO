import os
import time
import signal


def filho():
   os._exit(0)  

def pai(filhos):
    for x in range(0, 4):
        novoPID = os.fork()
        if novoPID == 0:
            filho()
        else:
            pids = (os.getpid(), novoPID)
            filhos.append(novoPID)
            print("Pai: %d, filho: %d\n" % pids)
    return filhos
            
    
def printar_filhos(filhos):
    print(filhos)

#comando para listar os filhos: ps --ppid PID_DO_PAI
filhos = [] 
filhos = pai(filhos)
while True:
    resultado = input(" s - suicidar \n k - matar um processo \n l - listar processos filhos\n")
    if resultado == 'k': 
        printar_filhos(filhos)  
        idFilho = input("\nInforme o processo que quer matar:\n")
        if(int(idFilho) in filhos):
            #os.kill(int(idFilho), signal.SIGKILL)
            os.waitpid(int(idFilho),9)
            filhos.remove(int(idFilho))
            print('\nFilho removido com sucesso.')
        else:
            print('\nId não encontrado. Tente novamente.')
        continue
    elif resultado == 'l':
        printar_filhos(filhos)    
        continue
    else:
        break




