#!/usr/bin/env python
# coding:utf8
# author:Z time:2018/7/30
import sys
import importlib
importlib.reload(sys)
import os
from tqdm import tqdm

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


os.chdir('E:/博士 2021/0 智能家用健康管理机器人 ZXD/0 健康 家庭 移动 机器人 Soopat ZXD 20220706/')

path = r'E:/博士 2021/0 智能家用健康管理机器人 ZXD/0 健康 家庭 移动 机器人 Soopat ZXD 20220706/'  #【设定pdf文件路径】
txt_save_path = 'E:/博士 2021/0 智能家用健康管理机器人 ZXD/4 专利撰写 ZXD 20220707/'  # 【设定保存TXT文件路径】


def parse(path, filename, txt_save_path):
    """
    功能：解析pdf 文本，保存到txt文件中
    path：pdf存放的文件夹路径
    filename: pdf文件名
    txt_save_path: 需要保存的txt文件夹路径

    """
    pdf_path = path + filename + '.pdf'
    fp = open(pdf_path, 'rb') # 以二进制读模式打开
    #用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages(): # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(txt_save_path+filename+'.txt', 'a', encoding='utf-8') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + '\n')

if __name__ == '__main__':
    files = os.listdir(path)
    for file in tqdm(files):
        filename = file.split('.')[0]
        parse(path, filename, txt_save_path)