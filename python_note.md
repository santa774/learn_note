### Python基础
#### 基本语法
* 注释：以#开头的语句是注释。 
* 其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块(区别于Java用分号作为一句语句的结束)。  
> Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用4个空格的缩进。
``` python
a = 10
if a >= 0:
    print('yes')
else:
    print('no')
```

#### 数据类型和变量
* **整数**: 没有大小限制，十六进制使用 **0x**前缀和 **0-9**，**a-f**表示， 
例如0xff00，0xa5b4c3d2  
Python有两种除法 **/** 和 **//**  
**/** 除法计算的结果永远是浮点数，如 9 / 3，结果为3.0  
**//** 除法称为地板除，计算结果永远是整数并向下取整，如 10 // 3，结果为3

* **浮点数**：没有大小限制，当长度过长的时候可以用 **e**替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5  

* **字符串**： 字符串是以单引号 **'**或双引号 **"**括起来的任意文本，比如 **'abc'**，**"xyz"**等等。 

* **转义字符**： 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\  
如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
``` python
>>> print('\\\t\\')
\       \
>>> print(r'\\\t\\')
\\\t\\
```

* **布尔值**
布尔值只有True、False两种值。
> 布尔值可以用and、or和not运算。就是与、或、非

* **空值**
空值是Python中特殊的值，用None表示，None不能够和0混淆，0是有意义的值，而None是一个特殊的空值。

* **变量**
Python中的变量在重新赋值的时候可以赋值为任意数据类型，所以Python是动态语言，与之相对的是静态语言，例如Java在变量重新赋值的时候，必须与初始定义的类型一致，否则会报错
``` Python
a = 123
print(a)   #输出: 123
a = true
print(a)   #输出：true
```

#### 字符串和编码
Python的字符串类型是 **str**，使用 **Unicode**编码
对于单个字符的编码，Python提供了 **ord()**函数获取字符的整数表示，**chr()**函数把编码转换为对应的字符：
``` Python
>>> ord('A')
65
>>> ord('中')  
20013
>>> chr(86)
'B'
>>> chr(25991)
'文'
```

对于字节类型 **bytes**的数据用带 **b** 前缀的单引号或双引号表示：
> x = b'ABC'  

要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
``` Python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
``` Python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

要计算str包含多少个字符，可以用len()函数：
``` Python
>>> len('ABC')
3
>>> len('中文')
2
```

len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
``` Python
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
```

可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
``` Python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

**格式化**  
在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
``` Python
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```

%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

常见的占位符有：  

占位符 | 含义 
:-:|:-:
%d | 整数
%s | 字符串
%f | 浮点数
%x | 十六进制整数

其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
``` Python
>>> '%.2f -- %05d' %(3.14159265, 159)
'3.14 -- 00159'
```

如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
``` Python
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
```

#### Python中的集合list和tuple  
list是一种可变的有序集合
tuple是不可变的有序集合

**list**  

* 使用中括号 **[]**，将List的元素括起来。  

* 访问list中的元素： **[i]**  （**i** 是索引，从0开始）

* 获取list元素的长度： **len(list)**  如果要取最后一个元素，还可以使用 **-1** 做索引，表示获取倒数第一个的元素；以此类推，可以获取倒数第二个、倒数第三个的元素  

* 删除list末尾的元素并返回删掉的元素： **pop()**  

* 删除指定索引的元素并返回删掉的元素： **pop(i)**  

* 把某个元素替换成别的元素: **list[2] = 'xxx'**

* list里面的元素的数据类型也可以不同， 比如：L = ['Apple', 123, True]

* list里的元素也可以是另一个list， 比如：
``` Python
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
>>> len(s)
4
```

* 长度为0的list, 比如：L = []


**tuple**  

* tuple叫元组，使用小括号 **()**，将tuple的元素括起来。  tuple和list非常类似，但是tuple一旦初始化就不能修改，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple.

它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]

tuple的陷阱：要定义一个只有1个元素的tuple，如果你这么定义：
``` Python
>>> t = (1)
>>> t
1
```

则变量t是一个整数，而不是一个tuple，由于都是用的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算
dd
