# projectIK
import pygame as pg
import event as ev
import random

# 기본 변수
PLAY = True

while PLAY:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            PLAY = False

    if ev.day <= 1:
        ev.main_e1()
    elif ev.day == 4:
        ev.main_e2()
        print("ev.day4")
    elif ev.day == 7:
        ev.main_e1()
        print("ev.day7")
    elif ev.day == 10:
        ev.main_e1()
    else:
        # 다 만들어지면 숫자대신 ev.sub_number들어갈 예정
        ev.sub_e(1)

    pg.display.flip()  # 화면 업데이트

pg.quit()