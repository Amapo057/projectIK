import pygame as pg
import random

# 파이게임 세팅
pg.init()
screen = pg.display.set_mode((480,720))
# 파이게임 창 이름
pg.display.set_caption("IK")

# 이미지
cg_path = ['cg/truck.png']
cg = []
for i, path in enumerate(cg_path):
    cg.append(pg.image.load(path))
    cg[i].set_alpha(220)

# 폰트 설정
# 폰트 확인
# for i in pg.font.get_fonts():
#     print(i)
font = pg.font.SysFont('malgungothic', 20, True, False)  # None은 기본 폰트, 폰트 크기
color1 = (0, 0, 0)

# 변수들
day = 1
step = 0
choice = 0
choice2 = 0

m1_e1 = ["트럭이 당신을 향해 달려온다. 어떻게 해야할까 ", 
       "1. 피한다", 
       "2. 포기한다"]
m1_e21 = ["당신은 결국 트럭를 피하지 못했습니다. 이또한 운명이겠지요", 
           "계속"]
m1_e22 = ["당신은 가까스로 트럭를 피했습니다. 뛰어난 반사신경, 운동실력, 그리고 운이 결합된 결과일 것입니다", 
          "1. 트럭 기사에게 따진다", 
          "2. 운이 좋았다 생각하고 집으로 돌아간다"]
ep3 = ["서브이벤트 입니다 줄바꿈 테스트 중 줄바 꿈 이이이잉 앗쌀라마라이꿍", 
       "1. ㅁㄴㅇㄹ", 
       "2. ㅁㄴㅇㄹ", 
       "3. ㅁㄴㄹ"]



def main_e1():
       global day, step, choice, choice2
       if step == 0:
              Text.output(m1_e1, cg[0])
       elif step == 1:
              if choice == 1:
                     Text.output(m1_e21)
                     choice2 = 1
              elif choice == 2:
                     Text.output(m1_e22)
                     choice2 = 2
       elif step == 2:
              if choice2 == 1:
                     next()
              elif choice2 == 2:
                     Text.output(ep3)
def main_e2():
       global day, step, choice, choice2
       if step == 0:
              Text.output(m1_e1, cg[0])
       elif step == 1:
              if choice == 1:
                     Text.output(m1_e21)
                     choice2 = 1
              elif choice == 2:
                     Text.output(m1_e22)
                     choice2 = 2
       elif step == 2:
              if choice2 == 1:
                     next()
              elif choice2 == 2:
                     Text.output(ep3)
       

       
                     
class Text:
       def output(episode = None, img = None):
              global day, step, choice
              selected_rect = None
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
                                   textrect.topleft = (50, 80 + i * font.get_height())
                                   if img != None and i == len(lines)-1:
                                          screen.blit(img, (120, 140 + i * font.get_height()))
                            else:
                                   textrect.topleft = (50, 720 - ((len(episode) - ind) * 40 + 50))
                            # 화면에 출력
                            screen.blit(textobj, textrect)

                            if ind != 0 and textrect.collidepoint(pg.mouse.get_pos()):
                                   selected_rect = textrect
                     if selected_rect:
                            highlight(selected_rect)
                            for event in pg.event.get():
                                   if event.type == pg.MOUSEBUTTONDOWN:
                                          if selected_rect.collidepoint(event.pos):
                                                 choice = ind
                                                 print("click")
                                                 step += 1
def highlight(rec):
      pg.draw.rect(screen, color1, rec, 2)

def per(r):
       return random.randint(1, 100) >= r      
    
def next():
       global day, step
       day += 1
       step = 0
       choice = 0
       choice2 = 0  