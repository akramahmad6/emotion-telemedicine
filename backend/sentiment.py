def analyze_emotion(text):
    text = text.lower()

    stress_words = ['stressed', 'anxious', 'panic', 'overwhelmed', 
                    'worried', 'cant sleep', 'nervous', 'fear', 
                    'anxiety', 'tension', 'pressure']
    
    negative_words = ['sad', 'depressed', 'bad', 'terrible', 'awful', 
                      'pain', 'hurt', 'sick', 'tired', 'lonely', 
                      'unhappy', 'miserable', 'upset', 'crying']
    
    positive_words = ['good', 'great', 'better', 'happy', 'fine', 
                      'well', 'excellent', 'wonderful', 'recovered',
                      'improving', 'healthy', 'cheerful', 'okay']

    if any(word in text for word in stress_words):
        return {'emotion': 'STRESS', 'confidence': 0.90}
    
    if any(word in text for word in negative_words):
        return {'emotion': 'NEGATIVE', 'confidence': 0.85}
    
    if any(word in text for word in positive_words):
        return {'emotion': 'POSITIVE', 'confidence': 0.88}
    
    return {'emotion': 'NEUTRAL', 'confidence': 0.70}