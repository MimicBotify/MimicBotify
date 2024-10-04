from pynput.mouse import Button, Controller
from PIL import ImageGrab
import time
import numpy as np

# Set up the mouse controller
mouse = Controller()

# Define game window boundaries
top_left = (515, 22)
bottom_right = (853, 690)

# Color definitions for the flower, crystal, and bomb
flower_rgb = [(63, 219, 0)]  # Add more similar colors if needed
crystal_rgb = (130, 221, 233)
bomb_hsv_range = [(0, 0, 71), (0, 5, 53)]  # HSV range for the bomb

# Time management
start_time = time.time()
timeout = 60  # 60 seconds

# Cooldown to avoid clicking the same area
area_click_cooldown = 1.5  # seconds
last_clicked_positions = []  # Store coordinates of recent clicks

# Flag to avoid clicking blue after crystal is clicked
crystal_clicked = False
crystal_cooldown_start = 0
crystal_cooldown_duration = 3 # Seconds to avoid blue after crystal

def can_click(x, y):
    """Check if the bot can click this area based on recent clicks."""
    global last_clicked_positions
    for pos, click_time in last_clicked_positions:
        if time.time() - click_time < area_click_cooldown:
            if abs(x - pos[0]) < 20 and abs(y - pos[1]) < 20:
                return False
    return True

def add_click_position(x, y):
    """Store the clicked position and the current time."""
    global last_clicked_positions
    last_clicked_positions.append(((x, y), time.time()))
    last_clicked_positions = [
        (pos, t) for pos, t in last_clicked_positions if time.time() - t < area_click_cooldown
    ]

def is_color_near(rgb, target_rgb, threshold=20):
    """Check if the color is near the target color within the threshold."""
    return all(abs(c1 - c2) < threshold for c1, c2 in zip(rgb, target_rgb))

def is_bomb_near(pixel_hsv):
    """Check if the pixel is in the bomb's HSV range."""
    return bomb_hsv_range[0] <= pixel_hsv <= bomb_hsv_range[1]

def find_and_click_color():
    global start_time, last_clicked_positions, crystal_clicked, crystal_cooldown_start

    while True:
        current_time = time.time()

        # End the script after timeout
        if current_time - start_time > timeout:
            print("Time is up. Script finished.")
            break

        # Capture a smaller part of the screen (within the game window)
        screenshot = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        screenshot_np = np.array(screenshot)

        # Priority: Check for crystal (blue)
        if not crystal_clicked:
            for x in range(0, screenshot_np.shape[1], 5):  # Width
                for y in range(0, screenshot_np.shape[0], 5):  # Height
                    pixel = screenshot_np[y, x]
                    if is_color_near(pixel, crystal_rgb):
                        screen_x, screen_y = x + top_left[0], y + top_left[1]
                        if can_click(screen_x, screen_y):
                            mouse.position = (screen_x, screen_y)
                            mouse.click(Button.left, 1)
                            add_click_position(screen_x, screen_y)
                            crystal_clicked = True
                            crystal_cooldown_start = time.time()
                            print(f"Clicked on crystal at ({screen_x}, {screen_y})")
                            break

        # Avoid clicking blue for the cooldown duration
        if crystal_clicked and time.time() - crystal_cooldown_start > crystal_cooldown_duration:
            crystal_clicked = False

        # Now look for flowers (green)
        for x in range(0, screenshot_np.shape[1], 10):  # Width
            for y in range(0, screenshot_np.shape[0], 10):  # Height
                pixel = screenshot_np[y, x]
                for color in flower_rgb:
                    if is_color_near(pixel, color):
                        screen_x, screen_y = x + top_left[0], y + top_left[1]
                        if can_click(screen_x, screen_y):
                            # Simulate click without moving the mouse physically
                            mouse.position = (screen_x, screen_y)
                            mouse.click(Button.left, 1)
                            add_click_position(screen_x, screen_y)
                            print(f"Clicked on flower at ({screen_x}, {screen_y})")
                            break

# Start scanning and clicking
find_and_click_color()
