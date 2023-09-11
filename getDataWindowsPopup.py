from pywinauto import Application
import time


def find_popup_and_get_data():
    app = Application(backend="uia")  # Use the "uia" backend for newer Windows applications
    app.connect(title="Windows PowerShell")  # Replace with the actual title of the popup

    popup = app.window(title="Windows PowerShell")
    if popup.exists():
        popup.set_focus()

        # Perform actions to get data (e.g., input fields, buttons)
        data_field = popup.child_window(title="Data Field Title")
        data_field.click_input()
        data_field.type_keys("your_data_here")

        # Perform further actions (e.g., clicking buttons)
        button = popup.child_window(title="Button Title")
        button.click_input()

    else:
        print("Popup not found.")


# Call the function to initiate the process
find_popup_and_get_data()
