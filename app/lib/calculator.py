import math

# Class to convert the expression


class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

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
            return True if a <= b else False
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
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while((not self.isEmpty()) and
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
            if type(i) == float:
                self.push(i)

            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(eval(str(val2) + i + str(val1)))

        return float(self.pop())


add_KW = {"sum", "add", "summation", "addition", "plus", "+"}
sub_KW = {"subtraction", "difference", "subtract", "-"}
mul_KW = {
    "product", "multiplication", "multiplied by", "into", "multiply", "x", "times"}
div_KW = {"quotient", "divided by", "by", "upon", "/"}

sine_KW = {"sin", "sine", "sign"}
cos_KW = {"cos", "cosine", "cosign", "Cos"}
tan_KW = {"tan", "tangent"}
cosec_KW = {"cosec", "cosecant"}
sec_KW = {"sec", "secant"}
cot_KW = {"cot", "cotangent"}

asin_KW = {"arcsin", "arcsine", "arcsign"}
acos_KW = {"arccos", "arccosine", "arccosign"}
atan_KW = {"arctangent", "arctan"}
asec_KW = {"arcsecant", "arcsec"}
acosec_KW = {"arccosec", "arccosecant"}
acot_KW = {"arccot", "arccotangent"}


def calculate(text_list):
    for i in range(len(text_list)):
        if text_list[i].lower() == "e":
            text_list[i] = math.e
        elif text_list[i].lower() == "pie" or text_list[i].lower() == "pi":
            text_list[i] = math.pi

    print(text_list)

    parameters = []

    i = 0
    N = len(text_list)

    expr = []
    while i < N:
        if text_list[i] == "power":
            a, b, count = False, False, 0
            j, k = i - 1, i + 1
            while j > -1 and k < N and count != 2:
                try:
                    if type(a) != float:
                        a = float(text_list[j])
                        count += 1
                except:
                    j -= 1

                try:
                    if type(b) != float:
                        b = float(text_list[k])
                        count += 1
                except:
                    k += 1

            parameters.append(math.pow(a, b))
            expr.append(math.pow(a, b))

            i = k + 1
            continue

        elif text_list[i] == "raised":
            a, b, count = False, False, 0
            j, k = i - 1, i + 1
            while j > -1 and k < N and count != 2:
                try:
                    if type(a) != float:
                        a = float(text_list[j])
                        count += 1
                except:
                    j -= 1

                try:
                    if type(b) != float:
                        b = float(text_list[k])
                        count += 1
                except:
                    k += 1

            parameters.append(math.pow(a, b))
            expr.append(math.pow(a, b))

            i = k + 1
            continue

        elif text_list[i: i + 3] == ["square", "root", "of"]:
            parameters.append(math.sqrt(float(text_list[i + 3])))
            expr.append(math.sqrt(float(text_list[i + 3])))
            i += 4
            continue
        elif text_list[i: i + 2] == ["square", "root"] and text_list[i + 2] != "of":
            try:
                parameters.append(math.sqrt(float(text_list[i + 2])))
                expr.append(math.sqrt(float(text_list[i + 2])))
                i += 3
                continue
            except:
                pass

        elif text_list[i: i + 3] == ["cube", "root", "of"]:
            parameters.append(math.pow(float(text_list[i + 3]), (1 / 3)))
            expr.append(math.pow(float(text_list[i + 3]), (1 / 3)))
            i += 4
            continue
        elif text_list[i: i + 2] == ["cube", "root"] and text_list[i + 2] != "of":
            try:
                parameters.append(math.pow(float(text_list[i + 2]), (1 / 3)))
                expr.append(math.pow(float(text_list[i + 2]), (1 / 3)))
                i += 3
                continue
            except:
                pass

        elif text_list[i] == "logarithm" or text_list[i] == "log":
            if text_list[i + 2] == "base":
                base = text_list[i + 3]
                if base == "e":
                    base = math.e
                elif base == "pi":
                    base = math.pi
                else:
                    base = float(text_list[i + 3])

                parameters.append(math.log(float(text_list[i + 1]), base))
                expr.append(math.log(float(text_list[i + 1]), base))
                i += 4
                continue

            elif text_list[i + 2: i + 5] == ["to", "the", "base"]:
                base = text_list[i + 5]
                if base == "e":
                    base = math.e
                elif base == "pi":
                    base = math.pi
                else:
                    base = float(text_list[i + 5])

                parameters.append(math.log(float(text_list[i + 1]), base))
                expr.append(math.log(float(text_list[i + 1]), base))
                i += 6
                continue

            elif text_list[i + 2: i + 4] == ["with", "base"] or text_list[i + 2: i + 4] == ["to", "base"]:
                base = text_list[i + 5]
                if base == "e":
                    base = math.e
                elif base == "pi":
                    base = math.pi
                else:
                    base = float(text_list[i + 5])

                parameters.append(math.log(float(text_list[i + 1]), base))
                expr.append(math.log(float(text_list[i + 1]), base))
                i += 5
                continue

            elif text_list[i - 1] == "natural":
                if text_list[i + 1] == "of":
                    parameters.append(
                        math.log(float(text_list[i + 2]), math.e))
                    expr.append(math.log(float(text_list[i + 2]), math.e))
                    i += 3
                    continue
                else:
                    parameters.append(
                        math.log(float(text_list[i + 1]), math.e))
                    expr.append(math.log(float(text_list[i + 1]), math.e))
                    i += 2
                    continue
            else:
                try:
                    parameters.append(
                        math.log(float(text_list[i + 1]), float(text_list[i + 2])))
                    expr.append(
                        math.log(float(text_list[i + 1]), float(text_list[i + 2])))
                    i += 3
                    continue
                except:
                    if text_list[i + 1] == "of":
                        try:
                            parameters.append(
                                math.log(float(text_list[i + 2]), float(text_list[i + 3])))
                            expr.append(
                                math.log(float(text_list[i + 2]), float(text_list[i + 3])))
                            i += 4
                            continue
                        except:
                            parameters.append(
                                math.log(float(text_list[i + 2]), 10))
                            expr.append(math.log(float(text_list[i + 2]), 10))
                            i += 3
                            continue
                    else:
                        parameters.append(
                            math.log(float(text_list[i + 1]), 10))
                        expr.append(math.log(float(text_list[i + 1]), 10))
                        i += 2
                        continue
        elif text_list[i] == "ln" or text_list[i] == "LN":
            if text_list[i + 1] == "of":
                parameters.append(math.log(float(text_list[i + 2]), math.e))
                expr.append(math.log(float(text_list[i + 2]), math.e))
                i += 3
                continue
            else:
                parameters.append(math.log(float(text_list[i + 1]), math.e))
                expr.append(math.log(float(text_list[i + 1]), math.e))
                i += 2
                continue

        elif text_list[i] in sine_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.sin(float(text_list[i + 2])))
                expr.append(math.sin(float(text_list[i + 2])))
                i += 3
                continue
            elif text_list[i + 1] == "inverse":
                if text_list[i + 2] == "of":
                    parameters.append(math.asin(float(text_list[i + 3])))
                    expr.append(math.asin(float(text_list[i + 3])))
                    i += 4
                    continue
                else:
                    parameters.append(math.asin(float(text_list[i + 2])))
                    expr.append(math.asin(float(text_list[i + 2])))
                    i += 3
                    continue
            else:
                parameters.append(math.sin(float(text_list[i + 1])))
                expr.append(math.sin(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in cos_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.cos(float(text_list[i + 2])))
                expr.append(math.cos(float(text_list[i + 2])))
                i += 3
                continue
            elif text_list[i + 1] == "inverse":
                if text_list[i + 2] == "of":
                    parameters.append(math.acos(float(text_list[i + 3])))
                    expr.append(math.acos(float(text_list[i + 3])))
                    i += 4
                    continue
                else:
                    parameters.append(math.acos(float(text_list[i + 2])))
                    expr.append(math.acos(float(text_list[i + 2])))
                    i += 3
                    continue
            else:
                parameters.append(math.cos(float(text_list[i + 1])))
                expr.append(math.cos(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in tan_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.tan(float(text_list[i + 2])))
                expr.append(math.tan(float(text_list[i + 2])))
                i += 3
                continue
            elif text_list[i + 1] == "inverse":
                if text_list[i + 2] == "of":
                    parameters.append(math.atan(float(text_list[i + 3])))
                    expr.append(math.atan(float(text_list[i + 3])))
                    i += 4
                    continue
                else:
                    parameters.append(math.atan(float(text_list[i + 2])))
                    expr.append(math.atan(float(text_list[i + 2])))
                    i += 3
                    continue
            else:
                parameters.append(math.tan(float(text_list[i + 1])))
                expr.append(math.tan(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in cosec_KW:
            if text_list[i + 1] == "of":
                parameters.append(1 / math.sin(float(text_list[i + 2])))
                expr.append(1 / math.sin(float(text_list[i + 2])))
                i += 3
                continue
            elif text_list[i + 1] == "inverse":
                if text_list[i + 2] == "of":
                    parameters.append(math.asin(1 / float(text_list[i + 3])))
                    expr.append(math.asin(1 / float(text_list[i + 3])))
                    i += 4
                    continue
                else:
                    parameters.append(math.asin(1 / float(text_list[i + 2])))
                    expr.append(math.asin(1 / float(text_list[i + 2])))
                    i += 3
                    continue
            else:
                parameters.append(1 / math.sin(float(text_list[i + 1])))
                expr.append(1 / math.sin(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in sec_KW:
            if text_list[i + 1] == "of":
                parameters.append(1 / math.cos(float(text_list[i + 2])))
                expr.append(1 / math.cos(float(text_list[i + 2])))
                i += 3
                continue
            elif text_list[i + 1] == "inverse":
                if text_list[i + 2] == "of":
                    parameters.append(math.acos(1 / float(text_list[i + 3])))
                    expr.append(math.acos(1 / float(text_list[i + 3])))
                    i += 4
                    continue
                else:
                    parameters.append(math.acos(1 / float(text_list[i + 2])))
                    expr.append(math.acos(1 / float(text_list[i + 2])))
                    i += 3
                    continue
            else:
                parameters.append(1 / math.cos(float(text_list[i + 1])))
                expr.append(1 / math.cos(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in cot_KW:
            if text_list[i + 1] == "of":
                parameters.append(1 / math.tan(float(text_list[i + 2])))
                expr.append(1 / math.tan(float(text_list[i + 2])))
                i += 3
                continue
            elif text_list[i + 1] == "inverse":
                if text_list[i + 2] == "of":
                    parameters.append(math.atan(1 / float(text_list[i + 3])))
                    expr.append(math.atan(1 / float(text_list[i + 3])))
                    i += 4
                    continue
                else:
                    parameters.append(math.atan(1 / float(text_list[i + 2])))
                    expr.append(math.atan(1 / float(text_list[i + 2])))
                    i += 3
                    continue
            else:
                parameters.append(1 / math.tan(float(text_list[i + 1])))
                expr.append(1 / math.tan(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in asin_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.asin(float(text_list[i + 2])))
                expr.append(math.asin(float(text_list[i + 2])))
                i += 3
                continue
            else:
                parameters.append(math.asin(float(text_list[i + 1])))
                expr.append(math.asin(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in acos_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.acos(float(text_list[i + 2])))
                expr.append(math.acos(float(text_list[i + 2])))
                i += 3
                continue
            else:
                parameters.append(math.acos(float(text_list[i + 1])))
                expr.append(math.acos(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in atan_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.atan(float(text_list[i + 2])))
                expr.append(math.atan(float(text_list[i + 2])))
                i += 3
                continue
            else:
                parameters.append(math.atan(float(text_list[i + 1])))
                expr.append(math.atan(float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in asec_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.acos(1 / float(text_list[i + 2])))
                expr.append(math.acos(1 / float(text_list[i + 2])))
                i += 3
                continue
            else:
                parameters.append(math.acos(1 / float(text_list[i + 1])))
                expr.append(math.acos(1 / float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in acosec_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.asin(1 / float(text_list[i + 2])))
                expr.append(math.asin(1 / float(text_list[i + 2])))
                i += 3
                continue
            else:
                parameters.append(math.asin(1 / float(text_list[i + 1])))
                expr.append(math.asin(1 / float(text_list[i + 1])))
                i += 2
                continue

        elif text_list[i] in acot_KW:
            if text_list[i + 1] == "of":
                parameters.append(math.atan(1 / float(text_list[i + 2])))
                expr.append(math.atan(1 / float(text_list[i + 2])))
                i += 3
                continue
            else:
                parameters.append(math.atan(1 / float(text_list[i + 1])))
                expr.append(math.atan(1 / float(text_list[i + 1])))
                i += 2
                continue

        try:
            parameters.append(float(text_list[i]))
            expr.append(float(text_list[i]))

        except:
            if text_list[i] in add_KW or text_list[i] in sub_KW or text_list[i] in mul_KW or text_list[i] in div_KW:
                # key_words.append(text_list[i])
                if text_list[i] in add_KW:
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
    print(expr)
    return expr


def result(text_list):
    # Driver program to test above function
    exp = calculate(text_list)
    obj = Conversion(len(exp))
    obj.infixToPostfix(exp)
    print(obj.output)
    exp = obj.output
    obj = Evaluate(len(exp))
    res = obj.evaluatePostfix(exp)
    print(res)
    return res
