from ast import *
import os
from rewriter.rewriter import *
from rewriter.eval_rewriter import *
from rewriter.if_true_rewriter import *
from rewriter.plusplus_rewriter import *
from rewriter.if_without_else_rewriter import *

path = "input-code/"
dir_list = [
    "plusplus-input/test_01.py",
    "plusplus-input/test_02.py",
    "plusplus-input/test_03.py",
    "IfWithoutElse/test_01.py",
    "IfWithoutElse/test_02.py",
    "IfWithoutElse/test_03.py",
    ]
 
print("Transforming files in '", path, "' :")


for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    # we apply all rewriters in the file
    for commandClass in RewriterCommand.__subclasses__():    
        command = commandClass()
        tree = command.apply(tree)
    # export in a new file
    f = open("transformed-code/"+file, "w")
    f.write(unparse(tree))
    f.close()


# # file = "plusplus-input/test_03.py"
# file = "IfWithoutElse/test_02.py"
# print(" ==== " + file + " ==== ")
# fileContent = open(path+file).read()
# tree = parse(fileContent)
# # print(dump(tree, indent=2))  ## para imprimir el arbol
# # we apply all rewriters in the file
# for commandClass in RewriterCommand.__subclasses__():    
#     command = commandClass()
#     tree = command.apply(tree)
# # export in a new file
# f = open("transformed-code/"+file, "w")
# f.write(unparse(tree))
# f.close()