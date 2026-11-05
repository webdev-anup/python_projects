from gtts import gTTS  # Yahan 'gTTs' ki jagah 'gTTS' karna hai

text = "Hello, how are you today?, Welcome To Python Programming Language!"

tts = gTTS(text=text, lang='en')

tts.save("voice.mp3")

print("Audio file saved as voice.mp3")