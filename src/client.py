import socket

# Greeting message
print("Welcome to POKERSIM CLIENT Program!\n")
print("Game mode: Single Player vs. Dealer\n")
print("Game information: SB 10, BB 20, dealer's buy-in 2000\n")

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
    connection_confirm_message = s.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
print(connection_confirm_message)

# [C2] Send player name to server
player_name = input("Player name: ")
try:
    s.send(player_name.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [C3] Send player buy in amount
player_buy_in = input("Buy in amount (1000-5000): ")
try:
    s.send(player_buy_in.encode())
except socket.error as err:
    print("socket send failed with error %s" %(err))

# [C4] Receive game start message
try:
    game_start_message = s.recv(1024).decode()
except socket.error as err:
    print("socket recv failed with error %s" %(err))
print(game_start_message)

is_quit = False
while not is_quit:
    # [C5] Receive hand first card
    try:
        hand_first_card = s.recv(1024).decode()
    except socket.error as err:
        print("socket recv failed with error %s" %(err))

    # [C6] Receive hand second card
    try:
        hand_second_card = s.recv(1024).decode()
    except socket.error as err:
        print("socket recv failed with error %s" %(err))

    # Prompt for quitting
    status = input("Do you want to continue? [Y/n]")
    if status == "" or status == "Y" or status == "y":
        is_quit = False
    elif status == "N" or status == "n":
        is_quit = True
    else:
        print("Type again!")

    # [CQ] Send quit status
    try:
        if is_quit:
            s.send("yes".encode())
        else:
            s.send("no".encode())
    except socket.error as err:
        print("socket send failed with error %s" %(err))




s.close()



