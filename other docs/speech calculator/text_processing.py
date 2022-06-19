import speech_recognition as sr


def addition(parameters):
    print("Addition called", parameters)
    return sum(parameters)


def subtraction(parameters, inv=False):
    print("Subtraction called", parameters)
    if inv:
        return parameters[1] - parameters[0]
    return parameters[0] - parameters[1]


def multiplication(parameters):
    print("Multiplication called", parameters)
    return parameters[0] * parameters[1]


def division(parameters):
    print("Division called", parameters)
    return parameters[0] / parameters[1]


def audio_to_text():
    text = None
    init_rec = sr.Recognizer()
    print("Let's speak!!")
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        print("Recognizing your text.............")
        text = init_rec.recognize_google(audio_data)

    print(text)
    return text.split()


text_list = audio_to_text()

add_KW = {"sum", "add", "summation", "addition", "plus", "+"}
sub_KW = {"subtraction", "difference", "subtract", "-"}
mul_KW = {
    "product", "multiplication", "multiplied by", "into", "multiply", "x", "times", "X"}
div_KW = {"quotient", "divided by", "by", "upon", "/"}
log_KW = {"log", "logarithm", "ln"}

parameters = []
key_words = []

i = 0
N = len(text_list)
inv = False
while i < N:
    try:
        parameters.append(float(text_list[i]))

    except:
        if text_list[i] in add_KW or text_list[i] in sub_KW or text_list[i] in mul_KW or text_list[i] in div_KW:
            key_words.append(text_list[i])

    if text_list[i] == "from":
        inv = True
    i += 1

print(parameters)
print(key_words)

print(key_words[0])
if key_words[0] in add_KW:
    print(addition(parameters))
elif key_words[0] in sub_KW:
    print(subtraction(parameters, inv))
elif key_words[0] in mul_KW:
    print(multiplication(parameters))
elif key_words[0] in div_KW:
    print(division(parameters))
