# 机器学习

算法模型对象，在该对象中已经集成好了一个一个的方程(还没求出解的方程) 模型对象的作用，通过非常实现预测或者分类

- 样本数据
  - 特征数据
  - 目标数据
- 模型对象的分类
  - 有监督学习:模型需要的样本数据中存在特征和目标
  - 无监督模型:模型需要的样本数据存在特征
  - 半监督学习:模型需要的样本数据中部分需要特征和目标，部分只需要特征



```
# 导包
import sklearn 
from sklearn.linear_model import LinearRegression  # 线性回归
```

```
# 实例化
linear = LinearRegression() 
```

```
# 训练模型
linear.fit(inshore_city_dist.reshape(-1,1),inshore_city_max_temp)
```

```
# 测试模型
linear.predict([[38]]) 
```

```
# 模型打分
linear.score(inshore_city_dist.reshape(-1,1),inshore_city_max_temp) 
```

```
# 绘制回归曲线
x = np.linspace(10,70,num=100)
y = linear.predict(x.reshape(-1,1))
```

```
plt.scatter(inshore_city_dist,inshore_city_max_temp)
plt.scatter(x,y)
```


$$
$x+y>z$
$$


