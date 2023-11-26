from flask import Flask, render_template, request
from googletrans import Translator
import random

app = Flask(__name__)

# Function to get user's preferred language
def select_language(choice):
    language_code = {
        '1': 'es',
        '2': 'fr',
        '3': 'en',
        '4': 'de',
        '5': 'ja',
        '6': 'zh-tw',
        '7': 'pt'
    }.get(choice, 'es')  # Default to English if invalid choice

    return language_code

def translate_text(text, dest_language):
    if text and text.strip():
        try:
            translator = Translator()
            detected_lang = translator.detect(text)
            if detected_lang and detected_lang.lang == dest_language:
                return text  # Return the input text if it's already in the destination language
            else:
                translated_text = translator.translate(text, dest=dest_language).text
                return translated_text
        except Exception as e:
            print(f"Translation Error: {e}")
            if dest_language == 'es':
                return text
            else:
                return f"Translation Error: {e}"
    else:
        return text




# Function to greet the user in the selected language
def greet_user(language_code):
    english_greeting = "Hello, I'm a mental health chatbot. My purpose is to give you motivational phrases to try to enjoy your day and improve your feelings. 🫀"
    return translate_text(english_greeting, language_code)

# Function to provide text of buttons and more in the correct language
def button_translate(language_code):
    english_txt_button = translate_text("Get an advice 💡", language_code)
    return english_txt_button

def txt_translate_1(language_code) :
    english_txt_option_1 = translate_text("Get a motivational phrase for depression ❤️‍🩹", language_code)
    return english_txt_option_1

def txt_translate2(language_code) :
    english_txt_option_2 = translate_text("Get a motivational phrase for anxiety ❤️‍🩹", language_code)
    return english_txt_option_2

def button_back_translate(language_code) :
    btn_back_translate = translate_text("Go Back 🔙", language_code)
    return btn_back_translate

def wait_translate(language_code) :
    wait_translate_txt = translate_text("Wait Please ... ⏰", language_code)
    return wait_translate_txt

def translate_disclaimer(language_code) : 
    disclaimer_txt = translate_text(" ⚠️⚠️⚠️ If you are experiencing a mental health crisis, remember you are not alone. Please seek immediate help. Call emergency services at 911 or contact a helpline like 131 for mental health support.", language_code)
    return disclaimer_txt


# Function to provide random advice for mental health issues
def mental_health_advice(language_code, issue):
    english_advice = {
        'depression': [
                    "Taking small steps every day can make a big difference. Try doing something you enjoy, even if it's for a few minutes. 🌟",
                    "Set achievable goals for yourself. Celebrate small victories. 🎉",
                    "Connect with others. Social support is crucial for mental well-being. 🤝",
                    "Your journey is unique; don't compare it to others'. Embrace your progress. 🌈",
                    "Find joy in simple moments; they add up to create a fulfilling life. ☀️",
                    "Every obstacle you overcome strengthens your resilience. Keep pushing forward. ⛰️",
                    "Remind yourself: it's okay to ask for help when you need it. 🆘",
                    "Celebrate your strengths and accomplishments, no matter how small. 🎊",
                    "Practice self-compassion; treat yourself with kindness and understanding. 🌺",
                    "Remember, setbacks are temporary. Keep your focus on the journey ahead. 🔄",
                    "Embrace a routine that nurtures your well-being. Consistency can bring comfort. 🕰️",
                    "You're not alone; there's a community of support ready to lift you up. 🌟",
                    "Remind yourself of the things that bring you happiness and purpose. 🌟",
                    "Reflect on your progress; every step forward is a testament to your strength. 🚶‍♂️",
                    "Even on tough days, your presence in this world matters. 🌍",
                    "Seek moments of laughter and joy; they're powerful healers. 😄",
                    "Allow yourself grace on the hard days; it's part of the journey. 🙏",
                    "Your journey may have obstacles, but they're stepping stones to growth. 🌱",
                    "Trust in your ability to navigate through life's challenges. 🌟",
                    "Believe in your resilience; you've overcome difficulties before. 💪",
                    "Every sunrise brings new opportunities; seize them. 🌅",
                    "Your strength shines through your vulnerabilities. 💪",
                    "Even on cloudy days, your light can break through. ☁️☀️",
                    "Patience with yourself is a crucial part of healing. ⏳",
                    "Your journey is a mosaic; every piece counts. 🖼️",
                    "Each breath you take is a testament to your resilience. 🌬️",
                    "The pursuit of healing is a brave endeavor. 🌱",
                    "You're sculpting a masterpiece from life's challenges. 🎨",
                    "Believe in your ability to rise from the shadows. 🌑✨",
                    "Nurture your soul; it's a garden waiting to bloom. 🌻",
                    "Even small steps forward lead to monumental progress. 👣",
                    "Your scars tell a story of survival and strength. ✨",
                    "There's power in asking for help; it's a sign of courage. 🆘",
                    "You're the architect of your resilience. 🏗️",
                    "Allow yourself to rest; it's part of the journey. 🛌",
                    "Your journey's rhythm is unique; embrace it. 🎶",
                    "The journey might be tough, but you're tougher. 💥",
                    "Every day is a canvas; paint it with hope. 🎨",
                    "Your perseverance is an inspiration to many. 🌟",
                    "The road might be winding, but it leads to growth. 🛣️"
        ],
        'anxiety': [
             "Remember, it's okay to feel overwhelmed sometimes. Take a moment to breathe deeply and focus on the present. 🌬️",
                "Practice self-care. Do something that brings you joy and relaxation. 🛀",
                "Talk to someone you trust about your feelings. Sharing can help lighten the burden. 🗨️",
                "Focus on what you can control; let go of what's beyond your reach. 🎯",
                "Mindfulness can ground you in the present, easing anxiety. 🧘",
                "Challenge negative thoughts with positive affirmations. 🌟",
                "Establish boundaries; prioritize your mental well-being. 🚫",
                "Visualize success and focus on positive outcomes. 🎯",
                "Practice deep breathing exercises to calm your mind and body. 🌅",
                "Engage in activities that bring a sense of calmness and peace. 🌿",
                "Trust in your capacity to adapt and handle uncertainty. 🛡️",
                "Seek out support groups or communities; knowing you're not alone can be comforting. 🤗",
                "Take breaks; give yourself moments of rest and rejuvenation. ☕",
                "Avoid dwelling on things beyond your control; focus on what you can influence. 🌐",
                "Remind yourself: anxiety doesn't define you; it's a part of your journey. 🌟",
                "Set realistic expectations for yourself; perfection isn't necessary. 🎯",
                "Embrace imperfections; they make you unique and special. 🌺",
                "Identify triggers and work on strategies to manage them effectively. 🎢",
                "Inhale courage, exhale fear. Repeat until calmness fills your being. 💨",
                "Your strength in facing anxiety is a testament to your resilience. 🌟",
                "Remember, it's okay to feel overwhelmed sometimes. Take a moment to breathe deeply and focus on the present. 🌬️",
                "Practice self-care. Do something that brings you joy and relaxation. 🛀",
                "Talk to someone you trust about your feelings. Sharing can help lighten the burden. 🗨️",
                "Focus on what you can control; let go of what's beyond your reach. 🎯",
                "Mindfulness can ground you in the present, easing anxiety. 🧘",
                "Challenge negative thoughts with positive affirmations. 🌟",
                "Establish boundaries; prioritize your mental well-being. 🚫",
                "Visualize success and focus on positive outcomes. 🎯",
                "Practice deep breathing exercises to calm your mind and body. 🌅",
                "Engage in activities that bring a sense of calmness and peace. 🌿",
                "Trust in your capacity to adapt and handle uncertainty. 🛡️",
                "Seek out support groups or communities; knowing you're not alone can be comforting. 🤗",
                "Take breaks; give yourself moments of rest and rejuvenation. ☕",
                "Avoid dwelling on things beyond your control; focus on what you can influence. 🌐",
                "Remind yourself: anxiety doesn't define you; it's a part of your journey. 🌟",
                "Set realistic expectations for yourself; perfection isn't necessary. 🎯",
                "Embrace imperfections; they make you unique and special. 🌺",
                "Identify triggers and work on strategies to manage them effectively. 🎢",
                "Inhale courage, exhale fear. Repeat until calmness fills your being. 💨",
                "Your strength in facing anxiety is a testament to your resilience. 🌟"
        ]
    }

     # Translate all advice strings for the chosen issue
    translated_advice = [translate_text(advice, language_code) for advice in english_advice.get(issue, [])]

    selected_phrase = random.choice(translated_advice or ["Sorry, advice for this issue is not available."])
    return selected_phrase

@app.route('/')

def index():
    title = translate_text("Mental Health Chatbot", 'es')
    select_language = translate_text("Select your preferred language:", 'es')
    start_chat = translate_text("Start Chat", 'es')
    lang_1 = translate_text("Español", 'es')
    lang_2 = translate_text("French", 'fr')
    lang_3 = translate_text("English", 'en')
    lang_4 = translate_text("German", 'de')
    lang_5 = translate_text("Japanese", 'ja')
    lang_6 = translate_text("Chinese", 'zh-tw')
    lang_7 = translate_text("Portuguese", 'pt')
    
    return render_template('index.html', title=title, select_language=select_language, start_chat=start_chat,
                           lang_1=lang_1, lang_2=lang_2, lang_3=lang_3, lang_4=lang_4, lang_5=lang_5,
                           lang_6=lang_6, lang_7=lang_7)

@app.route('/chat', methods=['POST'])
def chat():
    choice = request.form.get('choice')  # Using get() to avoid KeyError
    language = select_language(choice)
    greeting = greet_user(language)
    get_advice_depression = txt_translate_1(language)
    get_advice_anxiety = txt_translate2(language)
    get_advice = button_translate(language)
    wait = wait_translate(language)
    return render_template('index.html', greeting=greeting, get_advice_anxiety=get_advice_anxiety, get_advice_depression=get_advice_depression, get_advice=get_advice, wait=wait, language=language)

@app.route('/advice', methods=['POST'])
def advice():
    language = request.form.get('language')
    issue = request.form.get('issue')
    selected_advice = mental_health_advice(language, issue)
    continue_chat = button_back_translate(language)
    disclaimer = translate_disclaimer(language)
    year = "2023"
    
    return render_template('index.html', advice=selected_advice,  continue_chat=continue_chat, disclaimer=disclaimer, year=year,  language=language)

if __name__ == '__main__':
    app.run(debug=True)
