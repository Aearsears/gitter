import curses
import time

owl = """  
(o.o)
(   )
 " "
"""


def draw(x, y, s, stdscr):
    dx, dy = x, y
    for c in owl:
        if c == '\n' or c == '\r\n':
            dy += 1
            dx = x
        else:
            stdscr.addstr(dy, dx, c)
            dx += 1


def monster_animation(stdscr):
    # Disable cursor and enable color
    curses.curs_set(0)
    stdscr.nodelay(1)  # Make getch() non-blocking
    height, width = stdscr.getmaxyx()  # Get screen dimensions

    # initial pos
    x, y = height - 5, 1
    dx, dy = x, y
    up = 1

    while True:
        stdscr.clear()

        draw(dx, dy, owl, stdscr)

        # status bar/ message at bottom of screen
        stdscr.addstr(height - 1, 0, "Gitter",
                      curses.A_STANDOUT)

        # Refresh the screen to show the updates
        stdscr.refresh()

        dy += up
        up *= -1

        # Sleep for a short duration to control animation speed
        time.sleep(1)

        # Exit on key press
        if stdscr.getch() != -1:
            break


# Initialize curses and run the animation
curses.wrapper(monster_animation)
