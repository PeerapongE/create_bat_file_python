import sys
pythonPath = sys.executable
pythonPath

import os
cwd = os.getcwd()
cwd

PythonFileName = 'SimplePython.py'

f = open('RunPython.bat','w')
f.write('chdir ' + cwd + '\n')
f.write(pythonPath  + ' ' + PythonFileName + ' > log_file.txt')
f.close()
