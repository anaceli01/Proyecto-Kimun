import pygame as pg
import os


class LevelSelector:
    def __init__(self, width, height, change_state):
        self.width = width
        self.height = height
        self.change_state = change_state

        #CARGAR FONDO
        base_path = os.path.dirname(os.path.dirname(__file__))  # sube desde /states/
        bg_path = os.path.join(base_path, "assets", "images", "background.png")
        self.background = pg.image.load(bg_path).convert()

        #AJUSTA LA IMAGEN AL TAMAÑO DE LA VENTANA
        self.background = pg.transform.scale(self.background, (width, height))

        #CARGAR LA TIPOGRAFÍA PIXEL
        font_path = os.path.join(base_path, "assets", "fonts", "FontPixel.ttf")

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN PARA RETROCEDER
        self.button_position = ()
        self.button_back = pg.Polygon()

        #TIPOGRAFÍA DEL TÍTULO Y DE LOS BOTONES DE LOS NIVELES
        self.font_title = pg.font.Font(font_path, 40)
        self.font_button = pg.font.Font(font_path, 20)

        #DEFINIR LA FORMA Y POSICIÓN DEL BOTÓN
        self.button_level = pg.Rect(0, 0, 200, 60)
        self.button_level.center = (width // 2, height // 2 + 40)


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.button_level.collidepoint(event.pos):
                print('Botones para el nivel')


    def update(self):
            pass

    def draw(self, screen):
            #Dibujar el fondo 
            screen.blit(self.background, (0, 0))

            #TÍTULO
            title_surface = self.font_title.render("NIVEL", True, (0, 0, 0))
            title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2 - 40))
            screen.blit(title_surface, title_rect)


        