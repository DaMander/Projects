morse_code_translations = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

def string_to_morse():
    text = str(input("Enter your message: ")).lower()
    string_to_send = ""
    for string in text:
        if string == " ":
            string_to_send += " / "
        else:
            string_to_send += morse_code_translations[string]
            string_to_send += " "
    return string_to_send


def morse_to_string():
    morse_code = str(input("Enter morse code: "))
    text = ""
    morse_code = morse_code.split(" ")
    for word in morse_code:
        if word == "/":
            text += " "
        else:
            for letter, morse in morse_code_translations.items():
                if morse == word:
                    text += letter
    return text


print(string_to_morse())
print(morse_to_string())