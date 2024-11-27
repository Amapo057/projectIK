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
font = pg.font.SysFont("malgungothic", 20)  # None은 기본 폰트, 폰트 크기
white = (255, 255, 255)
for i in pg.font.get_fonts():
    print(i)

def text_out(text):
    global font, white, screen
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        # 라인에 단어 추가
        current_line.append(word)
        # 문자열 길이 측정위해 렌더
        text_surface = font.render(' '.join(current_line), True, white)
        # 길이 측정 후 라인스에 넣기
        if text_surface.get_width() > 450:
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]
    # 남은 짜투리 넣음
    if current_line:
        lines.append(' '.join(current_line))
    # 실제 문자열 한줄씩 출력. i는 인덱스, line은 문자열 들어감
    for i, line in enumerate(lines):
        # 문자열 렌더
        textobj = font.render(line, True, white)
        # 물체 만들기? rect가 rectangle의 약자. 사각형 물체 만든다고 보면됨
        textrect = textobj.get_rect()
        # x좌표, y좌표로 위치 잡음 y좌표는 for문이 반복할 때 마다 높이만큼 증가
        textrect.topleft = (20, 20 + i * font.get_height())
        # 화면에 출력
        screen.blit(textobj, textrect)

while PLAY:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            PLAY = False

    screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기

    # 텍스트 출력
    multiline_text = "개미친 김정은이 핵미사일을 광주에 떨궈서 그 여파로 난장판이 된 순천에서 살아남는 스토리 제한시간 6일동안 도시를 돌아다니며 물자를 획득 후 집으로 돌아와야됨"
    text_out(multiline_text)

    pg.display.flip()  # 화면 업데이트

pg.quit()
