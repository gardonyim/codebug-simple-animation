import codebug_tether
import time

SLEEP_TIME_MIN = 0.1
SLEEP_TIME_MAX = 1
SLEEP_TIME_STEP = 0.1
SLEEP_TIME = 0.5


codebug = codebug_tether.CodeBug()


def set_main_diagonal():
    codebug.clear()
    codebug.set_pixel(0, 0, 1)
    codebug.set_pixel(1, 1, 1)
    codebug.set_pixel(2, 2, 1)
    codebug.set_pixel(3, 3, 1)
    codebug.set_pixel(4, 4, 1)


def set_reverse_diagonal():
    codebug.clear()
    codebug.set_pixel(0, 4, 1)
    codebug.set_pixel(1, 3, 1)
    codebug.set_pixel(2, 2, 1)
    codebug.set_pixel(3, 1, 1)
    codebug.set_pixel(4, 0, 1)


def set_vertical():
    codebug.clear()
    codebug.set_col(2, 0b11111)


def set_horizontal():
    codebug.clear()
    codebug.set_row(2, 0b11111)


def main():
    sleep_time = SLEEP_TIME
    while True:
        set_vertical()
        time.sleep(sleep_time)
        set_main_diagonal()
        time.sleep(sleep_time)
        set_horizontal()
        time.sleep(sleep_time)
        set_reverse_diagonal()
        time.sleep(sleep_time)
        if codebug.get_input('A') == 1:
            if (sleep_time - SLEEP_TIME_STEP) >= SLEEP_TIME_MIN:
                sleep_time -= SLEEP_TIME_STEP
        if codebug.get_input('B') == 1:
            if (sleep_time + SLEEP_TIME_STEP) <= SLEEP_TIME_MAX:
                sleep_time += SLEEP_TIME_STEP


if __name__ == "__main__":
    main()