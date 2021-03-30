from parser import CalcParser, CalcLexer

def read_file_content(cmd: str) -> str:
    if len(cmd) < 3:
        return ''
    path = cmd[2:].strip()
    if len(path) < 3 or path[-3:] != '.ga':
        print('Invalid file path')
        return ''
    out = ''
    with open(path, "r") as file:
        out = file.read()
    return out

if __name__ == '__main__':
    lex = CalcLexer()
    yacc = CalcParser()
    while True:
        text = ''
        try:
            text = input('gai (> ')
        except EOFError:
            break
        if text and len(text) >= 4 and text[0:5] == 'quit':
            break
        elif text and len(text) >= 2 and text[0:2] == '$f':
            file_content = read_file_content(text)
            if len(file_content) > 0:
                yacc.parse(lex.tokenize(file_content))
            break
        elif text:
            yacc.parse(lex.tokenize(text))
