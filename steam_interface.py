import pyautogui
import time
import pygetwindow as gw
import cv2

# Define functions to find and click on specific game elements
def find_and_click(window, button_image):
    try:
        window.activate()  # Activate the specified window
        location = pyautogui.locateCenterOnScreen(button_image, confidence = .7)
        if location:
            pyautogui.click(location)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error finding or clicking {button_image}: {e}")
        return False

# Example usage: automate a sequence of actions in the game
def play_game(window):
    # Open the game
    time.sleep(1)
    if find_and_click(window, 'play_button.png'):
        time.sleep(2)  # Wait for the game to start
        # Perform actions in the game
        find_and_click(window, 'arena_button.png')
        time.sleep(1)
        # Perform other actions...
    else:
        print("Start game button not found. Game may not be visible.")

# Get the game window
game_window = gw.getWindowsWithTitle('Super Auto Pets')[0]

# Call the function to play the game with the specified window
play_game(game_window)