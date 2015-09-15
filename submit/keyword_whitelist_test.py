from sandbox import Sandbox

s=Sandbox()
code ="""
file("file.txt",'w').write("verma")

"""

s.execute(code)
