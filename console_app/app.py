from googletrans import Translator
import random

# Function to get user's preferred language
def select_language():
    print("Select your preferred language:")
    print("1. English")
    print("2. French")
    print("3. Español")
    print("4. Deutsch")
    print("5. 日本語")
    print("6. 中國人")
    print("7. Português")
    choice = input("Enter your choice: ")

    # Assign language code based on user's choice
    language_code = {
        '1': 'en',
        '2': 'fr',
        '3': 'es',
        '4': 'de',
        '5': 'ja',
        '6': 'zh-tw',
        '7': 'pt'
    }.get(choice, 'en')  # Default to English if invalid choice

    return language_code

# Function to translate text to the selected language
def translate_text(text, dest_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language).text
    return translated_text

# Function to greet the user in the selected language
def greet_user(language_code):
    english_greeting = "Hello, I'm a mental health chatbot. My purpose is to give you motivational phrases to try to enjoy your day and improve your feelings."
    return translate_text(english_greeting, language_code)

def mental_health_advice(language_code, issue):
    # English advice for mental health issues
    english_advice = {
        'depression': [
            "Taking small steps every day can make a big difference. Try doing something you enjoy, even if it's for a few minutes. 🌟",
            "Set achievable goals for yourself. Celebrate small victories. 🎉",
            "Connect with others. Social support is crucial for mental well-being. 🤝",
            "Your journey is unique; don't compare it to others'. Embrace your progress. 🌈"
        ],
        'anxiety': [
            "Remember, it's okay to feel overwhelmed sometimes. Take a moment to breathe deeply and focus on the present. 🌬️",
            "Practice self-care. Do something that brings you joy and relaxation. 🛀",
            "Talk to someone you trust about your feelings. Sharing can help lighten the burden. 🗨️",
            "Focus on what you can control; let go of what's beyond your reach. 🎯",
            "Mindfulness can ground you in the present, easing anxiety. 🧘"
        ]
    }

    # Pre-translate advice for the chosen language
    translated_advice = {
        'depression': [translate_text(advice, language_code) for advice in english_advice['depression']],
        'anxiety': [translate_text(advice, language_code) for advice in english_advice['anxiety']]
    }

    selected_phrase = random.choice(translated_advice.get(issue, ["Sorry, advice for this issue is not available."]))
    return selected_phrase


# Get user's preferred language
language = select_language()

# Greet the user in the selected language
print(greet_user(language))

# Example conversation loop
while True:
    choice = input(translate_text("Choose an option:\n1. Get Advice for Anxiety\n2. Get Advice for Depression\nEnter your choice (1 or 2): ", language))

    if choice == '1':
        print(mental_health_advice(language, 'anxiety'))
    elif choice == '2':
        print(mental_health_advice(language, 'depression'))
    else:
        print(translate_text("Invalid choice. Please choose 1 or 2.", language))

    user_input = input(translate_text("Would you like to continue? (1==Yes || 0==No): ", language))
    if user_input.lower() != '1':
        break
