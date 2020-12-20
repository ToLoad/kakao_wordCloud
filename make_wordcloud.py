from konlpy.tag import Okt
from konlpy.tag import Hannanum
from collections import Counter
from analyze_text import split_text
from wordcloud import WordCloud

# import matplotlib.pyplot as plt

def get_freq_used_words(id, text_file):
    results = split_text(id, text_file)
    hannanum = Hannanum()
    nouns = hannanum.nouns(results)

    for i, v in enumerate(nouns):
        if len(v) < 2:
            nouns.pop(i)

    count = Counter(nouns)

    nouns_list = count.most_common()

    # for v in nouns_list:
    #     print(v)
    
    return nouns_list

def make_png(id, text_file):
    wc = WordCloud(font_path='font\\NanumGothic.ttf',
        background_color='white',
        width=1000,
        height=1000)

    nouns_list = get_freq_used_words(id, text_file)
    wc.generate_from_frequencies(dict(nouns_list))
    wc.to_file('wordcloud.png')
    # plt.figure(figsize = (15, 10))
    # plt.axis("off")
    # plt.imshow(wc)
    # plt.show()
    print("finished..")

# f = open('123.txt', 'r', encoding='utf-8')
# make_png('준혁이', f)
