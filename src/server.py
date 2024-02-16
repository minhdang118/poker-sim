from setup import *
import socket

game = Game()

print("Welcome to POKERSIM SERVER Program!\n")
print("Game mode: Single Player vs. Dealer\n")
port = 12345

try :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("socket creation failed with error %s" %(err))

try:
    s.bind(('', port))
except socket.error as err:
    print("socket bind failed with error %s" %(err))

try :
    s.listen(5)
except socket.error as err:
    print("socket listen failed with error %s" %(err))

try:
    c, addr = s.accept()
except socket.error as err:
    print("socket accept failed with error %s" %(err))

connectionConfirmMessage = "Connected to Server\n"
try:
    c.send(connectionConfirmMessage.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

try:
    playerName = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))

print("Player " + playerName + " connected from port " + str(addr[1]) + "\n")

clientPlayer = Player(playerName)
game.add_player(clientPlayer)

dealerPlayer = Player("Dealer")
game.add_player(dealerPlayer)

gameStartMessage = "The game starts now!\n"
try:
    c.send(gameStartMessage.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

finally:
    s.close()
    c.close()







