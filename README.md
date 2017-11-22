>  由于BeautifulSoup的语法较为难记，对正则的掌握需要一定的要求，今天介绍另外一个网页解析工具pq，据介绍其用法与jQuery几乎完全一样，如果你懂jq，基本可以兑pq无缝对接的学习

# 安装
`pip3 install pyquery`
# 具体用法
### 0. 导包
`from pyquery import PyQuery as pq`
### 1. 初始化
>* **字符串初始化**
```
html = '''
    <div id="main">
      <ul id="outer">
        <li class="item0">项目1</li>
        <li class="itemn1"><a href="1.html">项目2</a></li>
        <li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
        <li class="itemn1 active"><a href="3.html">项目4</a></li>
        <li class="item0"><a href="4.html">项目5</a></li>
      </ul>
    </div>
'''
# 字符串初始化
def init_string():
    doc = pq(html)
    print(doc("li"))
```
打印结果
```
      <li class="item0">项目1</li>
      <li class="itemn1"><a href="1.html">项目2</a></li>
      <li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
      <li class="itemn1 active"><a href="3.html">项目4</a></li>
      <li class="item0"><a href="4.html">项目5</a></li>
```
>* **url 初始化**
```# url初始化
def init_url():
    doc = pq("http://wwww.baidu.com")
    print(doc("head"))
```
打印结果
```
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<meta content="always" name="referrer"/>
<link rel="stylesheet" type="text/css" href="http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css"/>
<title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title>
</head> 
```

>* **文件初始化** 

将文件路径传入
```# 文件初始化
def init_filename(name):
    doc = pq(filename= '/Users/xxxx/Desktop/a.html')
    print(doc("li"))
```

### 2.css 选择器
当然我对CSS选择器也不是很懂，查了一下资料，暂时当做一种规范写法吧
```
 doc = pq("http://wwww.baidu.com")
 print(type(doc))
```
通过打印doc的类型，返回类型是
`<class 'pyquery.pyquery.PyQuery'>`，而且在以下介绍的各个筛选方法中每一次筛选都是返回一个这样类型的对象，所以是可以通过传入选择器参数，不断的去筛选想要的结果，然后可以类比jQuery的css选择器，通过doc(参数)筛选需要的内容，规则如下
* 通过id筛选： #id
* 通过class选择：.class名
* 通过元素选择：元素名
* 层级关系： 如果同时写以上几种筛选条件
  * 并用空格分隔条件，表示在每一层筛选条件之内进行筛选，但是不仅仅是父子关系，只要满足在根节点一下的所有的子孙节点均会被筛选出来
  * 如果不用空格分割，表示在几种条件同事满足
* 例子
 >**doc("#outer  .item0")** 
```
<li class="item0">项目1</li>
      <li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
      <li class="item0"><a href="4.html">项目5</a></li>
```
**表示在id 为`outer`的元素的子元素class为`item0`元素**

> **doc(".item0.active")**
```
<li class="item0 active">
<a href="2.html">
<span class="bold">
项目3
</span>
</a>
</li>
```
**表示class 是item0 并且class为active的元素**

### 3.元素查找
> * **子元素：find  & children**
* find：查找所有符合元素的子元素，包括子元素的子元素，子子孙孙无穷尽也
* children：直接子元素
* 举个🌰，看看区别
```
def find_element():
    doc = pq(html)
    print("find---", doc.find("li"))
    print("children---", doc.children("li"))
```
打印结果
```
find--- <li class="item0">项目1</li> 
        <li class="itemn1"><a href="1.html">项目2</a></li> 
        <li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
        <li class="itetive"><a href="3.html">项目4</a></li>
        <li class="item0"><a href="4.html">项目5</a></li>
children--- 
```

**解析：find就不用解释了，由于直接子元素中没有`li`元素，所以打印为空**

>* **父元素：parent & parents** 
* parent：直接父节点，返回最多一个值
* parents：返回筛选点的之上层次的每一层的父节点
* 举个🌰，看看区别:
```
def find_parent():
    doc = pq(html)
    print("parent --", doc("li.item0").parent())
    print("parentS --", doc("li.item0").parents())
```
打印结果                                                                                  ![](http://upload-images.jianshu.io/upload_images/954728-1a02a4f55a330d74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>* **兄弟元素siblings**

筛选同级别的元素，同样是可以传入CSS样式进行再一次筛选，看🌰
```
# 兄弟元素 siblings
def find_sublings():
    doc = pq(html)
    print("siblings()--\n", doc(".item1.active").siblings())
    print("li .item0.active--\n", doc(".item1.active").siblings(".item1"))
```
打印结果
```
siblings()--
 <li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
        <li class="item1"><a href="1.html">项目2</a></li>
        <li class="item0">项目1</li>
        <li class="item0"><a href="4.html">项目5</a></li>
      
li .item0.active--
 <li class="item1"><a href="1.html">项目2</a></li>
```

### 4.元素遍历 items()
对于返回值是多个元素，然后对每个元素做处理，需要调用items方法，返回的`generator`类型，可以通过for 循环去取值
```
def fine_items():
    doc = pq(html)
    for item in doc("li").items():
        print(item())
```
打印结果
```
<li class="item0">项目1</li>
        
<li class="item1"><a href="1.html">项目2</a></li>
        
<li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item1 active"><a href="3.html">项目4</a></li>
        
<li class="item0"><a href="4.html">项目5</a></li>

```
也可以将遍历的值继续进行筛选
```
def fine_items():
    doc = pq(html)
    for item in doc("li").items():
        print(item(".item0"))
```
打印结果
```
<li class="item0">项目1</li>
        
<li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0"><a href="4.html">项目5</a></li>
```

### 5.获取属性attr()，文本text()，HTML便签html()
> 获取属性

获取元素的属性，这个不用过多解释，获取属性由两种写法，以a标签的`href`属性为例，比如变量a是筛选出来的a标签：
* a.attr("href")
* a.attr.href
```
def find_attr():
    doc = pq(html)
    a = doc("li.item1.active a")
    print(a.attr("href"))
    print(a.attr.href)
```
打印结果
```
3.html
3.html
``` 
> 获取文本

文本主要是包含在HTML标签内的内容，不包含标签
```
def find_text():
    doc = pq(html)
    a = doc("li.item1.active a")
    print(a.text())
```
打印结果
```
项目4
```
> 获取HTML
```
def find_html():
    doc = pq(html)
    a = doc("li.item1.active")
    print(a.html())
```
打印结果
```
<a href="3.html">项目4</a>
```

### 6.DOM操作(讲解部分操作)
> addClass 、 removeClass
```
def add_class():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.add_class("active")
    print(li)
```
打印结果
```
<li class="item0"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
```
> attr、 css

**attr:** 
* 修改属性，如果此属性已经存在就修改，没有的话就增加此属性
* 参数：两个参数，第一个为属性名字，第二个为属性值
```
def attr_test():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    li.attr("id", "item3")
    print(li)
    li.attr("id", "ITEM3")
    print(li)
```
打印结果
```
<li class="item0"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0" id="item3"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0" id="ITEM3"><a href="2.html"><span class="bold">项目3</span></a></li>
```

**css: 同attr** 
```
def css_test():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.css("font_size", "14px")
    print(li)
    li.css("font_size", "41px")
    print(li)
```
打印结果
```
<li class="item0"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0" style="font-size: 14px"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0" style="font-size: 41px"><a href="2.html"><span class="bold">项目3</span></a></li>
```
> remove : 删除
应用场景就是先筛选然后删除，为了做进异步筛选备用
```
def to_remove():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.find("span").remove()
    print(li)
```
打印结果
```
<li class="item0"><a href="2.html"><span class="bold">项目3</span></a></li>
        
<li class="item0"><a href="2.html"/></li>
```

# 更多内容 
请查看[PyQuery官方文档](http://pyquery.readthedocs.io/en/latest/api.html)
