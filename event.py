import pygame as pg
import random

# 파이게임 세팅
pg.init()
screen = pg.display.set_mode((480,720))
# 파이게임 창 이름
pg.display.set_caption("IK")

# 폰트 설정
# 폰트 확인
# for i in pg.font.get_fonts():
#     print(i)
font = pg.font.SysFont('malgungothic', 20, True, False)  # None은 기본 폰트, 폰트 크기
color1 = (255, 255, 255)

ep1 = ["이것은 지문부분입니다. 지문은 알아서 줄바꿈 후 출력됩니다. 띄어쓰기를 잘 인식하는지 테스트하는 용도", 
       "1. 코드", 
       "2. 문장", 
       "3. 차기"]

def main_e1():
    text_out(ep1)

def text_out(episode):
    for ind, ep in enumerate(episode):
       words = ep.split(' ')
       lines = []
       current_line = []
       for word in words:
              # 라인에 단어 추가
              current_line.append(word)
              # 문자열 길이 측정위해 렌더
              text_surface = font.render(' '.join(current_line), True, color1)
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
              textobj = font.render(line, True, color1)
              # 물체 만들기? rect가 rectangle의 약자. 사각형 물체 만든다고 보면됨
              textrect = textobj.get_rect()
              # x좌표, y좌표로 위치 잡음 y좌표는 for문이 반복할 때 마다 높이만큼 증가
              if ind == 0:
                     textrect.topleft = (20, 20 + i * font.get_height())
              else:
                    textrect.topleft = (20, 500 + (ind * 50))
              # 화면에 출력
              screen.blit(textobj, textrect)
                  