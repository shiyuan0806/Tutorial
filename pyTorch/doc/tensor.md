# package-torch.Tensor包详解

## 张量的类型
Torch定义了七种CPU tensor类型和八种GPU tensor类型(如下表):
torch.Tensor是默认的tensor类型（torch.FlaotTensor）的简称
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/pyTorch/images/20181128230534947.png)

## 张量的创建
这里介绍的是torch.Tensor创建张量，有以下几类创建方式:
```
class torch.Tensor
class torch.Tensor(*sizes)
class torch.Tensor(size)
class torch.Tensor(sequence)
class torch.Tensor(ndarray)
class torch.Tensor(tensor)
class torch.Tensor(storage)
```

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

### 规定大小创建
```
#创建3*4大小的Int类型的张量
a = torch.IntTensor(3, 4)
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
"""
a.tensor:tensor([[  42332272,          0,         24,          0],
        [        -1,  808263724, 1668444020, 1767059048],
        [1529374074,    2710832, 1634992169, 1768455209]], dtype=torch.int32)
a.size:torch.Size([3, 4])
"""
#也可以指定填充的值为0
a = torch.IntTensor(3, 4).zero_()
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
"""
a.tensor:tensor([[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]], dtype=torch.int32)
a.size:torch.Size([3, 4])
"""
#初始化创建
a = torch.zeros(3,4)
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
"""
a.tensor:tensor([[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]])
a.size:torch.Size([3, 4])
"""
```

### python的List序列创建
如果提供了python序列，将会从序列的副本创建一个tensor
```
a = torch.Tensor([[1,2,3], [4,5,6]])
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))

"""
a.tensor:tensor([[1., 2., 3.],
        [4., 5., 6.]])
a.size:torch.Size([2, 3])
"""
```

### 从numpy创建
```
a_np = np.arange(1,10)
a = torch.from_numpy(a_np)
b = torch.Tensor(a_np)
print('a_np.numpy:{}'.format(a_np))
print('a_np.size:{}'.format(a_np.shape))
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
print('b.tensor:{}'.format(b))
print('b.size:{}'.format(b.size()))
"""
a_np.numpy:[1 2 3 4 5 6 7 8 9]
a_np.size:(9,)
a.tensor:tensor([1, 2, 3, 4, 5, 6, 7, 8, 9])
a.size:torch.Size([9])
b.tensor:tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.])
b.size:torch.Size([9])
"""
```

### 从已有张量中创建
```
a = torch.Tensor([1,2,3])
b = torch.Tensor(a)
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
print('b.tensor:{}'.format(b))
print('b.size:{}'.format(b.size()))
"""
a.tensor:tensor([1., 2., 3.])
a.size:torch.Size([3])
b.tensor:tensor([1., 2., 3.])
b.size:torch.Size([3])
"""
```
### 对tensor常见API
```
仅记录了我认为比较常用和有用的API。
torch.is_tensor(obj)，若obj为Tensor类型，那么返回True。
torch.numel(obj)，返回Tensor对象中的元素总数。
torch.eye(n)，返回一个单位方阵，和MATLAB的eye()非常像。还有其他参数。
torch.from_numpy(obj)，利用一个numpy的array创建Tensor。注意，若obj原来是1列或者1行，无论obj是否为2维，所生成的Tensor都是一阶的，若需要2阶的Tensor，需要利用view()函数进行转换。
torch.linspace(start, end, steps)，返回一个1维的Tensor。
torch.ones()，与MATLAB的ones很接近。
torch.ones_like(input)，返回一个全1的Tensor，其维度与input相一致。
torch.arange(start, end, step)，直接返回一个Tensor而不是一个迭代器。
torch.zeros()，与MATLAB的zeros很像。
torch.zeros_like()，与torch.ones_like()类似。
torch.cat(seq, dim)，将tuple seq中描述的Tensor进行连接，通过实例说明用法。
torch.chunk（input, chunks, dim），与torch.cat()的作用相反。注意，返回值的数量会随chunks的值而发生变化.
torch.index_select(input, dim, index)，注意，index是一个1D的Tensor。
torch.masked_select(input, mask)，有点像MATLAB中利用bool类型矩阵进行索引的功能，要求mask是ByteTensor类型的Tensor。参考示例代码。注意，执行结果是一个1D的Tensor。
torch.squeeze(input)，将input中维度数值为1的维度去除。可以指定某一维度。结果是共享input的内存的。
torch.t(input)，将input进行转置，不是in place。输出的结果是共享内存的。要求input为2D。
torch.unsqeeze(input, dim)，在input目前的dim维度上增加一维。
好多random sampling的函数接口，还有inplace的。
torch.save()和torch.load()
不常见的运算函数
torch.clamp(input, min, max)，将input的值约束在min和max之间
torch.trunc(input)，将input的小数部分舍去。
torch.norm()
还有一些统计功能的函数。
torch.eq(input, other)，返回一个Tensor。
torch.equal(input, other)，返回True，False。
还有一些用于比较的函数，包括ne(), kthmin(), topk()
torch.grad()，与MATLAB的diag可能不同，这个函数将返回一个与原Tensor维度相同的Tensor。
torch.trace()，
torch.tril()和torch.triu()，返回下三角和上三角Tensor。
有一些用于batch上乘法，加法的函数。
torch.btriface()和torch.btrisolve()，LU分解和线性求解。
torch.dot(), torch.eig(), torch.inverse(), torch.matmul(), torch.mv()等函数。有各种decomposition的函数。
```
---


