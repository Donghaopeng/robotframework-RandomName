# robotframework-RandomName

随机生成中文姓名

支持python：2.x ｜ 3.x

##  功能

- 随机生成2位数的中文姓名，例如：陈某
- 随机生成3位数的中文姓名，例如：王某某
- 随机生成4位数的中文姓名，例如：贺连某某
- 生成的姓名是utf-8编码格式

### TODO

- 暂时没有收录少数名族的姓名


## 使用

### robotframework自动化测试使用

1. 将random_name.py复制到项目的根目录
2. 在你的test suit中添加 Library random_name.py。
3. 库加载成功后，搜索关键字查看是否加载成功
4. 在你的test case中直接引用关键字
5. 举个栗子：

    ```
    ${name}=	Get Name
    log	${name}
    ```


### python程序内使用

TODO

## 更新日志

### 20200403

- 优化生成名字算法
- 生成名字的长度可以自由选择
- 可以选择生成复姓名字