# VirtualKeyboard
A smart, contactless virtual keyboard built using OpenCV, cvzone, and MediaPipe, allowing users to type by hovering their index finger over keys for 2 seconds. Ideal for touchless interaction systems, accessibility interfaces, or creative human-computer interaction experiments.

🎯 Features
🖐️ Hand Tracking using cvzone and MediaPipe

⌨️ Virtual keyboard interface with multiple key rows

🕒 Hover-based typing (hold index finger over a key for 2 seconds to select)

⌫ Backspace support

✨ Smooth UI with a transparent text box overlay

🎮 Uses pynput to send actual keyboard inputs to your system


🛠️ Technologies Used
Python 3.11+

OpenCV

cvzone

MediaPipe

pynput

📦 Installation

git clone https://github.com/Anirudh-saiA/VirtualKeyboard
cd virtual-ai-keyboard
pip install -r requirements.txt
python main.py
Make sure your webcam is connected and working!

✅ Requirements
Install all dependencies with:
pip install opencv-python cvzone mediapipe pynput

🧪 How It Works
Webcam captures your hand movements.

cvzone + MediaPipe track landmarks of your hand.

If your index finger (tip) hovers over a key for more than 2 seconds, that key is triggered.

The key is typed using pynput.

Typed text is displayed on a semi-transparent overlay at the bottom.


