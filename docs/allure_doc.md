## 函数介绍
函数                             :备注
@allure.epic()                   :项目名称          
@allure.feature()                :模块名             
@allure.story()                  :子模块           
@allure.title(用例的标题)         :用例标题                     
@allure.severity()               :包括:blocker,critical,nomal,minor,trivial              
@allure.step()                   :测试步骤          
@allure.description()            :可以写预期结果                 
@allure testcase(url)            :链接到测试用例系统                 
@allure.issue(url)               :链接到bug系统              
@allure.link(url)                :一般可以链接到被测系统地址             
@allure.attachment()             :一般可以添加截图或者日志       

## 界面介绍
Overview：总览，显示用例执行情况、严重程度分布、环境信息等。
Categories：分类，按用例执行结果分类，异常错误和失败错误。
Suites：套件，按测试用例套件分类，目录 ->测试文件 -> 测试类 ->测试方法。
Graphs：图表，显示用例执行分布情况，状态、严重程度、持续时间、持续时间趋势、重试趋势、类别趋势、整体趋势。
Timeline：时间线，显示用例耗时情况，具体到各个时间点用例执行情况
Behaviors：行为，按用例行为举止分类（以标记文字形式显示，需要用例添加allure相关装饰器）
Package：配套，按目录形式分类，显示不同的目录用例执行情况。












