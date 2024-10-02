import os
import sys
import requests
import time
from datetime import datetime
import math
import random
import pyperclip
from PIL import Image, ImageFilter

class MultiPurposeTool:
    def __init__(self):
        self.running = True

    def show_menu(self):
        print("\nWelcome to the Expanded Multipurpose Tool!")
        print("1. System Information")
        print("2. Math Operations")
        print("3. Unit Conversions")
        print("4. Web Scraping")
        print("5. API Interaction (Weather)")
        print("6. File Handling")
        print("7. Text Processing")
        print("8. Cryptography")
        print("9. Clipboard Manager")
        print("10. Image Manipulation")
        print("11. Task Scheduler")
        print("12. Ping Test")
        print("13. IP Lookup")
        print("14. Mini Games")
        print("15. Exit")

    # Basic System Utilities
    def system_info(self):
        print("\nSystem Information:")
        print(f"Platform: {sys.platform}")
        print(f"Current Working Directory: {os.getcwd()}")
        print(f"Time: {datetime.now()}")

    # Advanced Math Tools (Calculator)
    def math_operations(self):
        print("\nAdvanced Math Tools:")
        print("1. Basic Operations")
        print("2. Square Root")
        print("3. Exponent")
        print("4. Logarithm (base 10)")
        choice = input("Choose an operation: ")

        if choice == '1':
            self.basic_math()
        elif choice == '2':
            num = float(input("Enter number: "))
            print(f"Square Root: {math.sqrt(num)}")
        elif choice == '3':
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print(f"Result: {base ** exp}")
        elif choice == '4':
            num = float(input("Enter number: "))
            print(f"Logarithm (base 10): {math.log10(num)}")
        else:
            print("Invalid choice.")

    def basic_math(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        try:
            if operation == '+':
                print(f"Result: {num1 + num2}")
            elif operation == '-':
                print(f"Result: {num1 - num2}")
            elif operation == '*':
                print(f"Result: {num1 * num2}")
            elif operation == '/':
                print(f"Result: {num1 / num2}")
            else:
                print("Invalid operation.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
    def image_manipulation(self):
     print("\nImage Manipulation Tool:")
     print("1. Resize Image")
     print("2. Apply Filter (BLUR)")
     print("3. Convert to Grayscale")
     choice = input("Choose an action: ")

     if choice == '1':
        self.resize_image()
     elif choice == '2':
        self.apply_filter()
     elif choice == '3':
        self.convert_to_grayscale()
     else:
        print("Invalid choice.")

    def resize_image(self):
     try:
         image_path = input("Enter the path to the image: ")
         image = Image.open(image_path)
         width = int(input("Enter new width: "))
         height = int(input("Enter new height: "))
         resized_image = image.resize((width, height))
         save_path = input("Enter the path to save the resized image (with extension): ")
         resized_image.save(save_path)
         print(f"Image resized and saved to {save_path}")
     except Exception as e:
        print(f"Error: {e}")

    def apply_filter(self):
     try:
         image_path = input("Enter the path to the image: ")
         image = Image.open(image_path)
         blurred_image = image.filter(ImageFilter.BLUR)
         save_path = input("Enter the path to save the blurred image (with extension): ")
         blurred_image.save(save_path)
         print(f"Blurred image saved to {save_path}")
     except Exception as e:
        print(f"Error: {e}")

    def convert_to_grayscale(self):
     try:
         image_path = input("Enter the path to the image: ")
         image = Image.open(image_path)
         grayscale_image = image.convert("L")
         save_path = input("Enter the path to save the grayscale image (with extension): ")
         grayscale_image.save(save_path)
         print(f"Grayscale image saved to {save_path}")
     except Exception as e:
        print(f"Error: {e}")

    # Unit Conversions (Length, Weight, Temperature)
    def unit_conversions(self):
        print("\nUnit Conversions:")
        print("1. Length (Meters to Kilometers)")
        print("2. Weight (Kilograms to Pounds)")
        print("3. Temperature (Celsius to Fahrenheit)")
        choice = input("Choose a conversion: ")

        if choice == '1':
            meters = float(input("Enter meters: "))
            print(f"Kilometers: {meters / 1000}")
        elif choice == '2':
            kg = float(input("Enter kilograms: "))
            print(f"Pounds: {kg * 2.20462}")
        elif choice == '3':
            celsius = float(input("Enter Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"Fahrenheit: {fahrenheit}")
        else:
            print("Invalid choice.")

    # Ping Test (Network utility)
    def ping_test(self):
        print("\nPing Test")
        url = input("Enter website URL (e.g., google.com): ")
        response = os.system(f"ping {url}")
        if response == 0:
            print(f"{url} is reachable.")
        else:
            print(f"{url} is not reachable.")

    # IP Lookup (Retrieve public IP)
    def ip_lookup(self):
        print("\nFetching your public IP address...")
        try:
            ip = requests.get("https://api.ipify.org").text
            print(f"Your public IP is: {ip}")
        except requests.RequestException as e:
            print(f"Error retrieving IP: {e}")

    # More Mini Games
    def mini_games(self):
        print("\nMini Games")
        print("1. Tic-Tac-Toe")
        print("2. Snake Game (Text-based)")
        print("3. Trivia Quiz")
        choice = input("Choose a game: ")

        if choice == '1':
            self.tic_tac_toe()
        elif choice == '2':
            self.snake_game()
        elif choice == '3':
            self.trivia_quiz()
        else:
            print("Invalid choice.")

    # Tic-Tac-Toe Game
    def tic_tac_toe(self):
        board = [" " for _ in range(9)]
        player = "X"

        def display_board():
            print(f"{board[0]} | {board[1]} | {board[2]}")
            print("-" * 5)
            print(f"{board[3]} | {board[4]} | {board[5]}")
            print("-" * 5)
            print(f"{board[6]} | {board[7]} | {board[8]}")

        def check_win(player):
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
            return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

        while " " in board:
            display_board()
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                if check_win(player):
                    display_board()
                    print(f"Player {player} wins!")
                    return
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move, try again.")

        display_board()
        print("It's a tie!")

    # Trivia Quiz Game
    def trivia_quiz(self):
        questions = [
            {"question": "What is the capital of France?", "answer": "paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "Who wrote 'Harry Potter'?", "answer": "jk rowling"}
        ]
        question = random.choice(questions)
        answer = input(f"Trivia: {question['question']}: ").lower()
        if answer == question['answer']:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    # Snake Game (simplified, text-based)
    def snake_game(self):
        print("Snake Game is currently in development. Coming soon!")

    def run(self):
        while self.running:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.system_info()
            elif choice == '2':
                self.math_operations()
            elif choice == '3':
                self.unit_conversions()
            elif choice == '4':
                self.web_scraping()
            elif choice == '5':
                self.get_weather()
            elif choice == '6':
                self.file_handling()
            elif choice == '7':
                self.text_processing()
            elif choice == '8':
                self.cryptography()
            elif choice == '9':
                self.clipboard_manager()
            elif choice == '10':
                self.image_manipulation()
            elif choice == '11':
                self.task_scheduler()
            elif choice == '12':
                self.ping_test()
            elif choice == '13':
                self.ip_lookup()
            elif choice == '14':
                self.mini_games()
            elif choice == '15':
                print("Goodbye!")
                self.running = False
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tool = MultiPurposeTool()
    tool.run()
