import getpass
import telnetlib

user = input("Digite o seu usuario: ")
password = getpass.getpass()

#ACESSA LISTA DE IPS
ip_routers = open ('routers_ip')

for ip in ip_routers:
    ip=ip.strip() #remove linha em branco da lista de ip
    print("Configurando Host " + ip)
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


    tn.write(b"conf t\n")
    tn.write(b"ip domain-name cisco.com\n")
    tn.write(b"crypto key generate rsa\n")
    #LEMBRE DE ALTERAR O TAMANHO DE BITS QUE VOCE PRECISA
    tn.write(b"1024\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

