# (课外作业）语音播报pyttsx
# 1.百度搜索相关中文解决方案，大概要用哪个包。
# 2.github搜索相关包。
# 3.pip install pyttsx3
# 4.示例代码
import pyttsx3
engine = pyttsx3.init()
engine.say('the lazy dog')
engine.runAndWait()