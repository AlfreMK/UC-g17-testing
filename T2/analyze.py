from ast import *
import os
from textwrap import indent
from rules.rule import *
#from rules.eval_used import *
#from rules.uncouple_method import *
#from rules.dummy_if import *
#from rules.uninitialized_attribute import *
from rules.bonus import *

path = "input-code/"
dir_list = os.listdir(path)
 
print("Analyzing files in '", path, "' :")


# for file in dir_list:
#     print(" ==== " + file + " ==== ")
#     fileContent = open(path+file).read()
#     tree = parse(fileContent)
#     warnings = []
#     for ruleClass in Rule.__subclasses__():    
#         newRule = ruleClass()
#         result = newRule.analyze(tree)
#         warnings.extend(result)
#     for warning in warnings:
#         warning.wprint()



file = "bonus02.py"
print(" ==== " + file + " ==== ")
fileContent = open(path+file).read()
tree = parse(fileContent)
warnings = []
#print(dump(tree, indent=2))  ## para imprimir el arbol
for ruleClass in Rule.__subclasses__():    
    newRule = ruleClass()
    result = newRule.analyze(tree)
    warnings.extend(result)
for warning in warnings:
    warning.wprint()