import pygame, sys
import os
from pygame.locals import *
from Card import *
from Deck import *
from Player import *

MARGIN_LEFT = 230
MARGIN_TOP = 150
WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (110, 110, 110)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 120, 0)
RED = (255, 0, 0)
LIGHT_RED = (120, 0, 0)

FPS = 30

pygame.init()
global back
back = "card_cover"
small_font = pygame.font.Font(None, 32)
large_font = pygame.font.Font(None, 50)

def update_file(player1):
    f = open('scores.txt','r') 
    file = f.readlines() 
    last = file[0] 
    last = last.strip()
    last = last.split(',')
    last = int(last[1])
    
    if last < int(player1.wins): 
        f.close() 
        file = open('scores.txt', 'w') 
        file.write(str(player1.name) + "," + str(player1.wins)) 
        file.close() 

def show_leader():
    f = open('scores.txt','r')
    file = f.readlines()
    last = file[0]
    last = last.strip()
    last = last.split(',')
    name = str(last[0])
    score = str(last[1])
    return name, score

click = False

def main_menu():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(GRAY)
        pygame.display.set_caption("WAR!")
        icon = pygame.image.load('cannon.png')
        pygame.display.set_icon(icon)

        war_button = large_font.render("GO TO WAR", True, WHITE)
        war_button_rect = war_button.get_rect()
        war_button_rect.center = (400, 200)
        war_rect = pygame.Rect(295, 173, 210, 55)
        
        pygame.draw.rect(screen, RED, war_button_rect, -1)
        pygame.draw.rect(screen, RED, war_rect, 3, border_radius=10)

        leader_button = large_font.render("LEADER BOARD", True, WHITE)
        leader_button_rect = leader_button.get_rect()
        leader_button_rect.center = (400, 400)
        leader_rect = pygame.Rect(250, 373, 300, 55)
        
        pygame.draw.rect(screen, RED, leader_button_rect, -1)
        pygame.draw.rect(screen, RED, leader_rect, 3, border_radius=10)
        
        options_button = large_font.render("OPTIONS", True, WHITE)
        options_button_rect = options_button.get_rect()
        options_button_rect.center = (400, 300)
        options_rect = pygame.Rect(315, 273, 170, 55)
        
        pygame.draw.rect(screen, RED, options_button_rect, -1)
        pygame.draw.rect(screen, RED, options_rect, 3, border_radius=10)
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= 300+200 and 170 <= mouse[1] <= 170+60:
                    name_screen()                    
                if 300 <= mouse[0] <= 300+200 and 370 <= mouse[1] <= 370+60:
                    leader_board()
                if 300 <= mouse[0] <= 300+200 and 270 <= mouse[1] <= 270+60:
                    options_screen()   

        screen.blit(war_button, war_button_rect)
        screen.blit(leader_button, leader_button_rect)
        screen.blit(options_button, options_button_rect)
        pygame.display.update()
        

def options_screen():
    global back
    running = True
    
    option_1 =  pygame.image.load(r'./Card_Pics/'+back+'.png')
    option_1 =  pygame.transform.scale(option_1, (100,160))
    option_2 =  pygame.image.load(r'./Card_Pics/blue.png')
    option_2 =  pygame.transform.scale(option_2, (100,160))
    option_3 =  pygame.image.load(r'./Card_Pics/black.png')
    option_3 =  pygame.transform.scale(option_3, (100,160))
    option_4 =  pygame.image.load(r'./Card_Pics/red.png')
    option_4 =  pygame.transform.scale(option_4, (100,160))
    option_5 =  pygame.image.load(r'./Card_Pics/xmas.png')
    option_5 =  pygame.transform.scale(option_5, (100,160))
    
    option_1_rect = pygame.Rect(20, 0, 70, 200)
    option_2_rect = pygame.Rect(140, 0, 70, 200)
    option_3_rect = pygame.Rect(260, 0, 70, 200)
    option_4_rect = pygame.Rect(380, 0, 70, 200)
    option_5_rect = pygame.Rect(500, 0, 70, 200)
    
    choose_text = large_font.render("CHOOSE YOUR CARDBACK", True, WHITE)
    choose_text_rect = choose_text.get_rect()
    choose_text_rect.center = (400, 500)
    
    while running:
        mouse = pygame.mouse.get_pos()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(GRAY)
        pygame.display.set_caption("OPTIONS!")
        icon = pygame.image.load('cannon.png')
        pygame.display.set_icon(icon)
        
        
        if option_1_rect.collidepoint(mouse):
            if click:
                back = "card_cover"
                return back
                running = False
                main_menu()
        if option_2_rect.collidepoint(mouse):
            if click:
                back = "blue"
                return back
                running = False
                main_menu()
        if option_3_rect.collidepoint(mouse):
            if click:
                back = "black"
                return back
                running = False
                main_menu()
        if option_4_rect.collidepoint(mouse):
            if click:
                back = "red"
                return back
                running = False
                main_menu()
        if option_5_rect.collidepoint(mouse):
            if click:
                back = "xmas"
                return back
                running = False
                main_menu()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        screen.blit(option_1, (20,0))
        screen.blit(option_2, (140,0))
        screen.blit(option_3, (260,0))
        screen.blit(option_4, (380,0))
        screen.blit(option_5, (500,0))
        screen.blit(choose_text, choose_text_rect)
        pygame.display.update()           

def name_screen():
    running = True
    input_rect = pygame.Rect(250, 273, 300, 55)
    user_text = ''
    while running:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(GRAY)
        pygame.display.set_caption("GET READY!")
        icon = pygame.image.load('cannon.png')
        pygame.display.set_icon(icon)
        pygame.draw.rect(screen,RED,input_rect,2)
        text_surface = large_font.render(user_text,True,(255,255,255,))
        
        name_box = large_font.render("ENTER YOUR NAME", True, WHITE)
        name_box_rect = name_box.get_rect()
        name_box_rect.center = (WIDTH//2, 70)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1] 
                if event.key == pygame.K_RETURN:
                    player1 = Player(user_text)
                    player2 = Player("Computer")
                    game_screen(player1, player2)
                if event.key == K_ESCAPE:
                    user_text = user_text[:-1]
                    running = False
                    main_menu()
                else:
                    user_text += event.unicode 
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        screen.blit(name_box, name_box_rect)
        pygame.display.update()

def leader_board():
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(GRAY)
        pygame.display.set_caption("OPTIONS!")
        icon = pygame.image.load('cannon.png')
        pygame.display.set_icon(icon)
        
        winner_board = large_font.render("THE WINNER IS: "+str(show_leader()), True, WHITE)
        winner_board_rect = winner_board.get_rect()
        winner_board_rect.center = (WIDTH//2, 70)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        screen.blit(winner_board, winner_board_rect)            
        pygame.display.update()           

def game_over(player1, player2):
    running = True
    clock = pygame.time.Clock()
    if player1.wins > player2.wins:
        winner = player1.name
        update_file(player1)
    else:
        winner = player2.name
    
    while running:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(GRAY)
        pygame.display.set_caption("WINNER!")
        icon = pygame.image.load('cannon.png')
        pygame.display.set_icon(icon)
        

        winner_board = large_font.render("THE WINNER IS: "+str(winner), True, WHITE)
        winner_board_rect = winner_board.get_rect()
        winner_board_rect.center = (WIDTH//2, 70)
        
        
        main_button = large_font.render("MAIN MENU", True, WHITE)
        main_button_rect = main_button.get_rect()
        main_button_rect.center = (400, 200)
        main_rect = pygame.Rect(295, 173, 210, 55)
        
        pygame.draw.rect(screen, RED, main_button_rect, -1)
        pygame.draw.rect(screen, RED, main_rect, 3, border_radius=10)
        
        
        play_again_button = large_font.render("PLAY AGAIN?", True, WHITE)
        play_again_button_rect = play_again_button.get_rect()
        play_again_button_rect.center = (400, 400)
        play_rect = pygame.Rect(275, 373, 250, 55)
        
        pygame.draw.rect(screen, RED, play_again_button_rect, -1)
        pygame.draw.rect(screen, RED, play_rect, 3, border_radius=10)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= 300+200 and 170 <= mouse[1] <= 170+60:
                    del player1
                    del player2
                    running = False
                    main_menu()                    
                if 300 <= mouse[0] <= 300+200 and 370 <= mouse[1] <= 370+60:
                    del player1
                    del player2
                    running = False
                    name_screen() 
        
        
        screen.blit(winner_board, winner_board_rect)
        screen.blit(play_again_button, play_again_button_rect)
        screen.blit(main_button, main_button_rect)
        pygame.display.update()
    
    
def game_screen(player1, player2):
    running = True
    clock = pygame.time.Clock()
    deck = Deck()
    p1_card =  pygame.image.load(r'./cannon.png')
    p1_card = pygame.transform.scale(p1_card, (100,160))
    p2_card =  pygame.image.load(r'./cannon.png')
    p2_card = pygame.transform.scale(p2_card, (100,160))
    if len(deck.cards) > 0:
        stack =  pygame.image.load(r'./Card_Pics/'+back+'.png')
        stack =  pygame.transform.scale(stack, (100,160))
    else:
        stack =  pygame.image.load(r'./cannon.png')
        stack =  pygame.transform.scale(stack, (100,160))
        
    while running:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(GRAY)
        pygame.display.set_caption("GAME!")
        icon = pygame.image.load('cannon.png')
        pygame.display.set_icon(icon)
        
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(deck.cards) > 0:
                    if MARGIN_LEFT+115 <= mouse[0] <= MARGIN_LEFT+200 and MARGIN_TOP+250 <= mouse[1] <= MARGIN_TOP+450:
                        try:
                            p1_draw = deck.deal()
                            p1_card = pygame.image.load(r'./cards/' + str(p1_draw.value) + str(p1_draw.suit) + '.png')
                            p1_card = pygame.transform.scale(p1_card, (100,160))
                            p2_draw = deck.deal()
                            p2_card = pygame.image.load(r'./cards/' + str(p2_draw.value) + str(p2_draw.suit) + '.png')
                            p2_card = pygame.transform.scale(p2_card, (100,160))
                            if p1_draw.value > p2_draw.value:
                                player1.wins = player1.wins + 1
                            elif p1_draw.value < p2_draw.value:
                                player2.wins = player2.wins + 1
                            elif p1_draw.value == p2_draw.value:
                                while p1_draw.value == p2_draw.value:
                                    try:
                                        for i in range(3):
                                            deck.deal()
                                                              
                                
                                        p1_draw = deck.deal()
                                        p1_card = pygame.image.load(r'./cards/' + str(p1_draw.value) + str(p1_draw.suit) + '.png')
                                        p1_card = pygame.transform.scale(p1_card, (100,160))
                                        p2_draw = deck.deal()
                                        p2_card = pygame.image.load(r'./cards/' + str(p2_draw.value) + str(p2_draw.suit) + '.png')
                                        p2_card = pygame.transform.scale(p2_card, (100,160))
                                        if p1_draw.value > p2_draw.value:
                                            player1.wins = player1.wins + 1
                                        elif p1_draw.value < p2_draw.value:
                                            player2.wins = player2.wins + 1
                                    except:
                                        running = False
                                        game_over(player1, player2)
                                
                            if len(deck.cards) == 0:
                                stack =  pygame.image.load(r'./cannon.png')
                                stack =  pygame.transform.scale(stack, (100,160))
                                running = False
                                game_over(player1, player2)
                        except:
                                running = False
                                game_over(player1, player2)      
                    else:
                        running = True
                        
                
            score_text = large_font.render(str(player1.name) + "=" +str(player1.wins), True, BLACK)
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (200, 70)
            score_rect = pygame.Rect(100, 40, 210, 55)
            pygame.draw.rect(screen, RED, score_text_rect, -1)
            pygame.draw.rect(screen, RED, score_rect, 3, border_radius=10)
            
            
            score_text_2 = large_font.render(str(player2.name) + "=" +str(player2.wins), True, BLACK)
            score_text_rect_2 = score_text_2.get_rect()
            score_text_rect_2.center = (550, 70)
            score_rect_2 = pygame.Rect(435, 40, 240, 55)
            pygame.draw.rect(screen, RED, score_text_rect_2, -1)
            pygame.draw.rect(screen, RED, score_rect_2, 3, border_radius=10)            

        screen.blit(p1_card, (MARGIN_LEFT,MARGIN_TOP))
        screen.blit(p2_card, (MARGIN_LEFT+220, MARGIN_TOP))
        screen.blit(stack, (MARGIN_LEFT+115, MARGIN_TOP+250))
        screen.blit(score_text, score_text_rect)
        screen.blit(score_text_2, score_text_rect_2)
        
        
                    
        pygame.display.update()

main_menu()