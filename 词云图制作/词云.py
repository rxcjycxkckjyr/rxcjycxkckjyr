import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from matplotlib import colors


f = open(r'金陵诗歌汇总.txt',"r",encoding="utf-8")
text = f.read()
f.close()
words_list_jieba = jieba.lcut(text)

def findifhave(demo,stop):
    for ret in stop:
        if(demo == ret):
            return 'T'


stop = ['\n']
with open("stop.txt",'r',encoding='utf-8') as f1:
    for line in f1:
        stop.append(line.replace("\n",""))
f1.close()

dict = {}
for key in words_list_jieba:
    dict[key] = dict.get(key,0) + 1
    
for demo in list(dict.keys()):
    if('T' == findifhave(demo,stop)):
        del dict[demo]

dict1 = sorted(dict.items(),key = lambda d:d[1] , reverse = True)
print(dict1)


background_image = np.array(Image.open('2.png'))
colormaps = colors.ListedColormap(['#871A84', '#BC0F6A', '#BC0F60', '#CC5F6A', '#AC1F4A'])
wordcloud = WordCloud(font_path='STCAIYUN.TTF',  # 字体
                        prefer_horizontal=0.99,
                        background_color='white',  # 背景色
                        max_words=20,  # 显示单词数
                        max_font_size=400,  # 最大字号
                        stopwords=stop,  # 过滤噪声词
                        mask=background_image,  # 背景轮廓
                        colormap=colormaps,  # 使用自定义颜色
                        collocations=False
                        ).fit_words(dict)
image = wordcloud.to_image()
image.show()  # 展示图片
wordcloud.to_file('D:\词云图.png')  # 保存图片