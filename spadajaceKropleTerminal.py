import curses
import random
import time

DROP_SYMBOLS = {1: '.', 2: '\'', 3: '|'}


def create_drop(max_x):
    """Tworzy nową kroplę na losowej pozycji x u góry ekranu z losową prędkością."""
    x = random.randint(0, max_x - 1)
    speed = random.randint(1, 3)  # Prędkość od 1 do 3
    return (x, 0, speed)


def update_drops(drops, max_y, max_x):
    """Aktualizuje pozycje kropli i generuje nowe."""
    new_drops = [(x, min(y + speed, max_y - 2), speed) for x, y, speed in drops if y + speed < max_y - 1]

    for _ in range(random.randint(2, 5)):  # Zwiększenie częstotliwości deszczu
        new_drops.append(create_drop(max_x))

    return new_drops


def draw_drops(stdscr, drops):
    """Rysuje krople na ekranie."""
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()

    for x, y, speed in drops:
        if 0 <= y < max_y - 1 and 0 <= x < max_x - 1:  # 🔥 Kluczowe zabezpieczenie!
            stdscr.addch(y, x, DROP_SYMBOLS[speed])

    stdscr.refresh()


def main(stdscr):
    """Główna funkcja programu."""
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    drops = []

    while True:
        max_y, max_x = stdscr.getmaxyx()
        drops = update_drops(drops, max_y, max_x)
        draw_drops(stdscr, drops)
        time.sleep(0.05)

        if stdscr.getch() != -1:  # Przerwanie pętl po wciśnięciu klawisza
            break


curses.wrapper(main)
