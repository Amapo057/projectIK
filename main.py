# projectIK
import pygame as pg
import event as ev
import random

# 이미지 불러오기
background_path = ['background/background.png']
# 이미지 넣기
background = []
for path in  background_path:
    background.append(pg.image.load(path))

# 기본 변수
PLAY = True
r = 0

while PLAY:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            PLAY = False

    ev.screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기
    ev.screen.blit(background[0], (0, 0))

    if ev.day <= 1:
        ev.main_e1()
        r = random.randint(1, 8)
    elif ev.day == 4:
        ev.main_e2()
        print("ev.day4")
    elif ev.day == 7:
        ev.main_e1()
        print("ev.day7")
    elif ev.day == 10:
        ev.main_e1()
    else:
        ev.sub_e(1)

    pg.display.flip()  # 화면 업데이트

pg.quit()