from setup import *
import socket

# Greeting message
print("Welcome to POKERSIM SERVER Program!\n")
print("Game mode: Single Player vs. Dealer\n")

# Create a socket object
port = 12345
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("socket creation failed with error %s" %(err))

# Bind to the port
try:
    s.bind(('', port))
except socket.error as err:
    print("socket bind failed with error %s" %(err))

# Now wait for client connection.
try :
    s.listen(5)
except socket.error as err:
    print("socket listen failed with error %s" %(err))

# [S0] Establish connection with client.
try:
    c, addr = s.accept()
except socket.error as err:
    print("socket accept failed with error %s" %(err))

# [S1] Send connection confirmation message
connectionConfirmMessage = "Connected to Server\n"
try:
    c.send(connectionConfirmMessage.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [S2] Receive player name from client
try:
    playerName = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
    
# [S3] Receive player buy in amount
try:
    playerBuyIn = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))

print("Player " + playerName + " joined with " + playerBuyIn + " buy in ["+ str(addr[1]) + "]\n")

# Initialize game
game = Game()

clientPlayer = Player(playerName)
game.add_player(clientPlayer)

dealerPlayer = Player("Dealer")
game.add_player(dealerPlayer)

game.init_blinds(10, 20)

# [S4] Send game start message
gameStartMessage = "The game starts now!\n"
try:
    c.send(gameStartMessage.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

finally:
    s.close()
    c.close()







