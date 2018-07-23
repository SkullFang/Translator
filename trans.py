#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/23/2018 4:53 PM
# @Author  : SkullFang
# @Contact : yzhang.private@gmail.com
# @File    : trans.py
# @Software: PyCharm
import sys,getopt
from googletrans import Translator
import time
def main(argv):
   input= ''
   output= ''
   translator = Translator(service_urls=['translate.google.cn'])
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["i=","o="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--i"):
         input = arg
      elif opt in ("-o", "--o"):
         output = arg
   fin = open(input[1:-1], 'r', encoding='utf-8')
   fou = open(output[1:-1], 'w', encoding='utf-8')
   for line in fin:
      print(line)
      fou.write(line)
      text = translator.translate(line, src='zh-cn', dest='en').text.strip('\n')
      print(text + '\n')
      fou.write(text + '\n')
      time.sleep(1)

if __name__ == "__main__":
   main(sys.argv[1:])