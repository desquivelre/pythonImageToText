import pyautogui

# Get the current screen resolution
screen_width, screen_height = pyautogui.size()

# Define the percentage of the screen where you want to click (e.g., 50% from the left and 50% from the top)
click_x_percent = 0.5  # 50% from the left
click_y_percent = 0.5  # 50% from the top

# Calculate the actual coordinates based on the screen resolution
click_x = int(screen_width * click_x_percent)
click_y = int(screen_height * click_y_percent)

# Move the mouse to the calculated coordinates and click
pyautogui.moveTo(click_x, click_y)
pyautogui.click()
