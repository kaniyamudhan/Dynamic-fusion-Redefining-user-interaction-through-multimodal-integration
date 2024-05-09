
# Eye-Controlled Mouse and Voice Recognition

This project combines eye-tracking technology with voice recognition to create an interactive system that allows users to control their computer using eye movements and voice commands.




## Features

- Eye Tracking: The system uses a webcam and the MediaPipe library to track eye movements, allowing users to move the mouse cursor with their eyes and perform actions such as clicking by blinking.
- Voice Recognition: Utilizes the SpeechRecognition library to recognize voice commands spoken by the user. Commands include opening applications, performing system actions (e.g., shutdown, restart), controlling volume/brightness, and more.
- Integration with PyAutoGUI: PyAutoGUI is used to simulate mouse clicks, keyboard inputs, and system controls based on the user's eye movements and voice commands.


## Requirements

- Python 3.x
- OpenCV (pip install opencv-python)
- MediaPipe (pip install mediapipe)
- PyAutoGUI (pip install pyautogui)
- SpeechRecognition (pip install SpeechRecognition)
## Usage notes

- Make sure to run the scripts in a well-lit environment for optimal eye tracking accuracy.
- Calibration may be required for accurate eye movement detection.
- Voice commands should be spoken clearly and in a language supported by the SpeechRecognition library.
## Screenshots

![capture_240508_211208](https://github.com/kaniyamudhan/Dynamic-fusion-Redefining-user-interaction-through-multimodal-integration/assets/112994943/402da0fb-6921-4839-8a38-54d8a315662d)

![capture_240508_112700](https://github.com/kaniyamudhan/Dynamic-fusion-Redefining-user-interaction-through-multimodal-integration/assets/112994943/992d7467-0d01-438d-8e29-53e5a2ab3d92)


## Acknowledgements

 - [Mediapipe](https://developers.google.com/mediapipe)
 - [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
 - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)


## License

[MIT](https://github.com/kaniyamudhan/Dynamic-fusion-Redefining-user-interaction-through-multimodal-integration/blob/main/LICENSE)

