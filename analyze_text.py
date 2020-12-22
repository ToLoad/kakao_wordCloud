import re
import string

result_text = ''

def cleaning_text(text):
    text = re.sub(pattern = '[사진]+ \\d+[장]', repl = '', string = text)
    text = re.sub(pattern = '[사진]+ \\d\\d+[장]', repl = '', string = text)
    text = re.sub(pattern = '[샵검색]+\\:', repl = '', string = text)
    text = re.sub(pattern = '\\n', repl = '', string = text)
    text = text.strip(string.punctuation) # 모든 구두점 삭제
    text = text.lstrip()

    return(text)

def get_name_phone(text):
    number1 = text.find(',')
    number2 = text.find(':', number1)
    if not (number1 == -1 or number2 == -1):
        id = text[number1 + 1 : number2]
        id = id.lstrip()
        id = id.rstrip()

        return(id)

def get_name_pc(text):
    number1 = text.find('[')
    number2 = text.find(']')
    if not (number1 == -1 or number2 == -1):
        id = text[: number2]
        id = id.lstrip()
        id = id.rstrip()

        return(id)

def get_text_phone(text):
    number = text.find(':')
    if not (number == -1):
        textT = text[number + 2:]
        textT = textT.lstrip()
        textT = textT.rstrip()

        return(textT)

def get_text_pc(text):
    number1 = text.find(']')
    number2 = text.find(']', number1 + 1)
    if not (number1 == -1 or number2 == -1):
        textT = text[number2 + 2:]
        textT = textT.lstrip()
        textT = textT.rstrip()

        return(textT)


def split_text(input_id, text_file, mode):
    lines = text_file.readlines()

    for idx, line in enumerate(lines):
        line = line.decode('utf-8')
        if (idx > 6):
            result = cleaning_text(line)
            if (mode == 'phone'):
                id = get_name_phone(result)
                text = get_text_phone(result)
            else:
                id = get_name_pc(result)
                text = get_text_pc(result)
            if (id == input_id):
                if not (text == '동영상' or text == '이모티콘' or text == '사진' or text == None or text == ''):
                    global result_text
                    result_text = result_text + ' ' + text
    return result_text

def get_id(text_file, mode):
    lines = text_file.readlines()
    id_array = [None for i in range(len(lines))]
    results = []

    for idx, line in enumerate(lines):
        line = line.decode('utf-8')
        if (idx > 6):
            result = cleaning_text(line)
            if (mode == 'phone'):
                id = get_name_phone(result)
            else:
                id = get_name_pc(result)
            id_array[idx] = id

    id_set = set(id_array)
    id_array = list(id_set)

    for i in id_array:
        if not (i == '' or i == None):
            results.append(i)

    return results                