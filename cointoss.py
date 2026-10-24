#idk what to do with this app:
import time
import sys
import random

def __main__():

    def main_menu():
        print("=== Welcome to the coin game ===")
        print("Commands: Face, Head or quit")
    main_menu()
    while True:
        def game():
            user_input = input('User: ').lower().strip()
            if user_input == 'face':
                results = ['face' , 'head']
                a = random.choice(results)
                if a == 'face':
                    print('You win! Returning to menu...')
                    time.sleep(1)
                    return main_menu()
                elif a == 'head':
                    print('You lose! Returning to menu...')
                    time.sleep(1)
                    return main_menu()
            elif user_input == 'head':
                resultsb = ['head' , 'face']
                b = random.choice(resultsb)
                if b == 'head':
                    print('You win! Returning to menu...')
                    time.sleep(1)
                    return main_menu()
                elif b == 'face':
                    print('You lose! Returning to menu...')
                    time.sleep(1)
                    return main_menu()
            elif user_input == 'quit':
                print('Closing Game...')
                time.sleep(1)
                sys.exit()
            else:
                print('[ERROR]! Not a valid command')
                return main_menu()
        game()

__main__()