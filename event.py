import pygame as pg
import random
import time

# 파이게임 세팅
pg.init()
screen = pg.display.set_mode((480,720))
# 파이게임 창 이름
pg.display.set_caption("IK")

# 배경 이미지
background_path = ['background/background.png']
background = []
for path in  background_path:
    background.append(pg.image.load(path))
# cg 이미지
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
choi = [1] * 10

pers = 0
perb = False
nums = 0
numb = False
sub_number = 0

# 메인 1-1 텍스트
m1_e1 = ["바람 한점 없는 조용한 밤, 간만에 거하게 달린 당신은 휘청이는 몸을 이끌고 집으로 향하는 길이였다.  신호등이 초록불로 바뀌자 저벅저벅 길을 건너는데 건너편에서 트럭 경적이 울린다. 얼핏보기에도 10톤은 족히 넘어보이는 트럭이 경적을 울리며 달려오는데 멈출 기미가 보이질 않는다. 어떻게 해야할까?", 
       "몸을 날려 피한다.", 
       "운명을 받아들이고 포기한다."]
m1_e111 = [" 몸을 있는 힘껏 날려보았지만 사람이 아무리 날래도 달려오는 트럭을 피할 수는 없었다.  마치 야구 배트에 맞은 야구공처럼 20m가량을 날라갔다. 온몸의 뼈가 으스러진 것만 같다. 살려달라고 소리치고 싶었지만 부러진 갈비뼈가 폐를 관통해 목소리가 나오지 않는다. 찢어진 이마에서 흐른 피가 시야를 가리더니 이내 눈앞이 깜깜해졌다", 
           "계속"]
m1_e112 = ["본능적으로 몸을 날려 트럭을 피했다. '내가 이정도의 반사신경이 있었나? 알코올이 날 각성시키기라도 한건가?'. 독백도 잠시 기사가 고래고래 소리치기 시작한다. '빨간 불에 차도로 걸어나오면 죽여달라고 환장한거야?? 멀쩡한 사람 인생 망치려고 작정했어???'  분명 초록불을 보고 건넜는데 저 기사가 무슨 헛소리를 하는 거지 싶던 것도 잠시 횡단보도의 초록불이 깜빡이기 시작한다. 당황스러움과 함께 취기가 날라갔다. '지금 초록불이 깜빡인다는건 아까 내가 본 초록불은..'  기사님께 재차 사과를 드리고 적당히 마셔야겠다는 생각과 함께 집으로 향했다.", 
          "(히든 엔딩 - 과음은 위험해) "]
m1_e121 = ["경적을 울리며 빠른 속도로 달려오는 트럭에 공포감에 휩싸였다. 어떻게 해야할지 잠시 고민했으나 내가 할 수 있는 것은 아무것도 없다고 깨달은 나는 이내 생각하는 것을 포기했다.  쿵 소리와 함께 내 몸이 바닥을 나뒹굴었다. 빨리 이 고통에서 해방되고 싶다는 생각만이 내 뇌를 지배했으며 그 생각도 잠시 이내 사망했다", 
           "계속"]
m1_e122 = ["끼이익 거리는 소리와 함께 트럭이 쭉 밀려 나오더니 다행히도 내 바로 앞에서 멈췄다. 트럭 기사가 차에서 내려 미쳤냐며 고래고래 소리를 지른다. 기사의 외침은 귀에 들어오지 않으며 살았다는 안도감만이 나를 감쌌다.  기사님께 죄송하다며 재차 사과를 드리고 떨리는 다리를 붙잡고 집으로 향했다.", 
           "(히든 엔딩 - 천운)"]

# 메인 1-2 텍스트
m1_e2 = ["퇴근 후 시원하게 맥주나 한잔 할까하고 편의점으로 향했다. 해외맥주 네캔과 간단한 안주거리를 사고 머 보면서 먹을까 하는 행복한 고민을 하면서 집으로 향하던 중 자꾸만 수상한 시선이 느껴진다. 착각인가 싶다가도 왠지 모른 공포를 느낀 나는 조금은 빠르게 걸음을 내딪었는데 뒤에서 누군가가 나를 쫓아오고 있음을 직감했다. 어떻게 해야할까?", 
         "전력을 다해 도망친다.", 
         "뒤돌아 대면한다."]
m1_e211 = ["젖먹던 힘을 다해 뛰기 시작했다. 폐가 찢어지는 것만 같았지만 도망치지 못한다면 내가 찢어질 수 있다고 생각이 든 나는 죽어라 도망쳤다. 따돌렸나 하고 안도의 한숨을 쉬는 찰나 칼이 내 복부를 관통하더니 새빨간 피가 쏟아지기 시작했다. 녀석은 내 배에 박힌 칼을 뽑아 수차례 다시 내 배를 찔렀다. 소리를 질러봤지만 몇 마디 외치지도 못한체 과다출혈로 사망했다.", 
           "계속"]
m1_e212 = ["너무 무서운 나머지 뒤도 안돌아보고 미친듯이 뛰기 시작했다. 하지만 그 녀석도 나를 죽어라 쫓아왔다. 제발 쫓아오지마라고 비명을 지르며 도망치는데 그 때 뒤에서 그 녀석이 소리쳤다. '아니 아저씨, 지갑 떨어뜨리셨어요!! 지갑 가져가시라고!!' 그 녀석은 살짝 비웃는듯한 웃음을 보이며 지갑을 건네주고는 사라졌다. 부끄러워서 쥐구멍에라도 숨고싶었지만 이내 아무일도 아니였다는 안도감이 날 감쌌다.", 
           "(히든 엔딩 - 아니 아재요..)"]
m1_e221 = ["내가 뒤돌아보자 그 녀석은 움찔하더니 묘한 기류가 흐르기 시작했다. '혹시 왜 쫓아오시나요? 용건이라도 있으신가요?' 괜히 겁이 났던 나는 목소리에 빠짝 힘을 주고서 물어봤다. 아무런 답도 하지 않더니 이내 성큼성큼 걸어왔다. 눈치채지도 못한 사이 칼이 내 복부를 관통했다. 배에 박힌 칼을 비틀고는 고통에 몸부림치는 내 표정을 보며 비릿한 웃음을 짓는다. 온몸을 짓누르는 공포도 잠시 이내 과다출혈로 사망했다.", 
           "계속"]


sub1_e1 = ['당신은 숲을 건너다 수염이 덥수룩한 남성이 불을 피우고 ', 
       "1. 다가간다", 
       "2. 공격한다", 
       "3. 무시한다"]
sub1_e111 = ["그곳에는 작은 토끼가 숨어있었습니다. 하얀털에 붉은 눈을 가지고 이마에 뿔이 나있는 토끼는 그저 당신을 바라볼 뿐이였습니다. 당신은 고민에 빠졌습니다.", 
             "공격한다", 
             "풀어준다"]
sub1_e11111 = ['토끼늰 엄청난 움직임으로 당신의 검을 피했습니다. ']
sub1_e121 = ['"느려" 토끼는 순식간에 달려들어 당신의 목을 노렸습니다. 머리에 나있는 뿔은 작으나 공격당하면 피해는 적지 않을 것입니다.', 
             '왼쪽으로 피한다', 
             '오른쪽으로 피한다']


ending_credit = ["결말에 도달하셨습니다. 즐겨주셔서 감사합니다"]

def main_e1():
       # step은 단계 output에서 선택할 때마다 알아서 증가시켜줌
       # output(텍스트 리스트, chi번호, cg 번호, 배경이미지 번호) choi, cg는 생략가능, choi 생략시 기본값 0
       if step >= 0:
              output(m1_e1, 0, 0)
              if step >= 1:
                     if choi[0] == 1:
                            # per(확률, 시드값) 시드값이 같으면 같은 결과가 나옴. 다른곳에서 쓸시 다른 값 사용. 물론 날짜 넘어가면 초기화됨
                            if per(95, 1):
                                   output(m1_e111, 1)
                                   if step >= 2:
                                          if choi[1] == 1:
                                                 # 다음날로 넘어가고 변수 다 초기화됨
                                                 next()
                            else:
                                   output(m1_e112)
                                   if step >= 2:
                                          end()
                     else:
                            if per(95, 2):
                                   output(m1_e121)
                                   if step >= 2:
                                          if choi[1] == 1:
                                                 next()
                            else:
                                   output(m1_e122)
                                   if step >= 2:
                                          end()

def sub_e(number):
       if number == 1:
              if step >= 0:
                     output(sub1_e1)
                     if step >= 1:
                            if choi[0] == 1:
                                   output(sub1_e111)
                            

def output(episode, choin = 0, cg_n = None, background_n = 0):
       global day, step, choi
       screen.blit(background[background_n], (0, 80))
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
                            textrect.topleft = (20, 100 + i * font.get_height())
                            if cg_n != None and i == len(lines)-1:
                                   screen.blit(cg[cg_n], (120, 140 + i * font.get_height()))
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
                                          print(choin)
                                          choi[choin] = ind
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
# 랜덤 숫자용 함수
def randnum(low, big, seed):
       global nums, numb
       if nums == seed:
              return numb
       else:
              nums = seed
              perb = random.randint(low, big)
              return perb
def next():
       global day, step, choi, sub_number
       day += 1
       step = 0
       choi = [1] * 10
       per(1, 999)
       sub_number = random.randint(1, 8)
def end():
       output(ending_credit)
