import cv2
import mediapipe as mp
import pyautogui
import threading
import subprocess
import speech_recognition as sr

# Initialize webcam
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Initialize speech recognition
listener = sr.Recognizer()

# Function to handle eye tracking
def eye_tracking():
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape

        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[158]]  # Left eye landmarks for blink
            left_x = [int(l.x * frame_w) for l in left]
            left_y = [int(l.y * frame_h) for l in left]
            cv2.circle(frame, (left_x[0], left_y[0]), 3, (0, 255, 255), -1)  # Draw left dot 1
            cv2.circle(frame, (left_x[1], left_y[1]), 3, (0, 255, 255), -1)  # Draw left dot 2
            cv2.line(frame, (left_x[0], left_y[0]), (left_x[1], left_y[1]), (0, 255, 255), 2)  # Draw line between dots
            if (left[0].y - left[1].y) < 0.015:
                # Click if both dots are touched by the line (yellow line is close to both dots)
                if left_y[0] < left_y[1] < left_y[0] + 5 or left_y[1] < left_y[0] < left_y[1] + 5:
                    pyautogui.click()
                    pyautogui.sleep(1)  # Optional sleep after click

        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)
# Function to handle voice recognition
def voice_recognition():
    while True:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice).lower()
                print('Command:', command)
                if 'open google' in command:
                    subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", "https://www.google.com"])
                    print('Google opened!')
                elif 'open youtube' in command:
                    subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", "https://www.youtube.com"])
                    print('YouTube opened!')
                elif 'open whatsapp' in command:
                    subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", "https://web.whatsapp.com/"])
                    print('WhatsApp opened!')
                elif 'open cmd' in command:
                    subprocess.Popen(["cmd.exe"])
                    print('Command Prompt opened!')
                elif 'search on google' in command:
                    search_query = command.replace('search on google', '')
                    subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", f"https://www.google.com/search?q={search_query}"])
                    print(f'Searching on Google: {search_query}')
                elif 'open calculator' in command:
                    subprocess.Popen(["calc.exe"])
                    print('Calculator opened!')
                elif 'open notepad' in command:
                    subprocess.Popen(["notepad.exe"])
                    print('Notepad opened!')
                elif 'open file explorer' in command:
                    subprocess.Popen(["explorer.exe"])
                    print('File Explorer opened!')
                elif 'open task manager' in command:
                    subprocess.Popen(["taskmgr.exe"])
                    print('Task Manager opened!')
                elif 'open settings' in command:
                    subprocess.Popen(["ms-settings:"])
                    print('Settings opened!')
                elif 'open control panel' in command:
                    subprocess.Popen(["control.exe"])
                    print('Control Panel opened!')
                elif 'open paint' in command:
                    subprocess.Popen(["mspaint.exe"])
                    print('Paint opened!')
                elif 'open word' in command:
                    subprocess.Popen(["winword.exe"])
                    print('Microsoft Word opened!')
                elif 'open excel' in command:
                    subprocess.Popen(["excel.exe"])
                    print('Microsoft Excel opened!')
                elif ('open power point') in command:
                    subprocess.Popen(["powerpnt.exe"])
                    print('Microsoft PowerPoint opened!')
                elif 'open visual studio code' in command:
                    subprocess.Popen(["code"])
                    print('Visual Studio Code opened!')
                elif 'open python idle' in command:
                    subprocess.Popen(["pythonw", "-m", "idlelib"])
                    print('Python IDLE opened!')
                elif 'shutdown' in command:
                    subprocess.Popen(["shutdown", "/s"])
                    print('Shutting down the computer!')
                elif 'restart' in command:
                    subprocess.Popen(["shutdown", "/r"])
                    print('Restarting the computer!')
                elif 'log off' in command:
                    subprocess.Popen(["shutdown", "/l"])
                    print('Logging off the computer!')
                elif 'hibernate' in command:
                    subprocess.Popen(["shutdown", "/h"])
                    print('Hibernating the computer!')
                elif 'sleep' in command:
                    subprocess.Popen(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])
                    print('Putting the computer to sleep!')
                elif 'volume up' in command:
                    pyautogui.press('volumeup')
                    print('Volume increased!')
                elif 'volume down' in command:
                    pyautogui.press('volumedown')
                    print('Volume decreased!')
                elif 'mute' in command:
                    pyautogui.press('volumemute')
                    print('Volume muted!')
                elif 'brightness up' in command:
                    pyautogui.press('brightnessup')
                    print('Brightness increased!')
                elif 'brightness down' in command:
                    pyautogui.press('brightnessdown')
                    print('Brightness decreased!')
                elif 'open camera' in command:
                    subprocess.Popen(["microsoft.windows.camera:"], shell=True)
                    print('Camera app opened!')
                elif 'take screenshot' in command:
                    pyautogui.screenshot("screenshot.png")
                    print('Screenshot taken!')
                elif ' click' in command:
                    pyautogui.click()
                    print('Left click performed!')
                elif 'right click' in command:
                    pyautogui.click(button='right')
                    print('Right click performed!')
                else:
                    print("Command not recognized.")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")

# Start eye tracking and voice recognition threads
eye_thread = threading.Thread(target=eye_tracking)
voice_thread = threading.Thread(target=voice_recognition)

eye_thread.start()
voice_thread.start()
