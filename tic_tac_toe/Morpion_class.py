
import pygame
import sys
from arene_class import Arene
from Screen_class import Screen
from Mouse import Mouse


class Morpion:
    """The main class for manage morpion"""

    def __init__(self):
        #Initialise l'ecran
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Morpion")

        self.arene = Arene()
        self.settings = Screen()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.mouse = Mouse()

    def run_game(self):
        while True:
            self._check_events()
            self._arene_draw()
            self._update_screen()


    def _draw_obj(self, event):
        #draw the cross or circle
        self._get_mouse_position(event)
        self._get_the_square()
        if self.mouse.player == 0:
            self._draw_cross()
        else:
            self._draw_circle()
        self._score()
        if self.mouse.player == 0:
            self.mouse.player = 1
        else:
            self.mouse.player = 0

    def _score(self):
        #check the score if a player winn or the match is NULL
        if self._score_raw() == 1 or self._score_columns() == 1 or self._score_diagonal() == 1:
            self._end(1)
        if self._score_null() == -1:
            self._end(-1)
    def _end(self, num):
        if num == 1:
            str = "YOU WINN !!"
        else:
            str = "NULL !!"
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"{str}", True, self.arene.White, self.arene.Black)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_rect().width// 2, self.screen.get_rect().height// 2)
        self.screen.fill(self.arene.Black)
        self.screen.blit(text, textRect)


    def _score_null(self):
        #return -1 if the score is null
        if (len(self.mouse.list_squares[0]) + len(self.mouse.list_squares[1])) >= 9:
            return -1

    def _score_diagonal(self):
        #check the diagonal
        if 0 in self.mouse.list_squares[self.mouse.player] and 4 in self.mouse.list_squares[self.mouse.player] and 8 in self.mouse.list_squares[self.mouse.player]:
            return(1)
        if 2 in self.mouse.list_squares[self.mouse.player] and 4 in self.mouse.list_squares[self.mouse.player] and 6 in self.mouse.list_squares[self.mouse.player]:
            return(1)

    def _score_columns(self):
        #check the columns
        if 0 in self.mouse.list_squares[self.mouse.player] and 1 in self.mouse.list_squares[self.mouse.player] and 2 in self.mouse.list_squares[self.mouse.player]:
            return(1)
        if 3 in self.mouse.list_squares[self.mouse.player] and 4 in self.mouse.list_squares[self.mouse.player] and 5 in self.mouse.list_squares[self.mouse.player]:
            return(1)
        if 6 in self.mouse.list_squares[self.mouse.player] and 7 in self.mouse.list_squares[self.mouse.player] and 8 in self.mouse.list_squares[self.mouse.player]:
            return(1)


    def _score_raw(self):
        #check the row

        if 0 in self.mouse.list_squares[self.mouse.player] and 3 in self.mouse.list_squares[self.mouse.player] and 6 in self.mouse.list_squares[self.mouse.player]:
            return(1)
        if 1 in self.mouse.list_squares[self.mouse.player] and 4 in self.mouse.list_squares[self.mouse.player] and 7 in self.mouse.list_squares[self.mouse.player]:
            return(1)
        if 2 in self.mouse.list_squares[self.mouse.player] and 5 in self.mouse.list_squares[self.mouse.player] and 8 in self.mouse.list_squares[self.mouse.player]:
            return(1)

    def _draw_circle(self):
        #draw circle at the center of sceen
        center_x = self.mouse.square_position_x - self.arene.space_between_column / 2
        center_y = self.mouse.square_position_y - self.arene.space_between_raw / 2
        pygame.draw.circle(self.screen, self.arene.White,[center_x, center_y],100, 10)
        #add the number of square to the list of circle player
        self.mouse.list_squares[1].append(self.mouse.square_position)

    def _draw_cross(self):
        #draw cross at the center of the screen
        #Ajustement is for draw lines inside de square
        #and not a the top left, right
        ajustement_x = self.arene.space_between_column / 4
        ajustement_y = self.arene.space_between_raw / 4

        point_1 = [self.mouse.square_position_x - ajustement_x,
                   self.mouse.square_position_y - ajustement_y]
        point_2 = [self.mouse.square_position_x + ajustement_x - self.arene.space_between_column,
                   self.mouse.square_position_y - ajustement_y]
        point_3 = [self.mouse.square_position_x - ajustement_x,
                   self.mouse.square_position_y + ajustement_y - self.arene.space_between_raw]
        point_4 = [self.mouse.square_position_x + ajustement_x - self.arene.space_between_column,
                   self.mouse.square_position_y + ajustement_y- self.arene.space_between_raw]
        pygame.draw.line(self.screen, self.arene.White, point_1, point_4, 10)
        pygame.draw.line(self.screen, self.arene.White, point_2, point_3, 10)
        #add the number of square to the list of cross player
        self.mouse.list_squares[0].append(self.mouse.square_position)

    def _get_the_square(self):
        #check for the good square where the mouse is and give
        #the number player for the squar
        for square, value in self.arene.square.items():
            if value[0] >= self.mouse.pos_x and value[1] >= self.mouse.pos_y:
                self.mouse.square_position = square
                self.mouse.square_position_x = value[0]
                self.mouse.square_position_y = value[1]



    def _update_screen(self):
        #update screen eatch time we go throught the loop
        pygame.display.flip()

    def _check_events(self):
        #key_bord and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._draw_obj(event)

    def _get_mouse_position(self, event):
        self.mouse.pos_x, self.mouse.pos_y = pygame.mouse.get_pos()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _arene_draw(self):
        #A methode for print the map
        self._draw_column()
        self._draw_raw()
        self._get_coord_square()

    def _get_coord_square(self):
        width = self.screen.get_rect().width
        height = self.screen.get_rect().height
        #creer tout les carrer dans dictionnaire a l aide d une boucle pour pouvoir
        #comparer avec les coordones de mouse et dessiner la croix ou le crayon
        for i in range(9):
            if height <= 0:
                height = self.settings.screen_height
                width -= self.arene.space_between_column
            self.arene.square[i] = [width, height]
            height -= self.arene.space_between_raw


    def _draw_column(self):
        #Draw the map columns
        x = self.settings.screen_width
        y = self.settings.screen_height
        self.arene.space_between_column = space_between_column = (x / 3)
        column_1 = pygame.draw.line(self.screen, self.arene.White,[space_between_column,0],
                         [space_between_column, y], 10)
        column_2 = pygame.draw.line(self.screen, self.arene.White,[space_between_column * 2,0],
                         [space_between_column * 2, y], 10)

    def _draw_raw(self):
        #Draw the map row
        x = self.settings.screen_width
        y = self.settings.screen_height
        self.arene.space_between_raw =  space_between_raw = (y / 3)
        raw_1 = pygame.draw.line(self.screen, self.arene.White,[0,space_between_raw],
                         [x, space_between_raw], 10)
        raw_2 = pygame.draw.line(self.screen, self.arene.White,[0,space_between_raw * 2],
                         [x, space_between_raw * 2], 10)




