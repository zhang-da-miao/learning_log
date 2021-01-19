"""
AUTHOR:         zhou_yi_guang
GITHUB:         https://github.com/zyiguang
EMAIL:          zhouyg180@gmail.com
TIME:           2021/1/19 11:24 上午
INSTRUCTIONS:   全局模版变量
"""

from django.conf import settings


def util(request):
    return {
        "data_1": "hello",
        "data_2": "world",
    }