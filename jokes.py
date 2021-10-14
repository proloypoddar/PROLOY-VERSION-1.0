# importing installed library
import pyttsx3
import pyjokes
  
# using get_joke() to generate a single joke
#language is english
#category is neutral
My_joke = pyjokes.get_joke(language="en", category="all")
  
pyttsx3.speak(My_joke)