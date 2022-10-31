import getpass
import telnetlib

user = input("Digite o seu usuario: ")
password = getpass.getpass()

ip_routers = open ('routers_ip')

for ip in ip_routers:
    ip=ip.strip() #remove linha em branco da lista de ip
    print("Realizando backup do Router: " + ip)
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show runn\n")
    tn.write(b"exit\n")

    ler_config = tn.read_all()
    save_config = open('backup-' + HOST, 'w')
    save_config.write(ler_config.decode('ascii'))
    save_config.write('\n')
    save_config.close

    print('Backup Completo')

    print(tn.read_all().decode('ascii'))
