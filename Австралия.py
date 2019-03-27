import pygame
import requests
import sys
import os

map_request = "http://static-maps.yandex.ru/1.x/?ll=133.795384,-25.694768&spn=1.579285%2C0.518130&l=map"
response = requests.get(map_request)
map_file = "map.png"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)