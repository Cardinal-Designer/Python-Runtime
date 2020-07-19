from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia
from PySide2.QtCore import Signal
import os,sys,json
agrv = sys.argv
sys.path.append(agrv[1])

next_ = None
if os.name == 'nt':
    next_ = '\\'
else:
    next_ = '/'
# 针对 Linux 和 windows 的不同，更改路径中的 反斜杠(\) 或 斜杠(/)

RunSupport = agrv[1]+next_+'RunSupport.json'

with open(RunSupport,'r+') as f:
    RunInfo = json.loads(f.read())
sys.argv = sys.argv[1:]
Run = __import__(RunInfo['Script'])
