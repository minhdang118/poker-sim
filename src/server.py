from setup import Game
import socket

print("Welcome to PokerSim Server Program!")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.bind(('', port))

game = Game()

