import http.server
import socketserver
import os

PORT = 8000  # Sunucunun çalışacağı port numarasını belirleyin
DIRECTORY = "Artun Site"  # Sunucunun kök dizini olarak kullanılacak dizini belirleyin

Handler = http.server.SimpleHTTPRequestHandler
os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Sunucu {} portunda başlatıldı...".format(PORT))
    httpd.serve_forever()

import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()