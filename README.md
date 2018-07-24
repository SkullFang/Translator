# Translator
中文句子批量翻译成英文。使用的是google translator

# 前言
这里使用了谷歌翻译的python api，对中文文章进行一个批量的翻译。运行环境为python 3.6

# 依赖库说明

googletrans

安装方法

pip install googletrans

sys和getopt（自带）


# 使用说明
本程序采用命令行输入，输出，如果想在IDE中进行输入输出可自行修改代码相应的地方。

## 帮助说明
python trans.py -h
结果为该程序的使用说明

## 翻译
python trans.py -i 'inputfile path' -o 'outputfile path'
控制台会有每一条的翻译结果，并且自动把结果输出到制定的文件中。

# Example
test文件夹中有测试文件，在源程序目录下命令行输入。
python trans.py -i './test/test.txt' -o 'result.txt'

在该目录就可以看到输出的结果。

# 未解决问题
因为底层调用的是google翻译的API,这个API是收费的。
在本测试中使用比较少数量的文字未发现问题。
但是不排除有问题，因为代码过于简单粗暴。
暂定为V0.0版本。

# 版本迭代
## v0.0

实现 文件到文件的翻译。

## v0.1

添加可以直接翻译句子新功能

example
命令行输入
```shell
python trans.py -s "早上好"
```
出来结果

Good morning


