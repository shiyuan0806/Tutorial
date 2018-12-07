# Tensorflow图的基本操作


## Tensorflow默认图构建

```

import tensorflow as tf
default_const = tf.constant(1.)  #默认图中构建常量default_const
print default_const

```

- 默认构建图，并构建图中构造常量default_const

```
'Tensor("Const:0", shape=(), dtype=float32)'
'''
