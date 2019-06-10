# 1、为什么s.title().upper()的结果是'NOW IS BETTER THAN NEVER.'  于Part.1.E.5.Strings

"""
import re

str = 'erererererea error wonderer severeness eer erer a era'

pttn = r'er{0}a'
re.findall(pttn, str)

pttn = r'[er]{0}a'
re.findall(pttn, str)

pttn = r'(er){0}a'
re.findall(pttn, str)

结果是：
['ea']
['a', 'a', 'a']
['', '', '']

问题：以上代码，结果2/3不能理解

"""