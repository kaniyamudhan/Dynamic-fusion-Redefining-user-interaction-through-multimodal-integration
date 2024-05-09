# Dynamic-fusion-Redefining-user-interaction-through-multimodal-integration

Eye-Controlled Mouse and Voice Recognition
This project combines eye-tracking technology with voice recognition to create an interactive system that allows users to control their computer using eye movements and voice commands.

Features
Eye Tracking: The system uses a webcam and the MediaPipe library to track eye movements, allowing users to move the mouse cursor with their eyes and perform actions such as clicking by blinking.
Voice Recognition: Utilizes the SpeechRecognition library to recognize voice commands spoken by the user. Commands include opening applications, performing system actions (e.g., shutdown, restart), controlling volume/brightness, and more.
Integration with PyAutoGUI: PyAutoGUI is used to simulate mouse clicks, keyboard inputs, and system controls based on the user's eye movements and voice commands.
Requirements
Python 3.x
OpenCV (pip install opencv-python)
MediaPipe (pip install mediapipe)
PyAutoGUI (pip install pyautogui)
SpeechRecognition (pip install SpeechRecognition)
Setup and Usage
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Connect a webcam to your computer for eye tracking.
Run the eye_tracking.py script to start the eye-tracking functionality.
Run the voice_recognition.py script to start the voice recognition functionality.
Follow the on-screen instructions for calibration and voice command recognition.
Enjoy controlling your computer using eye movements and voice commands!
Usage Notes
Make sure to run the scripts in a well-lit environment for optimal eye tracking accuracy.
Calibration may be required for accurate eye movement detection.
Voice commands should be spoken clearly and in a language supported by the SpeechRecognition library.
Acknowledgements
This project uses the MediaPipe library for face and landmark detection.
PyAutoGUI is utilized for simulating mouse and keyboard inputs.
SpeechRecognition library is used for voice command recognition.
License
This project is licensed under the MIT License.

