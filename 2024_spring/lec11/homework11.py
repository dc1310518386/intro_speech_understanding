import speech_recognition

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    recognizer = speech_recognition.Recognizer()
    
    # Load audio file
    with speech_recognition.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    
    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except speech_recognition.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return None