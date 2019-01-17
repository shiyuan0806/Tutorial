# package-torch.Tensor包详解

## 张量的类型
Torch定义了七种CPU tensor类型和八种GPU tensor类型(如下表):
torch.Tensor是默认的tensor类型（torch.FlaotTensor）的简称
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/pyTorch/images/20181128230534947.png)

## 张量的创建
通过torch包的函数进行张量的创建在《Pytorch第一课：package-torch（1）之张量初识》一文中的第2节有详细介绍。
这里介绍的是torch.Tensor创建张量，有以下几类创建方式:
class torch.Tensor
class torch.Tensor(*sizes)
class torch.Tensor(size)
class torch.Tensor(sequence)
class torch.Tensor(ndarray)
class torch.Tensor(tensor)
class torch.Tensor(storage)

### 无参数创建

如果没有提供参数，将会返回一个空的零维张量
```
a = torch.Tensor()
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
"""
a.tensor:tensor([])
a.size:torch.Size([0])
"""
```


