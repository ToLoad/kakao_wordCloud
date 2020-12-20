import re
import string

# results = []
result_text = ''

def cleaning_text(text):
    text = re.sub(pattern = '\\d\\d\\d\\d\\. \\d\\. \\d\\.', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d\\. \\d\\. \\d\\d\\.', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d\\. \\d\\d\\. \\d\\.', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d\\. \\d\\d\\. \\d\\d\\.', repl = '', string = text)
    text = re.sub(pattern = '[오전|오후]+ \\d\\:\\d\\d\\,', repl = '', string = text)
    text = re.sub(pattern = '[오전|오후]+ \\d\\:\\d\\,', repl = '', string = text)
    text = re.sub(pattern = '[오전|오후]+ \\d\\d\\:\\d\\d\\,', repl = '', string = text)
    text = re.sub(pattern = '[오전|오후]+ \\d\\d\\:\\d\\,', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d[년]+ \\d[월]+ \\d[일]+ \\w\\w\\w', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d[년]+ \\d[월]+ \\d\\d[일]+ \\w\\w\\w', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d[년]+ \\d\\d[월]+ \\d[일]+ \\w\\w\\w', repl = '', string = text)
    text = re.sub(pattern = '\\d\\d\\d\\d[년]+ \\d\\d[월]+ \\d\\d[일]+ \\w\\w\\w', repl = '', string = text)
    text = re.sub(pattern = '[사진]+ \\d+[장]', repl = '', string = text)
    text = re.sub(pattern = '[사진]+ \\d\\d+[장]', repl = '', string = text)
    text = re.sub(pattern = '[샵검색]+\\:', repl = '', string = text)
    text = re.sub(pattern = '\\n', repl = '', string = text)
    text = text.strip(string.punctuation) # 모든 구두점 삭제
    
    text = text.lstrip()


    return(text)

def get_name(text):
    number = text.find(':')
    id = text[ :number - 1]

    return(id)

def get_text(text):
    number = text.find(':')
    textT = text[number + 2:]
    textT = textT.lstrip()
    textT = textT.rstrip()

    return(textT)


def split_text(input_id, text_file):
    lines = text_file.readlines()

    for line in lines:
        line = line.decode('utf-8')
        result = cleaning_text(line)
        id = get_name(result)
        text = get_text(result)

        if (id == input_id):
            if not (text == '동영상' or text == '이모티콘' or text == '사진'):
                # results.append(text)
                global result_text
                result_text = result_text + ' ' + text
    return result_text             