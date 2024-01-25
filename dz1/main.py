import random
import logging
import pygame

RUNNING = False

def init_config():
    logging.basicConfig(level=logging.DEBUG)
    debug_variable = "Hello, debugging!"

init_config()

def start_game():
    logging.debug("Starting game...")

    logging
    pygame.init()
    RUNNING = True

def main_loop():

    return RUNNING

def stop_game():
    logging.debug("Game stopped.")
    RUNNING = False

def end_game():
    pass

def resume_game():
    pass

def main(args: str):
    # global RUNNING = false

    start_game()
    while main_loop():


        stop_game()

    end_game()

if __name__ == "__main__":
    main(None)
