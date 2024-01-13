#A graphical connect4 game using pyton

import sys
import numpy as np
import pygame 
import math

BOTTOM_COLOR  =(27,66,66)
CIRCLE_COLOR = (92,131,116)
BLACK= (0,0,0)

PLAYER1 = (49,48,77)
PLAYER2 = (243,248,255)

ROW_COUNT = 6
COLUMN_COUNT = 7

def creat_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_ball(board,row,col,ball):
    board[row][col] = ball

def next_valid_row(board,col):  
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0

def winning_move(board,ball):
    #check for hrizontal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c]==ball and board[r][c+1]==ball and board[r][c+2]==ball and board[r][c+3]==ball:
                return True

    #check for vertical win
    for c in range(COLUMN_COUNT ):
        for r in range(ROW_COUNT - 3):
            if board[r][c]==ball and board[r+1][c]==ball and board[r+2][c]==ball and board[r+3][c]==ball:
                return True

    #check for positive slope diagonal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c]==ball and board[r+1][c+1]==ball and board[r+2][c+2]==ball and board[r+3][c+3]==ball:
                return True

    #check for negative slope diagonal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(3,ROW_COUNT):
            if board[r][c]==ball and board[r-1][c+1]==ball and board[r-2][c+2]==ball and board[r-3][c+3]==ball:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BOTTOM_COLOR,(c*SQUARESIZE,r*SQUARESIZE + SQUARESIZE,SQUARESIZE,SQUARESIZE)) 
            pygame.draw.circle(screen,CIRCLE_COLOR,(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS) 
        
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] ==1:
                pygame.draw.circle(screen,PLAYER1,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS) 
            elif board[r][c]==2:
                pygame.draw.circle(screen,PLAYER2,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS) 
    pygame.display.update()       

board = creat_board();

game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width  = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

RADIUS = int(SQUARESIZE/2 -5)


screen = pygame.display.set_mode((width,height))
draw_board(board)
pygame.display.update() #shows update on reach run

myfont = pygame.font.SysFont("monspace",75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() #exits window
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            posx = event.pos[0]
            if turn ==0:
                pygame.draw.circle(screen,PLAYER1,(posx,int(SQUARESIZE/2)),RADIUS)
            else:
                 pygame.draw.circle(screen,PLAYER2,(posx,int(SQUARESIZE/2)),RADIUS)
        pygame.display.update()
        if event.type ==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            # print(event.pos)
            if turn == 0:
                posx = event.pos[0] #gives position of mosue
                col = int(math.floor(posx/SQUARESIZE))

                if(valid_location(board,col)):
                    row = next_valid_row(board,col)
                    drop_ball(board,row,col,1)
                    if(winning_move(board,1)):
                        label = myfont.render("Player 1 wins!!",1,PLAYER1)
                        screen.blit(label,(40,10))
                        game_over=True

            else: 
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if(valid_location(board,col)):
                    row = next_valid_row(board,col)
                    drop_ball(board,row,col,2)
                    if(winning_move(board,2)):
                        label = myfont.render("Player 2 wins!!",1,PLAYER2)
                        screen.blit(label,(40,10))
                        game_over=True
            draw_board(board)
            turn = turn + 1
            turn = turn % 2
            if game_over:
                pygame.time.wait(3000)