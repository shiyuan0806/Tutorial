# Tensorflow图的基本操作


## Tensorflow默认图构建

```

import tensorflow as tf
default_const = tf.constant(1.)  #默认图中构建常量default_const
print default_const

```

- 默认构建图，并构建图中构造常量default_const

```
Tensor("Const:0", shape=(), dtype=float32)
```

---

## Tensorflow手动构建图


```
import tensorflow as tf
default_const = tf.constant(1.)  #默认图中构建常量default_const
new_graph = tf.Graph()#构建图
with new_graph.as_default():
    const_in_new_graph = tf.constant(2., name='const_in_new_graph')#构建图中构建常量名为const_in_new_graph的常量const_in_new_graph
    print(const_in_new_graph.graph)# 打印常量const_in_new_graph所在构建图信息
    print(new_graph)# 打印手动新建构建图信息
    print(default_const.graph)# 打印默认图信息
default_graph = tf.get_default_graph()# 获得默认图
print(default_graph)#打印默认图信息
tf.reset_default_graph()#重置图
new_graph1 = tf.get_default_graph()#获得重置图后的默认图
print(new_graph1)#打印重置图后的默认图信息

```

- tf.Graph() # 构建图
- tf.get_default_graph() # 获取图
- tf.reset_default_graph() # 重置图

```
<tensorflow.python.framework.ops.Graph object at 0x7fd0424d1310>
<tensorflow.python.framework.ops.Graph object at 0x7fd0424d1310>
<tensorflow.python.framework.ops.Graph object at 0x7fd0424d10d0>
<tensorflow.python.framework.ops.Graph object at 0x7fd0424d10d0>
<tensorflow.python.framework.ops.Graph object at 0x7fd0424d14d0>
```

---

