# -*- coding: utf-8 -*-
"""
这是一个pip打包的例子

@author: lowinli

@email: lowinli@outlook.com
"""

import numpy as np


def softmax(x):
    """对向量进行softmax处理

    这只是对自动api文档的一个例子

    Args:
        x (int): 输入向量

    Returns:
        np.array: softmax结果

    Examples:
        >>> array = softmax(np.array([1, 1]))
        >>> array
        np.array([0.5, 0.5])

    References:
        softmax维基百科  https://en.wikipedia.org/wiki/Softmax_function
    """
    return np.exp(x) / np.sum(np.exp(x), axis=0)
