import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

x = W // 2
y = H // 2
kdsx = 150
kdsy = 150
speed_x = 0
speed_y = 0
delta_speed_x = 0.1
delta_speed_y = 0.1

flRunning = True
f = pygame.font.Font(None, 20)
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

    keys = pygame.key.get_pressed()
    dsx = round(((W / 2) - x) / kdsx, 2)
    dsy = round(((H / 2) - y) / kdsy, 2)

    if keys[pygame.K_LEFT]:
        speed_x -= delta_speed_x
    elif keys[pygame.K_RIGHT]:
        speed_x += delta_speed_x
    else:
        speed_x = (speed_x + dsx) * abs(dsx)

    if keys[pygame.K_UP]:
        speed_y -= delta_speed_y
    elif keys[pygame.K_DOWN]:
        speed_y += delta_speed_y
    else:
        speed_y = (speed_y + dsy) * abs(dsy)
    if x < 0:
        x = 0
        speed_x = 0
    elif x > W - 10:
        x = W - 10
        speed_x = 0

    if y < 0:
        y = 0
        speed_y = 0
    elif y > H - 20:
        y = H - 20
        speed_y = 0

    x += speed_x
    y += speed_y

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()
    clock.tick(FPS)

