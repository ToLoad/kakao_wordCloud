import re
import string

results = []
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
    text = re.sub(pattern = '\\n', repl = '', string = text)
    text = text.strip(string.punctuation) # 모든 구두점 삭제
    
    text = text.lstrip()


    return(text)

def get_name(text):
    # text = text.split(' : ')
    # id = text[0]

    number = text.find(':')
    id = text[ :number - 1]

    return(id)

def get_text(text):
    number = text.find(':')
    textT = text[number + 2:]

    return(textT)


def split_text(input_id):
    f = open('123.txt', 'r', encoding='utf-8')

    lines = f.readlines()

    for line in lines:
        result = cleaning_text(line)
        id = get_name(result)
        text = get_text(result)

        if (id == input_id):
            results.append(text)
            global result_text
            result_text = result_text + ' ' + text
    return result_text             

# id = input("분석할 사람의 이름을 입력하세요: ")
# split_text(id)
# print(results)