import pygame
import sys
import random

pygame.init()

FPS = 60  # frame per second

mouse = {"x": None, "y": None}

# 도화지 준비
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
width, height = screen.get_size()
clock = pygame.time.Clock()


colors = [
    "#FC5D1C",
    "#FCA81C",
    "#FC851C",
    "#FC361C",
    "#FCC31C",
    "#FFB575",
]  # 동그라미 색깔을 저장할 리스트
circles = []  # 동그라미 정보를 저장할 리스트


# 동그라미 초기화
# 도화지에 그림을 그리기 전에 동그라미 정보를 리스트에 정하자 😊
def init(circle_count=200):
    for _ in range(circle_count):
        r = random.uniform(4, 8)  # 동그라미의 반지름
        min = r
        x = random.uniform(r, width - r)  # 동그라미의 x 좌표
        y = random.uniform(r, height - r)  # 동그라미의 y좌표
        c = random.choice(colors)  # 동그라미의 색깔
        dx = (random.random() - 0.5) * 4  # 동그라미의 x좌표 변화량
        dy = (random.random() - 0.5) * 4  # 동그라미의 y좌표 변화량
        c = {"r": r, "x": x, "y": y, "c": c, "dx": dx, "dy": dy, "min": min}
        circles.append(c)  # circles 리스트에 동그라미 정보(circle)를 추가


# 종료
def quit():
    print("종료")
    pygame.quit()
    sys.exit()


# 동그라미 이동 관련 함수
def move_circle(c):
    # 동그라미가 가로 벽에 부딪히면 방향을 바꾸기
    if c["x"] + c["r"] >= width or c["x"] - c["r"] <= 0:
        c["dx"] *= -1
    # 동그라미가 세로 벽에 부딪히면 방향을 바꾸기
    if c["y"] + c["r"] >= height or c["y"] - c["r"] <= 0:
        c["dy"] *= -1

    # 동그라미 좌표 변화
    c["x"] += c["dx"]
    c["y"] += c["dy"]


# 마우스와의 거리에 따른 동그라미 반지름 변화 함수
def react_to_mouse(c):
    if (
        mouse["x"] is not None
        and abs(mouse["x"] - c["x"]) < 50
        and abs(mouse["y"] - c["y"]) < 50
        and (c["r"] < 40)
    ):
        c["r"] += 1
    elif c["r"] > c["min"]:
        c["r"] -= 1


init(400)
### 게임이 실행되면 작동
while True:
    screen.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
        elif event.type == pygame.MOUSEMOTION:
            mouse["x"], mouse["y"] = event.pos
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            circles = []
            init(400)

    for c in circles:
        move_circle(c)
        react_to_mouse(c)
        pygame.draw.circle(screen, c["c"], (c["x"], c["y"]), c["r"])

    pygame.display.flip()
    clock.tick(60)
