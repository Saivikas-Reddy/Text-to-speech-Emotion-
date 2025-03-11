import streamlit as st
 import pyttsx3

 def speak_with_emotion(text, emotion):
  #   """Speak text with the selected emotion."""
    engine = pyttsx3.init()
    
     # Set default voice parameters
     engine.setProperty('rate', 175)
     engine.setProperty('volume', 1.0)
    
     response = ""
    
     if emotion == "Happy":
         engine.setProperty('rate', 190)  # Increase speed
         engine.setProperty('volume', 1.2)  # Increase volume
         response = "That sounds wonderful!"
     elif emotion == "Sad":
         engine.setProperty('rate', 140)  # Decrease speed
         engine.setProperty('volume', 0.8)  # Lower volume
         response = "I'm here for you."
     elif emotion == "Angry":
         engine.setProperty('rate', 200)  # Faster speech
         engine.setProperty('volume', 4)  # Louder
         response = "Take a deep breath."
     elif emotion == "Neutral":
         response = "Got it."
    
     engine.say(f" {text}")
     if response:
         engine.say(response)
     engine.runAndWait()
     engine.stop()

# # Streamlit UI
 st.title("Text to Speech with Emotion Selection")

 text_input = st.text_area("Enter text to speak:")

 emotion = st.selectbox("Select an emotion:", ["Happy", "Sad", "Angry", "Neutral"])

 if st.button("Speak"):
     if text_input.strip():
         speak_with_emotion(text_input, emotion)
         st.success("Speaking...")
     else:
         st.warning("Please enter some text.")
