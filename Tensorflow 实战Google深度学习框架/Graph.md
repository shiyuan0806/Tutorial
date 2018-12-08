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
从上面的结果中可以看出，默认图，新建图，和重置后的图的id是不同的
---


## Tensorflow根据图的变量名获取张量

```
print(const_in_new_graph.name) #打印常量const_in_new_graph 变量名
tensor = new_graph.get_tensor_by_name('const_in_new_graph:0') #通过变量名获取张量
print(tensor)#打印获取的张量

```

- get_tensor_by_name() #根据变量名获取张量

```
const_in_new_graph:0
Tensor("const_in_new_graph:0", shape=(), dtype=float32)
```
从上面的结果中可以看出，const_in_new_graph的变量名是const_in_new_graph:0,根据变量名获取的张量就是const_in_new_graph

---


## Tensorflow获取图中变量操作节点

```
op_ = new_graph.get_operation_by_name('const_in_new_graph')
print(op_)
```
- get_operation_by_name() #获取操作节点 

```
name: "const_in_new_graph"
op: "Const"
attr {
  key: "dtype"
  value {
    type: DT_FLOAT
  }
}
attr {
  key: "value"
  value {
    tensor {
      dtype: DT_FLOAT
      tensor_shape {

      }
      float_val: 2.0
    }
  }
}

```

---


## Tensorflow获取图中元素列表

```
ng = new_graph.get_operations()
print(ng) 

```

- get_operations() #获取元素列表

```
[<tf.Operation 'const_in_new_graph' type=Const>]

```

从上面的结果中可以看出，get_operations获取图中元素列表const_in_new_graph

```
with new_graph.as_default():
    const_value = tf.constant(1., name='const_value')#构建图中构建常量名为const_value的常量const_value
ng = new_graph.get_operations()
print(ng) 

```

```
[<tf.Operation 'const_in_new_graph' type=Const>, <tf.Operation 'const_value' type=Const>]

```

从上面的结果中可以看出，get_operations获取图中元素列表const_in_new_graph，const_value

---

## Tensorflow获取图中对象

-  tf.Graph.as_graph_element(obj, allow_tensor=True, allow_operation=True) #传入一个对象返回一个张量或是一个OP

```
age = new_graph.as_graph_element(const_in_new_graph)#获取const_in_new_graph这个对象
print(age) 
```
- as_graph_element()  #获取对象

```
Tensor("const_in_new_graph:0", shape=(), dtype=float32)
```

---





