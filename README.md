##
设计思路：
终端输入选择方法类型，
通过常量文件inputTypeConstant将中文转化为对应的function name
分发到analyseWineDataOnOneType.py中对应的方法中。

##
analyseWineDataOnOneType.py具体代码实现参考python数据分析包pandas.

##
请注意：基于mac环境开发，windows系统需要切换文件读取路径，
即analyseWineDataOnOneType.py文件中'templateFiles/wineData.csv'。