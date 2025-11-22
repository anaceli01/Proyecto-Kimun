
import pygame as pg
from states.menu import Menu
from states.level_selector import LevelSelector

def main():
    pg.init()
    pg.display.set_caption("Willichedunguay")
    WIDTH, HEIGHT = 900, 500
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    current_state = None

    #Esta función será enviada a los estados
    def change_state(to):
        nonlocal current_state
        if to == "menu":
            current_state = Menu(WIDTH, HEIGHT, change_state)
        elif to == "level_selector":
            current_state = LevelSelector(WIDTH, HEIGHT, change_state)

    
    # INICIALIZA EL PRIMER ESTADO
    change_state("menu")


    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            current_state.handle_event(event)

        current_state.update()
        current_state.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()



