# -- coding: utf-8 --
import torch
import numpy as np
a = torch.Tensor()
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))
"""
a.tensor:tensor([])
a.size:torch.Size([0])
"""

# 创建3*4大小的Int类型的张量
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

a = torch.Tensor([[1,2,3], [4,5,6]])
print('a.tensor:{}'.format(a))
print('a.size:{}'.format(a.size()))

"""
a.tensor:tensor([[1., 2., 3.],
        [4., 5., 6.]])
a.size:torch.Size([2, 3])
"""


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