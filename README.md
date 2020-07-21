# Cardinal_Runtime
## 开发
基于Python 和 PySide2开发,请安装依赖
```
莫得问题，看一下你需要多少依赖就装多少（记得在wrapper.py引用模块后再打包）
```

它短小精悍，却可以为多平台直接执行Python代码提供可能。利用Pyinstaller的打包，可以保证无依赖缺少，同时不会影响源程序执行。

## 使用方法
1 . 在所需执行的Python文件目录下创建RunSupport.json  
格式：
```json
{
  "Script": "Show"
}
```
Tips: Script字段的数据不要加.py (wrapper是把你的程序当作一个模块引用的)

2 . 使用以下命令启动程序
```shell script
wrapper [python程序所在目录 -> 一定要是目录！] [传入参数]
```

windows用户使用wrapper.exe执行
