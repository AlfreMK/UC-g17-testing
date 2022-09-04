from ast import *
import threading
from multiprocessing.dummy import Array
import os

class Instrumentor(NodeTransformer):
    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        injected_code = 'Profile.record(\''+ transformedNode.name+'\',['
        i = 0
        for arg in transformedNode.args.args:
            if i == 0:
                injected_code = injected_code + arg.arg
            else:
                injected_code = injected_code + ', '+ arg.arg
            i = i + 1
        injected_code = injected_code + '])'
        
        ast_to_inject = parse(injected_code)
        
        if isinstance(transformedNode.body, list):
            transformedNode.body.insert(0, ast_to_inject.body[0])
        else:
            transformedNode.body = [ast_to_inject.body[0], node.body]
        
        fix_missing_locations(transformedNode)
        
        return transformedNode

class Profile:
    __singleton_lock = threading.Lock()
    __singleton_instance = None
    @classmethod
    def getInstance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    @classmethod
    def reset(cls):
        cls.__singleton_instance = None

    @classmethod
    def record(cls, functionName, args):
        cls.getInstance().ins_record(cls, functionName,args)
    
    # instance method
    def __init__(self):
        self.functions_called=[]
        self.functions_called_dict = {}

    def ins_record(self, cls, functionName, args):
        if functionName in self.functions_called_dict:
            self.functions_called_dict[functionName].append(args)
        else:
            self.functions_called_dict[functionName] = [args]

        self.functions_called.append(functionName)
    def printReport(self):
        print("-- methods that use the the same --")
        for key in self.functions_called_dict:
            # if an argument value is repeated print it
            repeated = [ x for x in self.functions_called_dict[key] if self.functions_called_dict[key].count(x) > 1 ]
            if len(repeated) == self.functions_called.count(key):
                print(key, ":", repeated[0])

    
def instrument(ast):
    visitor = Instrumentor()
    return  fix_missing_locations(visitor.visit(ast))