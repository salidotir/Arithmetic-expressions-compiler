import sys
import ply.lex as lex
import ply.yacc as yacc

# dictionary of number tokens
numbers = {
    '0': "Zer",
    '1': "One",
    '2': "Two",
    '3': "Thr",
    '4': "Fou",
    '5': "Fiv",
    '6': "Six",
    '7': "Sev",
    '8': "Eig",
    '9': "Nin",
    10: "Ten",
    100: "Hun",
    1000: "Tou"
}

def interpret_numbers(num):
    digits = str(num)[::-1]
    num_of_digits = len(digits)
    res_str = ""

    if num_of_digits == 1:
        res_str = numbers[digits[0]]

    elif num_of_digits == 2:
        res_str = numbers[digits[1]] + numbers[10] + "_" + numbers[digits[0]]

    elif num_of_digits == 3:
        res_str = numbers[digits[2]] + numbers[100] + "_" + numbers[digits[1]] + numbers[10] + "_" + numbers[digits[0]]

    elif num_of_digits == 4:
        res_str = "(" + numbers[digits[3]] + ")" + numbers[1000] + "_" + numbers[digits[2]] + numbers[100] + "_" + \
                  numbers[digits[1]] + numbers[10] + "_" + numbers[digits[0]]

    elif num_of_digits == 5:
        res_str = "(" + numbers[digits[4]] + numbers[10] + "_" + numbers[digits[3]] + ")" + numbers[1000] + "_" + \
                  numbers[digits[2]] + numbers[100] + "_" + numbers[digits[1]] + numbers[10] + "_" + numbers[digits[0]]

    elif num_of_digits == 6:
        res_str = "(" + numbers[digits[5]] + numbers[100] + "_" + numbers[digits[4]] + numbers[10] + "_" + numbers[
            digits[3]] + ")" + numbers[1000] + "_" + numbers[digits[2]] + numbers[100] + "_" + numbers[digits[1]] + \
                  numbers[10] + "_" + numbers[digits[0]]
    else:
        res_str = ""

    return res_str


tokens = [
    'NUMBER',
    'Plu',
    'Min',
    'Div',
    'Mul',
    'OpenParen',
    'CloseParen'
]

t_Plu = r'\+'
t_Min = r'\-'
t_Mul = r'\*'
t_Div = r'\/'
t_OpenParen = r'\('
t_CloseParen = r'\)'

t_ignore = " \t"
t = 1


def t_NUMBER(t):
    r'\d+'
    t.value = interpret_numbers(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# # Test lexer
# lexer.input("1+4+(5*6)")
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)


# Parsing rules
precedence = (
    ('left', 'Plu', 'Min'),
    ('left', 'Mul', 'Div')
)


def p_expr(p):
    '''expr : expression
            | num
            | empty
    '''
    print("Print ", p[1])


def p_empty(p):
    '''empty : 
    '''
    p[0] = None


def p_num_expr(p):
    "num : NUMBER"
    global t
    # num_interpreted = interpret_numbers(p[1])
    print("Assign " + p[1] + " to t" + str(t))
    p[0] = "t" + str(t)


def p_expression_binop(p):
    '''expression : expression Plu expression
                  | expression Min expression
                  | expression Mul expression
                  | expression Div expression'''
    global t
    if p[2] == '+':
        # p[0] = p[1] + p[3]
        print("Assign " + str(p[1]) + " Plu " + str(p[3]) + " to t" + str(t))
        p[0] = "t" + str(t)
    elif p[2] == '-':
        # p[0] = p[1] - p[3]
        print("Assign " + str(p[1]) + " Min " + str(p[3]) + " to t" + str(t))
        p[0] = "t" + str(t)
    elif p[2] == '*':
        # p[0] = p[1] * p[3]
        print("Assign " + str(p[1]) + " Mul " + str(p[3]) + " to t" + str(t))
        p[0] = "t" + str(t)
    elif p[2] == '/':
        # p[0] = p[1] / p[3]
        print("Assign " + str(p[1]) + " Div " + str(p[3]) + " to t" + str(t))
        p[0] = "t" + str(t)
    t += 1


def p_expression_group(p):
    "expression : OpenParen expression CloseParen"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"

    p[0] = p[1]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


# Biuld the parser
parser = yacc.yacc()

while True:
    try:
        t = 1
        s = input('interpret >> ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
