import socket, sys
    
def inciar():
    print ("=" * 60)
    print ("[+] Criado por roldan01 [+]")
    print ("=" * 60)
inciar() 

server = input("Digite o host que deseja fazer o scan: ")
serverip = socket.gethostbyname(server)    

print ("=" * 60)
print ("Scan no host: ", server)
print ("=" * 60)

try:
    for port in range(1,65535):
            mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if mysock.connect_ex((serverip,port)) == 0:
                print ("Porta {}: aberta.".format, port)
    mysock.close()
except KeyboardInterrupt:
    print("Cancelado.")
    sys.exit()
except socket.gaierror:
    print("Host não encontrado.")
except socket.error:
    print("Não conseguimos nos conectar ao server.")
