# -*-coding:utf-8-*-
from pyquery import PyQuery as pq
import sys

filename = '/Users/qinxinghua/Desktop/a.html'

html = '''
    <div id="main">
      <ul id="outer">
        <li class="item0">项目1</li>
        <li class="item1"><a href="1.html">项目2</a></li>
        <li class="item0 active"><a href="2.html"><span class="bold">项目3</span></a></li>
        <li class="item1 active"><a href="3.html">项目4</a></li>
        <li class="item0"><a href="4.html">项目5</a></li>
      </ul>
    </div>
'''

'''
三种初始化方式
'''


# 字符串初始化
def init_string():
    doc = pq(html)
    print(doc("li"))


# url初始化
def init_url():
    doc = pq("http://wwww.baidu.com")
    print(doc("head"))


# 文件初始化
def init_filename(name):
    doc = pq(filename=name)
    print(doc("li"))


'''
查找元素
'''


# 子元素find & children
def find_child():
    doc = pq(html)
    print("find---", doc.find("li"))
    print("children---", doc.children("li"))


# 父元素查找 parent & parents
def find_parent():
    doc = pq(html)
    print("parent --", doc("li.item0").parent())
    print("parentS --", doc("li.item0").parents())


# 兄弟元素 siblings
def find_sublings():
    doc = pq(html)
    print("siblings()--\n", doc(".item1.active").siblings())
    print("li .item0.active--\n", doc(".item1.active").siblings(".item1"))


# 元素遍历
def find_items():
    doc = pq(html)
    for item in doc("li").items():
        print(item(".item0"))


# 获取属性
def find_attr():
    doc = pq(html)
    a = doc("li.item1.active a")
    print(a.attr("href"))
    print(a.attr.href)


# 获取文本
def find_text():
    doc = pq(html)
    a = doc("li.item1.active a")
    print(a.text())


# 获取HTML
def find_html():
    doc = pq(html)
    a = doc("li.item1.active")
    print(a.html())


'''
DOM操作
'''


# addClass removeClass
def add_class():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.add_class("active")
    print(li)


# attr
def attr_test():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.attr("id", "item3")
    print(li)
    li.attr("id", "ITEM3")
    print(li)


# css
def css_test():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.css("font_size", "14px")
    print(li)
    li.css("font_size", "41px")
    print(li)


# remove
def to_remove():
    doc = pq(html)
    li = doc(".item0.active").remove_class("active")
    print(li)
    li.find("span").remove()
    print(li)


if __name__ == "__main__":
    to_remove()
