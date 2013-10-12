该代码实现了一个简单的des加解密算法
代码使用python2.7实现

各文件说明如下
Box.py: des加密算法各种表的存储
des.py：des加密算法的加解密算法实现，密码和密钥可以为任意字符（例如中文、@……＊＆@#@！等），密钥自动截取二进制化后的前64位作为密钥
example.py: 使用des.py加密图片的一个例子，其中plain.jpg为原始图片，ciper.jpg为加密后的图片，plain1.jgp为解密后的图片

运行方式：
1、图片加解密
安装python2.7后直接在命令行中输入: python example.py
2、des.py自带测试样例
安装python2.7后直接在命令行中输入: python des.py
