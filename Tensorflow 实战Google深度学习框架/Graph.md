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


## Tensorflow清除计算图

- tf.reset_default_graph()重置计算图

当在搭建网络查看计算图时，如果重复运行程序会导致重定义报错。为了可以在同一个线程或者交互式环境中（ipython/jupyter）重复调试计算图，就需要使用这个函数来重置计算图，随后修改计算图再次运行

需要注意的是,下面三种情况使用这个函数会报错：

```
with graph.as_default():
	#不能用
with tf.Session(): block.
	#不能用
tf.InteractiveSession() 
	#Your regions
	#不能用
sess.close()
```

- reset_default_graph 需要在with tf.session()外部调用

---


## Tensorflow图使用例

### 默认图基本操作

```
#-*- coding: utf-8 -*-
"""
@author: shiyuan
计算图的使用
"""


import tensorflow as tf

a = tf.constant([1.,2.],name = "a")
b = tf.constant([2.,3.],name = "b")
result = a + b

print (a)
print (b)
print (result)

"""
Tensor("a:0", shape=(2,), dtype=float32)
Tensor("b:0", shape=(2,), dtype=float32)
Tensor("add:0", shape=(2,), dtype=float32)
"""

default_graph = tf.get_default_graph()# 获得默认图
print(a.graph)
print(b.graph)
print(result.graph)
print(default_graph)#打印默认图信息

"""
<tensorflow.python.framework.ops.Graph object at 0x7f5e840ab110>
<tensorflow.python.framework.ops.Graph object at 0x7f5e840ab110>
<tensorflow.python.framework.ops.Graph object at 0x7f5e840ab110>
<tensorflow.python.framework.ops.Graph object at 0x7f5e840ab110>
"""

print(a.name) #a 变量名
print(b.name) #b 变量名
print(result.name) #result 变量名
a_tensor = default_graph.get_tensor_by_name('a:0') #通过变量名获取张量
b_tensor = default_graph.get_tensor_by_name('b:0') #通过变量名获取张量
result_tensor = default_graph.get_tensor_by_name('add:0') #通过变量名获取张量
print(a_tensor)#打印获取的张量
print(b_tensor)#打印获取的张量
print(result_tensor)#打印获取的张量

"""
a:0
b:0
add:0
Tensor("a:0", shape=(2,), dtype=float32)
Tensor("b:0", shape=(2,), dtype=float32)
Tensor("add:0", shape=(2,), dtype=float32)
"""

a_op = default_graph.get_operation_by_name('a')
b_op = default_graph.get_operation_by_name('b')
result_op = default_graph.get_operation_by_name('add')
print(a_op)
print(b_op)
print(result_op)

"""
name: "a"
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
        dim {
          size: 2
        }
      }
      tensor_content: "\000\000\200?\000\000\000@"
    }
  }
}

name: "b"
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
        dim {
          size: 2
        }
      }
      tensor_content: "\000\000\000@\000\000@@"
    }
  }
}

name: "add"
op: "Add"
input: "a"
input: "b"
attr {
  key: "T"
  value {
    type: DT_FLOAT
  }
}

"""

ng = default_graph.get_operations()
print(ng) 

"""
[<tf.Operation 'a' type=Const>, <tf.Operation 'b' type=Const>, <tf.Operation 'add' type=Add>]
"""
```
---


### 构建图基本操作

```
#-*- coding: utf-8 -*-
"""
@author: shiyuan
计算图的使用
"""

import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    v = tf.get_variable("v",shape=[1],initializer = tf.zeros_initializer())
print (tf.get_default_graph())
print (g1)
print (v.graph)
print (v)
print (v.name)
v_tensor1 = g1.get_tensor_by_name('v:0') #通过变量名获取张量
print(v_tensor1)#打印获取的张量
v_op1 = g1.get_operation_by_name('v')
print(v_op1)#打印获取的张量
ng1 = g1.get_operations()
print(ng1)
"""
<tensorflow.python.framework.ops.Graph object at 0x7f688316c190>
<tensorflow.python.framework.ops.Graph object at 0x7f68f8fc3ad0>
<tensorflow.python.framework.ops.Graph object at 0x7f68f8fc3ad0>
<tf.Variable 'v:0' shape=(1,) dtype=float32_ref>
v:0
Tensor("v:0", shape=(1,), dtype=float32_ref)
name: "v"
op: "VariableV2"
attr {
  key: "_class"
  value {
    list {
      s: "loc:@v"
    }
  }
}
attr {
  key: "container"
  value {
    s: ""
  }
}
attr {
  key: "dtype"
  value {
    type: DT_FLOAT
  }
}
attr {
  key: "shape"
  value {
    shape {
      dim {
        size: 1
      }
    }
  }
}
attr {
  key: "shared_name"
  value {
    s: ""
  }
}

[<tf.Operation 'v/Initializer/zeros' type=Const>, <tf.Operation 'v' type=VariableV2>, <tf.Operation 'v/Assign' type=Assign>, <tf.Operation 'v/read' type=Identity>]
"""


g2 = tf.Graph()
with g2.as_default():
    v = tf.get_variable("v",shape=[1],initializer = tf.ones_initializer())
print (tf.get_default_graph())
print (g2)
print (v.graph)
print (v)
print (v.name)
v_tensor2 = g2.get_tensor_by_name('v:0') #通过变量名获取张量
print(v_tensor2)#打印获取的张量
v_op2 = g2.get_operation_by_name('v')
print(v_op2)#打印获取的张量
ng2 = g2.get_operations()
print(ng2)

"""
<tensorflow.python.framework.ops.Graph object at 0x7f688316c190>
<tensorflow.python.framework.ops.Graph object at 0x7f688316c590>
<tensorflow.python.framework.ops.Graph object at 0x7f688316c590>
<tf.Variable 'v:0' shape=(1,) dtype=float32_ref>
v:0
Tensor("v:0", shape=(1,), dtype=float32_ref)
name: "v"
op: "VariableV2"
attr {
  key: "_class"
  value {
    list {
      s: "loc:@v"
    }
  }
}
attr {
  key: "container"
  value {
    s: ""
  }
}
attr {
  key: "dtype"
  value {
    type: DT_FLOAT
  }
}
attr {
  key: "shape"
  value {
    shape {
      dim {
        size: 1
      }
    }
  }
}
attr {
  key: "shared_name"
  value {
    s: ""
  }
}
[<tf.Operation 'v/Initializer/ones' type=Const>, <tf.Operation 'v' type=VariableV2>, <tf.Operation 'v/Assign' type=Assign>, <tf.Operation 'v/read' type=Identity>]
"""

with tf.Session(graph = g1) as sess:
     sess.run(tf.global_variables_initializer())
     with tf.variable_scope("",reuse = True):
        print(sess.run(tf.get_variable("v")))

"""
[0.]
"""
with tf.Session(graph = g2) as sess:
     sess.run(tf.global_variables_initializer())
     with tf.variable_scope("",reuse = True):
        print(sess.run(tf.get_variable("v")))


"""
[0.]
"""

```

---


### 图指定设备

```
g=tf.Graph()
# 指定计算运行的设备。
with g.device('/gpu:0'):
    result=a+b
```







