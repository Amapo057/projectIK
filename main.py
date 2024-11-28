# projectIK
import pygame as pg
import event as ev

# 기본 변수
PLAY = True

rect = 0

while PLAY:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            PLAY = False

    ev.screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기
    print(ev.day)

    if ev.day <= 1:
        rect = ev.main_e1()
    elif ev.day == 2:
        ev.main_e1()
        print("ev.day4")
    elif ev.day == 7:
        ev.main_e1()
        print("ev.day7")
    elif ev.day == 10:
        ev.main_e1()
    else:
        ev.sub_e()

    pg.display.flip()  # 화면 업데이트

pg.quit()
