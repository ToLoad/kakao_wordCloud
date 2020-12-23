from konlpy.tag import Okt
from konlpy.tag import Hannanum
from collections import Counter
from analyze_text import split_text
from wordcloud import WordCloud

from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_freq_used_words(id, text_file, mode):
    results = split_text(id, text_file, mode)
    hannanum = Hannanum()
    nouns = hannanum.nouns(results)

    for i, v in enumerate(nouns):
        if len(v) < 2:
            nouns.pop(i)

    count = Counter(nouns)
    nouns_list = count.most_common(200)

    return nouns_list

def make_png(id, text_file, mode):
    wc = WordCloud(font_path='./font/NanumGothic.ttf',
        background_color='white',
        width=1000,
        height=1000)

    nouns_list = get_freq_used_words(id, text_file, mode)
    wc.generate_from_frequencies(dict(nouns_list))
    plt.switch_backend('agg')
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(wc)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    buf.truncate(0)
    buf.seek(0)
    
    # return f"<img src='data:image/png;base64,{data}'/>"
    return (data, nouns_list)