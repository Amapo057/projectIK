# projectIK
import pygame as pg
import event as ev

# 기본 변수
PLAY = True
day = 1

while PLAY:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            PLAY = False

    ev.screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기

    # 텍스트 출력
    ev.main_e1()

    pg.display.flip()  # 화면 업데이트

pg.quit()
