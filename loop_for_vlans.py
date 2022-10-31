import getpass
import telnetlib

HOST = "10.100.1.1"
user = input("Digite o seu usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"conf t\n")
#Laco FOR
for vlans in range (10,15):
    tn.write(b"vlan " + str(vlans).encode('ascii') + b"\n")
    tn.write(b"name Rede_Lan_" + str(vlans).encode('ascii') + b"\n")


tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
