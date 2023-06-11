import pyautogui
import time

# Locate the tab and activate it
tab_x = 100  # X-coordinate of the tab
tab_y = 100  # Y-coordinate of the tab
pyautogui.click(tab_x, tab_y)

# Wait for the tab to become active
time.sleep(1)

# Send keyboard commands to the tab
pyautogui.typewrite('https://www.example.com')
pyautogui.press('enter')

# Wait for the page to load
time.sleep(5)

# Scroll down the page
pyautogui.scroll(-100)  # Negative value for scrolling down

# Click on a specific element
element_x = 500  # X-coordinate of the element
element_y = 300  # Y-coordinate of the element
pyautogui.click(element_x, element_y)

# Perform other actions as needed

# Close the tab
pyautogui.hotkey('ctrl', 'w')
