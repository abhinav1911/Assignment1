from __future__ import print_function
import sys

class Sandbox(object):
	def __init__(self):
		self.x=None
		
	def _safe_import(self,__import__,list):
		def safe(module_name,globals={},locals={},fromlist=[],level=-1):
			
			if module_name in list:
				return __import__(module_name,globals,locals,level=-1)
				
			else:
				raise ImportError ( 
				"blocked import of " +(module_name) )
			
				
		return safe
  
	def execute(self,string):
		main=sys.modules["__main__"].__dict__
		orgbuiltins=main["__builtins__"].__dict__
		whitelist = set(('ArithmeticError','AssertionError','AttributeError','ImportError','int','print','str','input','__import__','abs','all','set' ))
		
		for builtin in orgbuiltins.keys():
			if builtin not in whitelist:
				del orgbuiltins[builtin]
				
	
		p=Sandbox()	
		safe_modules=["string","re","print_function","__future__"]
		orgbuiltins["__import__"]=p._safe_import(__import__,safe_modules)


		
		
		exec string
		
		
