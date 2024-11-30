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
font = pg.font.SysFont('malgungothic', 16, True, False)  # None은 기본 폰트, 폰트 크기
color1 = (0, 0, 0)

# 변수들
day = 1
step = 0
choice = 0
choice2 = 0
percent = True
pers = 0
perb = False

m1_e1 = ["바람 한점 없는 조용한 밤, 간만에 거하게 달린 당신은 휘청이는 몸을 이끌고 집으로 향하는 길이였다.  신호등이 초록불로 바뀌자 저벅저벅 길을 건너는데 건너편에서 트럭 경적이 울린다. 얼핏보기에도 10톤은 족히 넘어보이는 트럭이 경적을 울리며 달려오는데 멈출 기미가 보이질 않는다. 어떻게 해야할까?", 
       "1. 몸을 날려 피한다.", 
       "2. 운명을 받아들이고 포기한다."]
m1_e211 = [" 몸을 있는 힘껏 날려보았지만 사람이 아무리 날래도 달려오는 트럭을 피할 수는 없었다.  마치 야구 배트에 맞은 야구공처럼 20m가량을 날라갔다. 온몸의 뼈가 으스러진 것만 같다. 살려달라고 소리치고 싶었지만 부러진 갈비뼈가 폐를 관통해 목소리가 나오지 않는다. 찢어진 이마에서 흐른 피가 시야를 가리더니 이내 눈앞이 깜깜해졌다", 
           "계속"]
m1_e212 = ["본능적으로 몸을 날려 트럭을 피했다. '내가 이정도의 반사신경이 있었나? 알코올이 날 각성시키기라도 한건가?'. 독백도 잠시 기사가 고래고래 소리치기 시작한다. '빨간 불에 차도로 걸어나오면 죽여달라고 환장한거야?? 멀쩡한 사람 인생 망치려고 작정했어???'  분명 초록불을 보고 건넜는데 저 기사가 무슨 헛소리를 하는 거지 싶던 것도 잠시 횡단보도의 초록불이 깜빡이기 시작한다. 당황스러움과 함께 취기가 날라갔다. '지금 초록불이 깜빡인다는건 아까 내가 본 초록불은..'  기사님께 재차 사과를 드리고 적당히 마셔야겠다는 생각과 함께 집으로 향했다.", 
          "(히든 엔딩 - 과음은 위험해) "]
m1_e221 = ["경적을 울리며 빠른 속도로 달려오는 트럭에 공포감에 휩싸였다. 어떻게 해야할지 잠시 고민했으나 내가 할 수 있는 것은 아무것도 없다고 깨달은 나는 이내 생각하는 것을 포기했다.  쿵 소리와 함께 내 몸이 바닥을 나뒹굴었다. 빨리 이 고통에서 해방되고 싶다는 생각만이 내 뇌를 지배했으며 그 생각도 잠시 이내 사망했다", 
           "계속"]
m1_e222 = ["끼이익 거리는 소리와 함께 트럭이 쭉 밀려 나오더니 다행히도 내 바로 앞에서 멈췄다. 트럭 기사가 차에서 내려 미쳤냐며 고래고래 소리를 지른다. 기사의 외침은 귀에 들어오지 않으며 살았다는 안도감만이 나를 감쌌다.  기사님께 죄송하다며 재차 사과를 드리고 떨리는 다리를 붙잡고 집으로 향했다.", 
           "(히든 엔딩 - 천운)"]
sub1 = ["서브이벤트 1입니다", 
       "1. ㅁㄴㅇㄹ", 
       "2. ㅁㄴㅇㄹ", 
       "3. ㅁㄴㄹ"]
ending_credit = ["결말에 도달하셨습니다. 즐겨주셔서 감사합니다"]



def main_e1():
       global day, step, choice, choice2, percent
       if step == 0:
              Text.output(m1_e1, cg[0])
       elif step == 1:
              if choice == 1:
                     choice2 = 1
                     if per(95, 1):
                            Text.output(m1_e211)
                     else:
                            percent = False
                            Text.output(m1_e212)
              elif choice == 2:
                     choice2 = 2
                     if per(95, 1):
                            Text.output(m1_e221)
                     else:
                            Text.output(m1_e222)
       elif step == 2:
              if choice2 == 1:
                     if percent:
                            next()
                     else:
                            Text.output(ending_credit)
              elif choice2 == 2:
                     if percent:
                            next()
                     else:
                            Text.output(ending_credit)
def main_e2():
       pass

def sub_e(number):
       if number == 1:
              if step == 0:
                     Text.output(sub1)
              elif step == 1:
                     if choice == 1:
                            choice2 = 1
                            Text.output(m1_e211)
                     elif choice == 2:
                            choice2 = 2
                            Text.output(m1_e212)
              elif step == 2:
                     next()
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
                            if text_surface.get_width() > 440:
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
                                   textrect.topleft = (20, 80 + i * font.get_height())
                                   if img != None and i == len(lines)-1:
                                          screen.blit(img, (120, 140 + i * font.get_height()))
                            else:
                                   textrect.topleft = (20, 720 - ((len(episode) - ind) * 40 + 50))
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

def per(r, seed):
       global pers, perb
       if pers == seed:
              return perb
       else:
              pers = seed
              perb = random.randint(1, 100) <= r
              return perb
def next():
       global day, step
       day += 1
       step = 0
       choice = 0
       choice2 = 0  
asdf
asdf
