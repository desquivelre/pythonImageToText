import schedule
import time
import subprocess
import datetime

def execute_exe():
    try:
        # Replace 'path_to_your_program.exe' with the actual path to your .exe file
        subprocess.Popen([r'C:\Users\Administrador\Documents\GNX-SCREENSHOT\main\main.exe'])
        print("Scheduled task executed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Define the days on which you want to repeat the execution
days_to_repeat = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  # Replace with your desired days

# Schedule the initial execution (optional)
# execute_exe()

# Schedule the repeated execution on specific days
for day in days_to_repeat:
    # Create a daily schedule for each specified day
    schedule.every().monday.at('15:00').do(execute_exe)
    schedule.every().tuesday.at('15:00').do(execute_exe)
    schedule.every().wednesday.at('15:00').do(execute_exe)
    schedule.every().thursday.at('15:00').do(execute_exe)
    schedule.every().friday.at('11:52').do(execute_exe)

# Run the scheduled tasks continuously
while True:
    schedule.run_pending()
    time.sleep(1)
