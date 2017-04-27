# -*- coding:utf-8 -*-#
__author__ = 'RJS'
import jieba
import json

keywords = ['γ', '能谱', '识别', '核信号', '监测', '伽马']


def interest():
    interest = {}
    with open('newest.json', 'r') as f:
        data = json.load(f)
        key_lst = data.keys()
        for i, ele in enumerate(key_lst):
            word = jieba.cut(ele, cut_all=False)
            for j, w in enumerate(word):
                if w in keywords:
                    interest[ele] = data[ele]
    return interest

