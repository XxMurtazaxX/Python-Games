import win32com.client as wincl
speaker = wincl.Dispatch("SAPI.SpVoice")

print("Welcome to RoboSpeaker by Murtaza!")

while True:
    x = input("What do you want me to speak: ")
    if x == 'q':
        break
    speaker.Speak(x)
