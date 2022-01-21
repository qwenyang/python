#!/usr/bin/python2.7
#coding:utf8

"""
File Name :			reconstruct_code.py
Creation Date :		2022-01-20
Created By :        qwenyang
Description :
"""

import time
import json
import re
from functools import reduce

# word 的分隔符
split_operators = [',', ' ', '\t', ':']

# 写入文件
def writeToFile(file_path, lines):
    lines = map(lambda line: line+'\n', lines)
    with open(file_path, 'w+') as f:
        f.write(reduce(lambda res,line:res + line, lines))

# 读出文件
def readFromFile(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda line:line.rstrip('\n'), lines))
        return lines

# 解析一行代码的单词
def parseWords(line):
    words = re.split("([', \t:'])", line)
    return words

# 将一个变量参数param转换成驼峰
def snakeToCamel(param):
    words = param.split('_')
    if len(words) == 1:
        return words[0]
    words = list(map(lambda word: word.capitalize(), words))
    words[0] = words[0][:1].lower() + words[0][1:]
    return ''.join(words)

def codeStyleSnakeToCamel(file_path):
   lines = readFromFile(file_path)
   line_words = list(map(parseWords, lines))
   new_lines = []
   for words in line_words:
       words = list(map(snakeToCamel, words))
       new_lines.append(''.join(words))
   writeToFile(file_path+'.bak', new_lines)

if __name__ == '__main__':
    codeStyleSnakeToCamel('./snake_code_style.txt')
