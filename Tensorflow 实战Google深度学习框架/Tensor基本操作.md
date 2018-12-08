# TensorFlow基本类型及操作函数
TensorFlow 中使用 tensor 来代表所有数据，操作间的数据传递也是tensor
tensor 可以看做是一个 n维的数组或列表，
每个tensor都包含 类型(type)， 阶(rank), 形状(shape)

## 类型  
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/496d1b9d-1f7c-40ad-82a2-843e7019bbc7.png)

---

## 阶(rank)

指的是维度。张量的阶和矩阵的阶不是一个概念，主要是看有几层[] 标量、向量、矩阵的阶数
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/a117236b-efd3-45b1-92c5-fff4e447108c.png)

---

## shape

shape用于组织张量内部的组织关系。shape可以通过Python中的整数列表或元组来表示

也可以用 TensorFlow 中的相关函数来描述

---

## tensor的相关操作
主要包括：类型转换、数值操作、形状变换、数据操作
### 类型转换 
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/10ae6c75-c90f-4d3f-80ef-0e0cac5080a5.png)

### 数值操作
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/edc613e8-af16-43c3-9c5e-000253465660.png)

### 形状变换
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/fac0e41c-24ff-485a-a473-25375f60bc06.png)

### 数据操作
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/3698b757-3f7f-4c30-9044-834521302c12.png)

### 算术运算函数
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/72bc509e-2b6d-4f3b-934c-78d8417b0a89.png)

### 矩阵运算 
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/6ad617a1-4d60-423d-b79c-ac09d9386896.png)

### 复数操作    
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/a0a4f068-0c7c-466f-a240-ee2e4e14d70b.png)

### 规约计算
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/819c383e-0ec5-4322-a402-393ea601864a.png)

### 分割
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/0a5721b1-fd65-46fd-bb97-b78d36f0140b.png)

### 序列比较于索引提取
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/60d640e3-9fa9-4bf2-aa2c-2223a65c1e84.png)

### 错误类 
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/3df7354b-2149-4b56-b6b3-5f0f7ec5355d.png)

### 错误类 
![Image text](https://github.com/shiyuan0806/Tutorial/blob/master/Tensorflow%20%E5%AE%9E%E6%88%98Google%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6/images/3df7354b-2149-4b56-b6b3-5f0f7ec5355d.png)

---

## 示例
```
tf.unsorted_segment_sum(tf.constant([0.2, 0.1, 0.5, 0.7, 0.8]),
                        tf.constant([0, 0, 1, 2, 2]), 3)
上面输出结果为：   array([ 0.3,  0.5 , 1.5 ], dtype=float32)
tf.unsorted_segment_sum(tf.constant([[0.2, 0.1, 0.5, 0.7, 0.8],
                                     [0.2, 0.2, 0.5, 0.7, 0.8]]),
                        tf.constant([[0, 0, 1, 2, 2],
                                     [0, 0, 1, 2, 2]]), 3)
上面这个的输出为：  array([ 0.7,  1. ,  3. ], dtype=float32)
如果想要输出下面的结果，应该怎么办呢？
array([ [ 0.3,  0.5 , 1.5 ], [ 0.4, 0.5, 1.5 ] ], dtype=float32)

第一： 通过转置
import tensorflow as tf
with tf.Session() as sess:
    data = tf.constant([[0.2, 0.1, 0.5, 0.7, 0.8],
                        [0.2, 0.2, 0.5, 0.7, 0.8]])
    idx = tf.constant([0, 0, 1, 2, 2])
    result = tf.transpose(tf.unsorted_segment_sum(tf.transpose(data), idx, 3))
    print(sess.run(result))
Output:
[[ 0.30000001  0.5         1.5       ]
 [ 0.40000001  0.5         1.5       ]]

第二：
data = tf.constant([[0.2, 0.1, 0.5, 0.7, 0.8],
                    [0.2, 0.2, 0.5, 0.7, 0.8]])
segment_ids = tf.constant([[0, 0, 1, 2, 2],
                           [0, 0, 1, 2, 2]])
num_segments = 3
rows = []
for data_i, ids_i in zip(data, segment_ids):
    rows.append(tf.unsorted_segment_sum(data_i, ids_i))
result = tf.stack(rows, axis=0)

第三：
num_rows = tf.shape(segment_ids)[0]
rows_idx = tf.range(num_rows)
segment_ids_per_row = segment_ids + num_segments * tf.expand_dims(rows_idx, axis=1)
seg_sums = tf.unsorted_segment_sum(data, segment_ids_per_row,
                                   num_segments * num_rows)
result = tf.reshape(seg_sums, [-1, num_segments])
Output:
array([[ 0.3, 0.5, 1.5 ],
       [ 0.4, 0.5, 1.5 ]], dtype=float32)

```
--- 


