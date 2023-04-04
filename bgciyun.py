# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:58:35 2023

@author: 22837
"""
# 词云图

from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云，颜色生成器，停止词

import matplotlib.pyplot as plt # 数据可视化
from PIL import Image  # 处理图片
import numpy as np  # 科学计算


train = ''#分词后的文件直接连接成字符串使用
fp = open('./zanjuke.txt','r',encoding='utf-8')
for line in fp:#加载词
    if line != '':
       train=train+line


img = Image.open('./bg.jpg')  # 打开图片
img_array = np.array(img)  # 将图片装换为数组


# 配置词云的背景，图片，字体大小等参数
wc = WordCloud(
    background_color='white',  # 设置显示内容在什么颜色内
    width=1000,  # 设置图片宽,默认为400
    height=1000,  # 设置图片高,默认为200
    mask=img_array,  # 设置词云背景模板
    font_path="msyh.ttc",  # 设置字体路径
    scale=1.5,  # 图照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍
    max_words=1000,  # max_words图片上显示的最大词语的个数
    max_font_size=120,  # max_font_size为最大字体的大小
    min_font_size=4,  # min_font_size为最小字体大小,默认为4
    mode='RGB',  # ,默认值RGB,当参数为“RGBA”并且background_color不为空时，背景为透明
    relative_scaling=.5,  # 词频和字体大小的关联性,默认值
    collocations=True  # 是否包括两个词的搭配
)

wc.generate_from_text(train)  # 根据文本生成词云
#image_colors = ImageColorGenerator(img_array)  # 获取color
#plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")  # 按照给定的图片颜色布局生成字体颜色,当wordcloud尺寸比image大时，返回默认的颜色
plt.imshow(wc)
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图片
wc.to_file('中文词云图1.png')  # 保存图片


