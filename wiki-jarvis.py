import speech_recognition as sr 
import pyttsx3

import wikipedia
  
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      

Intro="Hey user, .. This is Python jarvis AI made by Dewashish Jaiswal....How can i help you?"
print(Intro)
SpeakText(Intro)
print()
Help1="i can help you regarding your internet searches based on wikipedia.. "
print(Help1)
SpeakText(Help1)
print()

while True:
 print("Say wikipedia to search or say quit to exit from Jarvis AI")
 SpeakText("Say wikipedia to search..... or...... say quit to exit from Jarvis AI")
 print()
 try:
    with sr.Microphone() as s1:
        r.adjust_for_ambient_noise(s1,duration=0.2)
        a1=r.listen(s1)
        mt1=r.recognize_google(a1)
        if mt1.lower()=="wikipedia":
                print("Welcome to wikipedia....... What do you want to know?")
                SpeakText("Welcome to wikipedia....... What do you want to know?")
    # Exception handling to handle 
    # exceptions at the runtime 
                try: 
          
        # use the microphone as source for input.
                    with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
                     r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
                     audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
                     MyText = r.recognize_google(audio2) 
                     MyText = MyText.lower()
                     z = wikipedia.summary(MyText,sentences=2)
  
                     print("Did you say "+z) 
                     SpeakText(z) 
              
                except sr.RequestError as e: 
                    print("Could not request results; {0}".format(e)) 
          
                except sr.UnknownValueError: 
                    print("unknown error occured")
        elif mt1.lower()=="quit":
            
            break            
        else:
            print("say again")
            SpeakText("Say Again")
 except sr.RequestError as e: 
                    print("Could not request results; {0}".format(e)) 
          
 except sr.UnknownValueError: 
                    print("unknown error occured")
