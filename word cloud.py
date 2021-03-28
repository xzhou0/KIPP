#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:59:58 2021

@author: xzxz
"""
from wordcloud import WordCloud
#from scipy.misc import imread
import matplotlib.pyplot as plt
import pandas as pd


user_labels_list = []
excel_path = "./ID_act_alumni_AP_GPA_Enroll.csv"    #excel文件路径
user_labels = pd.DataFrame(pd.read_csv(excel_path))  #读取excel表格
#print(user_labels['user_label'])
for label in user_labels['Currently Enrolled School']:    #把表格的每一列存到列表user_labels_list中
    user_labels_list.append(label)
#excel文本处理   
cleanedList = [x for x in user_labels_list if str(x) != 'nan']   #去掉空值
mytext = ''.join(cleanedList)    #把列表变成字符串
mytext = mytext.replace(";"," ")  #把字符串中的分号；换成空格，不换也没关系好像


#词云制作
#mk = imread('20180906191748940.jfif')   #读取词云背景形状图片
wordcloud = WordCloud(background_color="white",max_words=50,collocations=False)   #设置词云字体，背景色，最大词数和背景形状图片
wordcloud.generate(mytext)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()
#图片导出
wordcloud.to_file('lables.png')