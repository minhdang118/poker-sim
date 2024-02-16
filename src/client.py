import socket

print("Welcome to POKERSIM CLIENT Program!\n")
print("Game mode: Single Player vs. Dealer\n")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("socket creation failed with error %s" %(err))

port = 12345

try:
    s.connect(('127.0.0.1', port))
except socket.error as err:
    print("socket connect failed with error %s" %(err))

try:
    connectionConfirmMessage = s.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
print(connectionConfirmMessage)

playerName = input("Player name: ")
try:
    s.send(playerName.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

try:
    gameStartMessage = s.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
print(gameStartMessage)

s.close()



