from googletrans import Translator

translator = Translator()

while True:
    text = input("Enter text to translate (press Enter to quit): ").strip()
    if not text:
        print("Exiting...")
        break

    translated = translator.translate(text, src='en', dest='bn')
    print("Bangla Translation:", translated.text)
