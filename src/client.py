import socket

# Greeting message
print("Welcome to POKERSIM CLIENT Program!\n")
print("Game mode: Single Player vs. Dealer\n")

# Create a socket object
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("socket creation failed with error %s" %(err))

# [C0] Connect to the server
port = 12345
try:
    s.connect(('127.0.0.1', port))
except socket.error as err:
    print("socket connect failed with error %s" %(err))

# [C1] Receive connection confirmation message
try:
    connectionConfirmMessage = s.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
print(connectionConfirmMessage)

# [C2] Send player name to server
playerName = input("Player name: ")
try:
    s.send(playerName.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [C3] Send player buy in amount
playerBuyIn = input("Buy in amount (1000-5000, SB 10, BB 20): ")
try:
    s.send(playerBuyIn.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [C4] Receive game start message
try:
    gameStartMessage = s.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
print(gameStartMessage)

s.close()



