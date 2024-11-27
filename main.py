# projectIK
import pygame as pg
import random

# 기본 변수
PLAY = True

# 파이게임 세팅
pg.init()
screen = pg.display.set_mode((480,720))
# 파이게임 창 이름
pg.display.set_caption("IK")

# 폰트 설정
font = pg.font.Font(None, 20)  # None은 기본 폰트, 폰트 크기
white = (255, 255, 255)

def text_out(text):
    global font, white, screen
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        # 라인에 단어 추가
        current_line.append(word)
        text_surface = font.render(' '.join(current_line), True, white)
        if text_surface.get_width() > 450:
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    for i, line in enumerate(lines):
        textobj = font.render(line, True, white)
        textrect = textobj.get_rect()
        textrect.topleft = (20, 20 + i * font.get_height())
        screen.blit(textobj, textrect)

while PLAY:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            PLAY = False

    screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기

    # 텍스트 출력
    
    multiline_text = "Welcome to the Text RPG! This is a new line.im fine tank you and you? hello world"
    text_out(multiline_text)

    pg.display.flip()  # 화면 업데이트

pg.quit()
