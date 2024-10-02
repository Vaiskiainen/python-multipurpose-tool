import os
import sys
import requests
import time
from datetime import datetime
import math
import pyperclip
import sqlite3
from PIL import Image, ImageFilter  # For image manipulation
import random

class MultiPurposeTool:
    def __init__(self):
        self.running = True

    def show_menu(self):
        print("\nWelcome to the Expanded Multipurpose Tool!")
        print("1. System Information")
        print("2. Math Operations")
        print("3. Web Scraping")
        print("4. API Interaction (Weather)")
        print("5. File Handling")
        print("6. Text Processing")
        print("7. Cryptography")
        print("8. Clipboard Manager")
        print("9. Image Manipulation")
        print("10. Task Scheduler")
        print("11. Voice Assistant")
        print("12. Database Interaction")
        print("13. Mini Games")
        print("14. Exit")

    # Existing methods here...
    # Adding new functionality below...

    # Cryptography (Caesar Cipher)
    def cryptography(self):
        print("\nCryptography - Caesar Cipher")
        action = input("Choose: [1] Encode or [2] Decode: ")
        text = input("Enter text: ")
        shift = int(input("Enter shift amount: "))

        def caesar_cipher(text, shift, encode=True):
            result = ""
            for char in text:
                if char.isalpha():
                    shift_amount = shift if encode else -shift
                    char_code = ord(char) + shift_amount
                    if char.islower():
                        result += chr((char_code - 97) % 26 + 97)
                    else:
                        result += chr((char_code - 65) % 26 + 65)
                else:
                    result += char
            return result

        if action == '1':
            print("Encoded text:", caesar_cipher(text, shift, encode=True))
        elif action == '2':
            print("Decoded text:", caesar_cipher(text, shift, encode=False))
        else:
            print("Invalid option.")

    # Clipboard Manager
    def clipboard_manager(self):
        print("\nClipboard Manager")
        action = input("Choose: [1] Copy or [2] Paste: ")

        if action == '1':
            text = input("Enter text to copy: ")
            pyperclip.copy(text)
            print("Text copied to clipboard.")
        elif action == '2':
            print("Clipboard content:", pyperclip.paste())
        else:
            print("Invalid option.")

    # Image Manipulation (Resize or apply filter)
    def image_manipulation(self):
        print("\nImage Manipulation")
        filename = input("Enter image filename: ")
        action = input("Choose: [1] Resize, [2] Apply Blur filter: ")

        try:
            img = Image.open(filename)
            if action == '1':
                width = int(input("Enter new width: "))
                height = int(input("Enter new height: "))
                img = img.resize((width, height))
                img.show()
            elif action == '2':
                img = img.filter(ImageFilter.BLUR)
                img.show()
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"Error: {e}")

    # Task Scheduler (simple delay)
    def task_scheduler(self):
        print("\nTask Scheduler")
        delay = int(input("Enter delay in seconds: "))
        task = input("Enter task description (e.g., 'print a message'): ")

        print(f"Task scheduled: {task} will execute after {delay} seconds.")
        time.sleep(delay)
        print(f"Executing task: {task}")
        if task == "print a message":
            print("Hello! This is your scheduled message.")
        # You can add more task types here...

    # Mini Games
    def mini_games(self):
        print("\nMini Games")
        print("1. Number Guessing")
        print("2. Rock-Paper-Scissors")
        choice = input("Choose a game: ")

        if choice == '1':
            self.number_guessing_game()
        elif choice == '2':
            self.rock_paper_scissors()
        else:
            print("Invalid option.")

    def number_guessing_game(self):
        print("Number Guessing Game - Guess the number between 1 and 100!")
        number = random.randint(1, 100)
        guess = None
        while guess != number:
            guess = int(input("Enter your guess: "))
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("Correct! You guessed the number.")

    def rock_paper_scissors(self):
        print("Rock-Paper-Scissors")
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice.")
        elif user_choice == computer_choice:
            print(f"It's a tie! Both chose {user_choice}.")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You win! {user_choice} beats {computer_choice}.")
        else:
            print(f"You lose! {computer_choice} beats {user_choice}.")

    def run(self):
        while self.running:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.system_info()
            elif choice == '2':
                self.math_operations()
            elif choice == '3':
                self.web_scraping()
            elif choice == '4':
                self.get_weather()
            elif choice == '5':
                self.file_handling()
            elif choice == '6':
                self.text_processing()
            elif choice == '7':
                self.cryptography()
            elif choice == '8':
                self.clipboard_manager()
            elif choice == '9':
                self.image_manipulation()
            elif choice == '10':
                self.task_scheduler()
            elif choice == '11':
                print("Voice Assistant not yet implemented!")
            elif choice == '12':
                print("Database interaction not yet implemented!")
            elif choice == '13':
                self.mini_games()
            elif choice == '14':
                print("Exiting...")
                self.running = False
            else:
                print("Invalid option, try again.")

# Main
if __name__ == "__main__":
    tool = MultiPurposeTool()
    tool.run()
