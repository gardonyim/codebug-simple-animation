import codebug_tether
import time

SLEEP_TIME_MIN = 0.1
SLEEP_TIME_MAX = 1
SLEEP_TIME_STEP = 0.1
SLEEP_TIME = 0.5
SCREEN_SIZE = 5


codebug = codebug_tether.CodeBug()


def display(line, sleep_time):
    codebug.clear()
    map(codebug.set_pixel(), line)
    time.sleep(sleep_time)


def set_main_diagonal(sleep_time):
    line = [(index, index, 1) for index in range(SCREEN_SIZE)]
    display(line, sleep_time)


def set_side_diagonal(sleep_time):
    line = [(index, SCREEN_SIZE - index, 1) for index in range(SCREEN_SIZE)]
    display(line, sleep_time)


def set_vertical(sleep_time):
    line = [(index, 2, 1) for index in range(SCREEN_SIZE)]
    display(line, sleep_time)


def set_horizontal(sleep_time):
    line = [(2, index, 1) for index in range(SCREEN_SIZE)]
    display(line, sleep_time)


def main():
    sleep_time = SLEEP_TIME
    while True:
        set_vertical(sleep_time)
        set_main_diagonal(sleep_time)
        set_horizontal(sleep_time)
        set_side_diagonal(sleep_time)
        if codebug.get_input('A') == 1 and (sleep_time - SLEEP_TIME_STEP) >= SLEEP_TIME_MIN:
                sleep_time -= SLEEP_TIME_STEP
        if codebug.get_input('B') == 1 and (sleep_time + SLEEP_TIME_STEP) <= SLEEP_TIME_MAX:
                sleep_time += SLEEP_TIME_STEP


if __name__ == "__main__":
    main()
