from ast import *
import os
from textwrap import indent
from rules.rule import *
# from rules.eval_used import *
# from rules.uncouple_method import *
# from rules.dummy_if import *
# from rules.uninitialized_attribute import *

from rules.suspicious_variable_name import *
from rules.never_readed_variable import *
from rules.dataclass import *
from rules.bonus import *


path = "input-code/"
dir_list = [
    "suspiciousVariable/test_01.py",
    "suspiciousVariable/test_02.py",
    "suspiciousVariable/test_03.py",
    "NeverReaded/test_01.py",
    "NeverReaded/test_02.py",
    "NeverReaded/test_03.py",
    "dataClass/test_01.py",
    "dataClass/test_02.py",
    "dataClass/test_03.py",
    "dataClass/test_04.py",
    "bonus01.py",
    "bonus02.py",
    "bonus03.py",
    ]
 
print("Analyzing files in '", path, "' :")


for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    warnings = []
    for ruleClass in Rule.__subclasses__():    
        newRule = ruleClass()
        result = newRule.analyze(tree)
        warnings.extend(result)
    for warning in warnings:
        warning.wprint()




# file = "bonus03.py"


# file = "code_test_03.py"
# file = "dataClass/test_01.py"


# file = "suspiciousVariable/test_03.py"
# file = "NeverReaded/test_03.py"
# file = "dataClass/test_04.py"


# print(" ==== " + file + " ==== ")
# fileContent = open(path+file).read()
# tree = parse(fileContent)
# warnings = []
# #print(dump(tree, indent=2))  ## para imprimir el arbol
# for ruleClass in Rule.__subclasses__():    
#     newRule = ruleClass()
#     result = newRule.analyze(tree)
#     warnings.extend(result)
# for warning in warnings:
#     warning.wprint()