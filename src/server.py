from setup import *
import socket

# Greeting message
print("Welcome to POKERSIM SERVER Program!\n")
print("Game mode: Single Player vs. Dealer\n")
print("Game information: SB 10, BB 20, dealer's buy-in 2000\n")

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
connection_confirm_message = "Connected to Server\n"
try:
    c.send(connection_confirm_message.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [S2] Receive player name from client
try:
    player_name = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
    
# [S3] Receive player buy in amount
try:
    player_buy_in = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))

print("Player " + player_name + " joined with " + player_buy_in + " buy in ["+ str(addr[1]) + "]\n")

# Initialize game
game = Game()

# Add players and set up buy-ins
dealer_player = Player("Dealer")
game.add_player(dealer_player)
game.table.players[0].buy_in(2000)

client_player = Player(player_name)
game.add_player(client_player)
game.table.players[1].buy_in(int(player_buy_in))

# Set blinds
game.set_blinds(10, 20)
game.init_blinds()

# [S4] Send game start message
game_start_message = "\nThe game starts now!\n"
try:
    c.send(game_start_message.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [S5] Receive game start confirmation
try:
    game_start_confirmation = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))

is_quit = False

# while not is_quit:

# Deal hands
game.deal_hands()
game.set_action()

# [S6] Send player hand first card
player_hand_first_card = game.table.players[1].hand[0].to_string()
try:
    c.send(player_hand_first_card.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [S7] Receive player hand first card confirmation
try:
    player_hand_first_card_confirmation = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))

# [S8] Send player hand second card
player_hand_second_card = game.table.players[1].hand[1].to_string()
try:
    c.send(player_hand_second_card.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [S9] Receive player hand second card confirmation
try:
    player_hand_second_card_confirmation = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))

# [SQ] Receive quit status
try:
    is_quit = c.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))








s.close()
c.close()







