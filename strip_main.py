# a stupid little parser that finds top level function bodies
# and strips them out
import re

def scan_to_matching(s, open_c, close_c):
    c_stack = []
    for i,c in enumerate(s):
        if c == open_c:
            c_stack.append(c)
        elif c == close_c:
            if len(c_stack) == 0:
                return i
            else :
                c_stack.pop()
    assert i >= 0
    return i

code = open('main.R').read()

# we use the line at the end of main.R to mark code that shouldn't be stripped
code_end = code.index('# SUPPORT CODE - DO NOT EDIT BELOW THIS LINE')-2

if code_end == -1 :
    code_end = len(code)

boundaries = [0]

i = 0
while i < len(code[:code_end]):

    function_pos = re.search('function', code[i:])
    if function_pos is None:
        break

    i += function_pos.span()[1]

    # find and omit the function arguments
    while code[i] != '(':
        i += 1
    i += 1 # step into paren
    end_i = scan_to_matching(code[i:], '(', ')')
    i += end_i+1 # step out of paren

    while code[i] != '{':
        i += 1
    i += 1 # step into function body
    end_i = scan_to_matching(code[i:], '{', '}')

    repl = code[i:i+end_i]
    boundaries.extend([i, i+end_i])

    i += end_i+1

boundaries.append(len(code))

for st, en in [boundaries[i:i+2] for i in range(0, len(boundaries),2)]:
    print(code[st:en])
    if en != len(code):
        print('    return(NULL)')
