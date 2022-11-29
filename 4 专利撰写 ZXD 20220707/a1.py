#版权人：朱小冬 技术支持：qq1399176533
#print('hello world');
print("........................................# 专利分析软件 #................................................. ")
print("................................# 版权人：朱小冬 #技术支持：qq1399176533 #...............................");

import os
import re
import pdfplumber   # 导入pdfplumber （如果pip下载模块不成功，指定版本号得以解决
import pandas as pd

df = pd.DataFrame(columns= ["申请日","申请号","申请公布号","申请公布日","授权公告号",\
                            "授权公告日","专利申请人","发明人","专利名称","技术领域",\
                            "专利关键技术点分析（保护了什么创新技术点）"])
df_row = 1

paths = ["E:/博士 2021/0 智能家用健康管理机器人 ZXD/0 健康 家庭 移动 机器人 Soopat ZXD 20220706",\
         "E:/博士 2021/0 智能家用健康管理机器人 ZXD/1 医疗 家庭 移动 机器人 Soopat ZXD 20220707",\
         "E:/博士 2021/0 智能家用健康管理机器人 ZXD/2 智能健康管理机器人 百度学术 ZXD 20221013"] #文件夹目录
for path in paths:
  files= os.listdir(path) #得到文件夹下的所有文件名称
  #file = files[2];print(file)
  for file in files: #遍历文件夹
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
      with pdfplumber.open(os.path.join(path,file)) as pdf:
        print("共",len(pdf.pages),"页 ...")
        content = []
        for i in range(len(pdf.pages)):
          #print(".................................................第",i+1,"页...................................................")
          page = pdf.pages[i]  # 获取到pdf的页数
          page_content= page.extract_text(); page_text = path + "," + file;
          if(i<1):
            #print(page.extract_text())

            res= re.search(".*申请日(.*)\n.*",page_content)  #申请日
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 1'); k = 1; k = k + 1;

            res= re.search(r".*申请号(.*)\n",page_content)  #申请号
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 2'); k = k + 1;

            res= re.search(r".*申请公布号(.*)\n",page_content)  #申请公布号
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 3'); k = k + 1;

            res= re.search(r".*申请公布号(.*)\n",page_content)  #申请公布日
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 4'); k = k + 1;

            res= re.search(r".*授权公告号(.*)\n",page_content)  #授权公告号
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 5'); k = k + 1;

            res= re.search(r".*授权公告日(.*)\n",page_content)  #授权公告日
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 6'); k = k + 1;

            res= re.search(r".*专利权人(.*)\n",page_content)  #专利申请人
            if not res:
              res= re.search(r".*申请人(.*)\n",page_content)  #专利申请人
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 7'); k = k + 1;

            res= re.search(r".*发明人(.*)\n",page_content)  #专利权人
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 8'); k = k + 1;

            res= re.search(r".*专利名称\n([\s\S]*)\n\(.*",page_content)  #专利名称
            if not res:
              res= re.search(r".*发明名称\n([\s\S]*)\n\(.*",page_content)  #专利名称
              if not res:
                res= re.search(r".*实用新型名称\n([\s\S]*)\n\(.*",page_content)  #专利名称
            if res:
              result = res[1].strip(); #print(result,"fgfd ")
              content.append(result); #print(content,"rdgfg")
            else:
              content.append(file); k = k + 1;

            res= re.search(".*摘要\n([\s\S]*).*",page_content)  #专利关键技术点分析（保护了什么创新技术点）
            if res:
              result = res[1].replace("\n",""); result = result .replace(" ","");#print(result,"fgfd ")
              content.append('无 10'); content.append(result); #print(content,"rdgfg")
            else:
              content.append('无 10'); content.append('无 11'); k = k + 1;

            page_text.append(page_content);
          else:
            res= re.search(r".*\n\[0001\]([\s\S]*)\n背景技术\n.*",page_content)  #技术领域
            if res:
              result = res[1].replace("\n","");result = result .replace(" ",""); #print(result,"fgfd ")
              content[9] = result; #print(content,"背景技术rdgfg");
              break;
            elif (i+1 == len(pdf.pages)):
              content[9] = "无 10";

            page_text.append(page_content);

          df.=page_content;

    #print(len(content),"  ",content)
    if(k>2):    #if k>9
      content.append();k=0;
    df.loc[df_row] = content
    df_row =df_row+1



df = df.drop_duplicates(subset="专利名称",keep="first")
df.to_excel('专利分析报告.xlsx')
#        page_content = '\n'.join(page.extract_text().split('\n'))  # 处理读取到的字符串
#        content = content+page_content

print("分析完成 ...")
