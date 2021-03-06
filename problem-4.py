# from distutils import extension
# import glob, os
# from msilib.schema import Directory
# import os

# print("Please input the Directory")
# directory = input()
# print("Please input the Extension")
# extension = input()

# from pathlib import Path

# def recursive_walk(folder):
    
#     for folderName, subfolders, filenames in os.walk(folder):
#         for filename in filenames:
#             _extension = filename.split(".")[len(filename.split(".")) - 1]
#             if(_extension == extension):    
#                 if subfolders:
#                     for subfolder in subfolders:
#                         recursive_walk(subfolder)
#                 print('\nFolder: ' + folderName + '\n')
#                 print("\t" + filename + '\n')

# recursive_walk(directory)


class Interpreter:
    def __init__(self):
        pass

    def run(self,code):
        for xs in code:
            self.eval(xs)


    # This is our magic function. It evauates xs parameter 
    # according to its first element  and calls appropriate 
    # member function and passes the parameter to that function.
    # If xs is not a list then returns xs itself:

    def eval(self,xs):
        if isinstance(xs,list):
            return self.__getattribute__(xs[0])(xs)
        return xs


    # Our first function (or opcode) is Print. If last item 
    # is a comma it doesn't print newline:  

    def Print(self,xs):
        if len(xs)==1:
            print()
            return
        l=len(xs)-1
        for i,x in enumerate(xs[1:]):
            e=self.eval(x)
            if i<l-1:
                print(e,end="")
            else:
                if e!=",":
                    print(e)
                else:
                    print(e,end="")

# This is AST (Abstract Syntax Tree) generated by 
# parser. Consisting of recursive lists
# (No, not lisp :P )
code=[
    ["Print","Hello World!","Sky is blue"],
    ["Print",1,","],
    ["Print",2,","],
    ["Print",3],
    ["Print","a"],
    ["Print","b"],
    ["Print"],
    ["Print","c"],
]

interpreter=Interpreter()

interpreter.run(code)