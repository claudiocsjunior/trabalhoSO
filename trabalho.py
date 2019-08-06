import os


def child():
   os._exit(0)  

def parent():
    childs = [] 
    
    for x in range(0, 4):
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            childs.append(newpid)
            print("parent: %d, child: %d\n" % pids)
    
def printar_filhos(filhos)
    print(filhos)




    while True:
        reply = input("q for quit / c for new fork\n")
        if reply == 'c': 
            continue
        else:
            break

parent()


