![图片](https://user-images.githubusercontent.com/20177836/149867689-b0ed642f-e287-4066-a2d9-d7354f81209f.png)
![图片](https://user-images.githubusercontent.com/20177836/149867714-dffe830c-45d8-417d-b152-5e2e8703a09e.png)


# 初衷

> 最近看了一个书，叫做《成为可怕的自律人》，其中有个观点是可以有一个List来给自己做的事进行打分评估，以此来判断List完成的状态。具体可以看看我得书摘[成为可怕的自律人](https://www.emperinter.info/2022/01/12/triggers-creating-behavior-that-lasts-becoming-the-person-you-want-to-be/) 。刚开始我是搞了一个Excel的（如下），主要有4点：process（事件完成度）、emotion（情绪状态）、energy(精神，最近有点犯困)、以及keywords（关键字，今天的小总结吧）。前3个都是10分制，后面那个可以弄成一个词云图。后来想想还是用技术人的角度搞个轮子吧，顺便学点小东西。

![图片](https://user-images.githubusercontent.com/20177836/149657815-798f1e57-4b49-4c25-a874-aeebbf868761.png)


# 设计

- Python
- Django【网页版部署，随时随地可用】


# 逻辑

## 页面说明

| 页面 | 作用 |
|:---:|:---:|
| 注册页面 | 默认首页,用的最少，跳转后到管理页面 |
| 管理页面 | 填写数据相关信息的页面，用的最多 |
| 可视化 | 首页的一个按钮跳转 |

## 流程

- 注册（仅一次），注册后自动跳转到管理页面
- 填写相关信息
- 点击跳转到可视化页面
- 可视化首页可跳转到管理页面
- 只能管理页面注销登录
