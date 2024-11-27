# projectIK
import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((480,720))
pg.display.set_caption("IK")

# 폰트 설정
font = pg.font.Font(None, 20)  # None은 기본 폰트, 36은 폰트 크기

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기

    # 텍스트 출력
    draw_text('Welcome to the Text RPG!', font, (255, 255, 255), screen, 20, 20)
    draw_text('Press any key to start.', font, (255, 255, 255), screen, 20, 60)

    pg.display.flip()  # 화면 업데이트

pg.quit()
