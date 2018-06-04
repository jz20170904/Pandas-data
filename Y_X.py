# -*- coding:GB2312 -*-
import pandas as pd
import numpy as np
import re
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import chardet
mpl.rcParams['font.sans-serif'] = [u'SimHei']  #FangSong/���� FangSong/KaiTi
mpl.rcParams['axes.unicode_minus'] = False


# with open('Data.out','r') as wd:
#     txet=wd.read()
#     type=chardet.detect(txet)
#     print type["encoding"]


Data = pd.read_fwf('Data.out')
Data.to_csv('CreatData.txt', sep=',')#���Ϊ�ļ����ڲ������ж�
List_all = [] #������������ļ���
List_need=[]#����������б�
#��ȡ������Ҫ�����Ӧ������
for i in range(Data.ix[:,0].size):
    if re.search('==',str(Data.ix[[i]].values[0][0])) !=None:
        List_all.append(i)

#������Ҫ���ַ��б�
List_Tab_need = ['02-set']
#��ȡ�ַ��б��Ӧ������
for i in range(Data.ix[:, 0].size):
    for j in range(len(List_Tab_need)):
        if re.search(List_Tab_need[j], str(Data.ix[[i]].values[0][0])) != None:
            List_need.append(i)
List_and=[i for i in range(len(List_all)) if List_all[i] in List_need]



#��ȡx,y����������
def y_x(List_all):
    y=[]#����y���б�
    x=[]#����x���б�
    a=List_all[List_and[0]]+5
    b=List_all[List_and[0]+1]-1
    Taking_x_rst=Data.iloc[a:b,0]
    for i in range((Taking_x_rst.size/2)):
        a0=a+2*i
        #¥����Fn
        y.append(float(Data.iloc[a0,0].split()[0]))
    for i in range((Taking_x_rst.size/2)):
        b0=a+1+2*i
        if len(Data.iloc[b0,0].split())==5:
            x.append(float(Data.iloc[b0,0].split()[3].split('/')[1]))
        else:
            x.append(float(Data.iloc[b0,0].split()[4]))
    ny=np.array(y)
    dx=np.array([1/i for i in x])
    #��������
    plt.figure(facecolor="w",figsize=(3,4))
    plt.plot(dx,ny,"--",label=u"y-x",color="red",linewidth=3)
    plt.title(u"*_y-x_*",fontsize=15)
    plt.xlabel(u"x",fontsize=20)
    plt.ylabel(u"y",fontsize=20)
    plt.xlim((0,max(dx)))
    plt.ylim((0,ny[0]))
    plt.legend()
    plt.savefig(u"y-x")#����ͼƬ
    plt.show()
y_x(List_all)











