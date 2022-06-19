import speech_recognition as sr
from word2number import w2n
import inflect
num2word = inflect.engine()

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
        audio_data = init_rec.record(source, duration=10)
        print("Recognizing your text.............")
        text = init_rec.recognize_google(audio_data)

    print(text)
    return text.split()


text_list = audio_to_text()
# text_list = "million divided by 12 + million into two".split()
# print("million divided by 12 + million into two")

add_KW = {"sum", "add", "summation", "addition", "plus", "+"}
sub_KW = {"subtraction", "difference", "subtract", "-"}
mul_KW = {
    "product", "multiplication", "multiplied by", "into", "multiply", "x", "times"}
div_KW = {"quotient", "divided by", "by", "upon", "/"}

parameters = []
key_words = []

i = 0
N = len(text_list)
inv = False
expr = []
operand = 0
wordtonum = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
while i < N:
    try:
        try:
            # print(text_list[i])
            parameters.append(float(text_list[i]))
            # expr.append(float(w2n.word_to_num(text_list[i])))
        except:
            
            parameters.append(float(wordtonum[text_list[i]]))
            
            # expr.append(float(text_list[i]))
        # print(0, parameters)
    except:
        if not(text_list[i] in add_KW or text_list[i] in sub_KW or text_list[i] in mul_KW or text_list[i] in div_KW):
            
                # print(1, text_list[i])
                word= ""
                if len(parameters)!=0:
                    # print(''.join(map(str, map(int, parameters))))
                    word = num2word.number_to_words(''.join(map(str, map(int, parameters))))
                    # print(2, word)
                opr = float(w2n.word_to_num(word+ " " + text_list[i]))
                # print("opr", opr)
                parameters = []
                # expr.append(opr)
                parameters.append(opr)
            # except:
            #     pass
        else:
                
                # print(parameters)
                # print(1, text_list[i])
                # print(''.join(map(str, map(float, parameters))))
                word = num2word.number_to_words(''.join(map(str, map(float, parameters))))
                # print(2, word)
                opr = float(w2n.word_to_num(word))
                # print("opr", opr)
                parameters = []
                expr.append(opr)

        if text_list[i] in add_KW or text_list[i] in sub_KW or text_list[i] in mul_KW or text_list[i] in div_KW:
            # key_words.append(text_list[i])
            if text_list[i]  in add_KW:
                expr.append('+')

    
            elif text_list[i] in sub_KW:
                expr.append('-')
            elif text_list[i] in mul_KW:
                expr.append('*')
            elif text_list[i] in div_KW:
                expr.append('/')
                


    if text_list[i] == "from":
        inv = True
    i += 1
# print(parameters)

# print(''.join(map(str, map(int, parameters))))
word = num2word.number_to_words(''.join(map(str, map(float, parameters))))
# print(2, word)
opr = float(w2n.word_to_num(word))
# print("opr", opr)
parameters = []
expr.append(opr)
print(expr)

class Conversion:
     
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
     
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
     
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
     
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
     
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False
             
    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
         
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if type(i) == float:
                self.output.append(i)
             
            # If the character is an '(', push it to stack
            elif i  == '(':
                self.push(i)
 
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and
                                self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
 
        # print "".join(self.output)


class Evaluate:
     
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
     
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
     
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
     
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
     
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
 
    # The main function that converts given infix expression
    # to postfix expression
    def evaluatePostfix(self, exp):
         
        # Iterate over the expression for conversion
        for i in exp:
             
            # If the scanned character is an operand
            # (number here) push it to the stack
            if type(i)==float:
                self.push(i)
 
            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(eval(str(val2) + i + str(val1)))
 
        return float(self.pop())
 
# Driver program to test above function
exp = expr
obj = Conversion(len(exp))
obj.infixToPostfix(exp)
print(obj.output)
exp = obj.output
obj = Evaluate(len(exp))
print(obj.evaluatePostfix(exp))
