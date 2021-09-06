
import pygame
#bo = [
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0],
#[0,0,0,0,0,0,0,0，0]]
bo = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]]

bo_gui = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]]

clicked = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

WIDTH, HEIGHT = 550, 625
diff = 500/9
fps =25
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
GREY = (217, 217, 217)
BLUE = (0,0,220)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 64)
Title = font2.render("Sudoku", True, BLACK)
# text surface object
TitleRect = Title.get_rect()
# set the center of the rectangular object.
TitleRect.center = (WIDTH // 2, 50)

pygame.display.set_caption('Sudoku Solver')


def draw_board():
    i = 25
    j = 100
    while i < 550:
        pygame.draw.line(WIN, BLACK, (i,100), (i,600), 3)
        i+=diff
    while j < 625:
        pygame.draw.line(WIN, BLACK, (25,j), (525,j), 3)
        j+=diff
    i = 25
    j = 100
    while i < 550:
        pygame.draw.line(WIN, BLACK, (i,100), (i,600), 6)
        i+=3*diff
    while j < 625:
        pygame.draw.line(WIN, BLACK, (25,j), (525,j), 6)
        j+=3*diff

def find_empty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return (r,c)
    return (None, None)

def valid (board, num, pos):
    # check row
    row_vals = board[pos[0]]
    if num in row_vals:
        return False 
    # check column
    col_vals = [board[i][pos[1]] for i in range(9)]
    if num in col_vals:
        return False

    # check block
    for i in range(3*(pos[0]//3), 3*(pos[0]//3)+3):
        for j in range(3*(pos[1]//3), 3*(pos[1]//3)+3):
            if num == board[i][j]:
                return False
    return True

def solve(board):
    pos = find_empty(board)
    if pos[0] is None:
        return True
    
    for i in range(1,10):
        if valid(board, i, pos):
            board[pos[0]][pos[1]] = i
            if solve(board):
                return True
        board[pos[0]][pos[1]] = 0   
    return False

solve(bo)
for row in bo:
    print (row)


def solve_animation(board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pos = find_empty(board)
    if pos[0] is None:
        return True
    
    for i in range(1,10):
        # pygame.draw.rect(WIN, WHITE, (pos[1] * diff +25, pos[0] * diff + 110, diff - 5, diff - 5))
        pygame.draw.rect(WIN, RED,(pos[1] * diff +25, pos[0] * diff + 100, diff, diff))
        draw_board()
        num = font1.render(str(i), True, BLACK)
        WIN.blit(num, (pos[1] * diff + 45, pos[0] * diff + 115))
        pygame.display.update()
        # pygame.time.day(10)
        if valid(board, i, pos):
            # pygame.time.day(50)
            # pygame.draw.rect(WIN, WHITE, (pos[1] * diff +25, pos[0] * diff + 110, diff - 5, diff - 5))
            pygame.draw.rect(WIN, GREEN,(pos[1] * diff +25, pos[0] * diff + 100, diff, diff))
            draw_board()
            num = font1.render(str(i), True, BLACK)
            WIN.blit(num, (pos[1] * diff + 45, pos[0] * diff + 115))
            pygame.display.update()
            # pygame.time.day(10)
            board[pos[0]][pos[1]] = i
            if solve_animation(board):
                return True
        board[pos[0]][pos[1]] = 0  
        pygame.draw.rect(WIN, WHITE, (pos[1] * diff +25, pos[0] * diff + 100, diff, diff))
        draw_board()
        # pygame.draw.rect(WIN, BLACK,(pos[1] * diff +25, pos[0] * diff + 110, diff - 5, diff - 5), 3)
        # num = font1.render("0", True, BLACK)
        # WIN.blit(num, (pos[1] * diff + 45, pos[0] * diff + 115))
        pygame.display.update()
        # pygame.time.day(2)    
    return False

def draw_window(board):
    WIN.fill(WHITE)
    draw_board()
    WIN.blit(Title, TitleRect)
    for i in range(9):
        for j in range(9):
            if board[j][i] != 0:
                num = font1.render(str(board[j][i]), True, BLACK)
                WIN.blit(num, (i * diff + 45, j * diff + 115))
    pygame.display.update()

def highlight():
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= 25 and mouse[0]<=525 and mouse[1]>=100 and mouse[1]<=600 and clicked[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)] != 2:
        #highlight grey
        pygame.draw.rect(WIN, GREY, ((mouse[0]-25)//diff * diff +25, (mouse[1]-100)//diff * diff + 100, diff, diff))
        #sected
        # if clicked[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)] == 1:
        #     pygame.draw.rect(WIN, BLUE, ((mouse[0]-25)//diff * diff +25, (mouse[1]-100)//diff * diff + 100, diff, diff))
        #write numer
        if bo_gui[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)] !=0:
            num = font1.render(str(bo_gui[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)]), True, BLACK)
            WIN.blit(num, ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
        #draw lines again
        draw_board()
        pygame.display.update()
        # if clicked[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)] == 0:
        #unhiglight button
        pygame.time.delay(100)
        pygame.draw.rect(WIN, WHITE, ((mouse[0]-25)//diff * diff +25, (mouse[1]-100)//diff * diff + 100, diff, diff))
        #rewrite number
        if bo_gui[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)] !=0:
            num = font1.render(str(bo_gui[int((mouse[1]-100)//diff)][int((mouse[0]-25)//diff)]), True, BLACK)
            WIN.blit(num, ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
        draw_board()
    
    # pygame.draw.rect(WIN, GREY, (5 * diff +25, 5 * diff + 100, diff, diff))


def main():
    clock = pygame.time.Clock()
    run = True
    draw_window(bo_gui)
    while run:
        clock.tick(fps)
        highlight()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                solve_animation(bo_gui)
                for row in bo_gui:
                    print(row)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     for i in range(len(clicked)):
            #         for j in range(len(clicked)):
            #             clicked[i][j] = 0
            #     x,y = int(((mouse[0]-25)//diff)), int(((mouse[1]-100)//diff))
            #     # print(str(x) + ", " + str(y))
            #     if bo_gui[y][x] == 0:
            #         clicked[y][x] = 1
            # if event.type == pygame.KEYDOWN:
            #     clicked[int(((mouse[1]-100)//diff))][int(((mouse[0]-25)//diff))] == 2
            #     pygame.draw.rect(WIN, WHITE, ((mouse[0]-25)//diff * diff +25, (mouse[1]-100)//diff * diff + 100, diff, diff))
            #     if event.key == pygame.K_1:
            #         WIN.blit(font1.render("1", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_2:
            #         WIN.blit(font1.render("2", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_3:
            #         WIN.blit(font1.render("3", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_4:
            #         WIN.blit(font1.render("4", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_5:
            #         WIN.blit(font1.render("5", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_6:
            #         WIN.blit(font1.render("6", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_7:
            #         WIN.blit(font1.render("7", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_8:
            #         WIN.blit(font1.render("8", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     if event.key == pygame.K_9:
            #         WIN.blit(font1.render("9", True, GREY), ((mouse[0]-25)//diff * diff + 45, (mouse[1]-100)//diff * diff + 115))
            #     draw_board()
            #     pygame.display.update()
            #     pygame.time.delay(1000)
                    
                
            # if pygame.mouse.get_pressed():
                # a,b = event.mouse.get_pos()
                # x,y = ((a-25)//diff), ((b-100)//diff)
                # if bo_gui[y][x] == 0:
                #     pygame.draw.rect(WIN, BLUE, (x * diff +25, y * diff + 100, diff, diff))
                #     if event.type == pygame.KEYDOWN:
                #         print(pygame.key.name(event.key))


            
            
if __name__ == '__main__':
    main()

