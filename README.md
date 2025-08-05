**🎙️ Speech to Indian Sign Language Translator 🤟**
An assistive AI application that captures live speech or audio recordings, converts it into text, and displays the relevant Indian Sign Language (ISL) through images or GIFs — bridging the communication gap between the hearing and speech-impaired community.

**🧠 Overview**
Indian Sign Language (ISL) is the primary mode of communication for the deaf and hard-of-hearing individuals. However, since it requires dedicated learning and practice, most people are unable to use it effectively, creating a communication barrier.

This project aims to translate spoken audio into ISL using speech recognition and natural language processing. The application visually represents the spoken content in ISL format, making communication more inclusive and accessible.

**🚀 Features**
🎤 Live speech input using microphone (via PyAudio)

🌐 Online speech recognition using Google Speech API

📴 Offline support using CMU Sphinx

🧠 Text preprocessing and phrase detection using NLP

📚 Dictionary-based machine translation to ISL

🖼️ ISL output shown using images or GIFs

🖱️ Easy GUI interface with EasyGUI

👋 Voice command to exit the application (say "goodbye" to close)

**🎯 Objectives**
Provide information access and services to deaf individuals in Indian Sign Language.

Build a scalable and extendable system that can later include the complete ISL vocabulary including manual and non-manual signs.

Create an offline-capable desktop application to ensure accessibility even in low-connectivity regions.

Promote inclusive communication between hearing and speech-impaired individuals.

**🛠️ Technology Stack**
**Component	         Description**
Frontend	            EasyGUI for user interaction
Audio Input	         Microphone via PyAudio
Speech Recognition	Google Speech API (online) & CMU Sphinx (offline)
Text Processing	   Natural Language Processing (NLP)
Translation Logic	   Dictionary-based ISL mapping
Output            	ISL images/GIFs displayed in sequence

**📈 Working Algorithm**
🔁 Audio-to-Sign Language Workflow
Start the application
Calibrate microphone for ambient noise
Capture live speech through microphone
Convert speech to text (online)
Text preprocessing (convert to lowercase, clean text)
Check for termination keyword ("goodbye" to exit)
**Translate text:**
If phrase exists in dictionary → Show corresponding ISL GIFs
Else → Break into characters and show ISL letters with slight delay
Repeat steps until terminated

**🧪 How to Run**
Download or clone this repository.
Open a terminal in the project directory.

**Run the application using:**
python main.py

Use the GUI to begin recording.

Speak into your microphone.

Observe the ISL output as images or animations.

Say **"goodbye"** to exit the application.

**❤️ Contribution & Support**
Contributions are welcome to extend this initiative. If you're passionate about accessible communication and inclusive tech, feel free to fork and submit a pull request!

