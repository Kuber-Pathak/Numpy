import numpy as np
import pygame 
import sys

BOTTOM_COLOR  =(27,66,66)
CIRCLE_COLOR = (92,131,116)

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
            print(r)
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

def print_screen(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BOTTOM_COLOR,(c*SQARESIZE,r*SQARESIZE + SQARESIZE,SQARESIZE,SQARESIZE))
            pygame.draw.circle(screen,CIRCLE_COLOR,(int(c*SQARESIZE+SQARESIZE/2),int(r*SQARESIZE+SQARESIZE +SQARESIZE/2)),RADIUS)

board = creat_board();


game_over = False
turn = 0

pygame.init()
SQARESIZE = 100

height = (ROW_COUNT + 1) * 100
width = COLUMN_COUNT * 100

RADIUS = int(SQARESIZE/2)

screen = pygame.display.set_mode((height,width))

print_screen(board)
pygame.display.update()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("")
            # if turn == 0:
            #     col = int(input("player 1 enter you choice (0-6)"))
            #     if(valid_location(board,col)):
            #         row = next_valid_row(board,col)
            #         drop_ball(board,row,col,1)
            #         if(winning_move(board,1)):
            #             print("Congratulations player 1 wins!!!")
            #             game_over=True

            # else: 
            #     col = int(input("player 2 enter you choice (0-6)"))
            #     if(valid_location(board,col)):
            #         row = next_valid_row(board,col)
            #         drop_ball(board,row,col,2)
            #         if(winning_move(board,2)):
            #             print("Congratulations player 2 wins!!!")
            #             game_over=True

            # print_board(board)
            # turn = turn + 1
            # turn = turn % 2
