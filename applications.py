import os
import urllib.parse


def find_exe_file(app_name, search_directories):
    # Loop through each directory to search for the .exe file
    for directory in search_directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower() == f"{app_name.lower()}.exe":
                    return os.path.join(root, file)
    return None

def open_webpage(command):
    if "listen to some music" in command.lower():
        os.system('start firefox https://music.youtube.com')
    elif "open youtube" in command.lower():
        os.system('start firefox https://www.youtube.com')
    elif "open chat gpt" in command.lower():
        os.system('start firefox https://chat.openai.com')
    elif "open sharepoint" in command.lower():
        os.system('start firefox https://solvitursystems.sharepoint.com/sites/Assistance/Shared%20Documents/Forms/AllItems.aspx?OR=Teams%2DHL&CT=1680307118436&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzAzMDUwMTExMCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&viewid=2ad0b798%2D9dd1%2D42b0%2D852e%2Dd9c343ac885e')
    elif "company website" in command.lower():
        os.system('start firefox https://www.solvitursystems.com')
    elif "open SolvAssess" in command.lower():
        os.system('start firefox https://solvassess.com/')
    elif "open Netflix" in command.lower():
        os.system('start firefox https://www.netflix.com')
    else:
        # If the command doesn't match any predefined web actions, perform a web search
        search_query = command.replace("open ", "", 1)
        encoded_query = urllib.parse.quote(search_query)
        os.system(f'start firefox https://www.google.com/search?q={encoded_query}')

def open_application(command):
    command = command.lower()
    words = command.split()
    
    try:
        verb_index = words.index('open') if 'open' in words else words.index('close')
    except ValueError:
        print("Command verb (open/close) not found!")
        return
    
    app_name = ' '.join(words[verb_index + 1:])
    
    if not app_name:
        print("Application name not specified!")
        return

    # First, try to find and open/close the application
    search_directories = ['C:/Program Files', 'C:/Program Files (x86)', 'C:/Users/User/AppData/Local']
    exe_path = find_exe_file(app_name, search_directories)
    
    if exe_path:
        if 'open' in words:
            os.system(f"start {exe_path}")
        elif 'close' in words:
            os.system(f"taskkill /im {os.path.basename(exe_path)} /f")
    else:
        # If the application is not found, try opening a webpage instead
        open_webpage(command)