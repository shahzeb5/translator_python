# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:58:37 2021

@author: pc user
"""

from googletrans import Translator

translater = Translator()

out=translater.translate("i love you", dest="ur")
print(out.text)