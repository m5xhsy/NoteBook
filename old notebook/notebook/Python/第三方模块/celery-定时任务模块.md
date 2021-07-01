### Celery组成

```
- Celery 发布任务
- Celery 记录任务的缓存
	- redis / rabbitMQ
	- 任务记录 		 -b roker -任务id
	- 任务返回记录 	- backend
- Celery Worken	 
	- 主动执行任务
	- 主动反馈结果
```

### 创建任务

```python
# task.py
# 创建任务 启动worken命令 $ celery -A task worker -l INFO -c 25		#-A是文件名，-l 是日志输出级别 -c是线程数
import time
from celery import Celery	# 导入模块

# 设置任务记录和任务返回记录的存储redis库
app = Celery("tasks", broker = "redis://:Ass078678@127.0.0.1:6363/0",backend="redis://:Ass078678@127.0.0.1:6363/0")

@app.task
def my_task1(arg):	# 任务
    print("start 1")
    time.sleep(30)
    print("end 1")
    return arg
```

### 执行任务

```python
# 执行任务
from task import my_task

res = my_task.delay()			# 将任务交给worker执行，返回值是一串id
print("task1  ", res)
```

### 监控任务

```python
# 监控任务
from celery.result import AsyncResult
from task import app

async_task = AsyncResult(id="6b0db196-3803-4e43-ac22-0dd9365a3bcc",app=app)	# 通过worker返回的id监控

if async_task.successful():		# 判断是否执行成功 
    result = async_task.get()	# 执行成功获取任务的返回值
    print(result)
```

### 定时任务

```pyrhon

from task import my_task
import time,datetime

tp = time.time()		# 获取时间戳
utc_time = datetime.datetime.utcfromtimestamp(tp)	# 转换成utc时间
add_time = datetime.timedelta(seconds=10)			# 10秒转换成utc时间
utc_time = utc_time + add_time						# 2个时间相加


res = my_task.apply_async(args=("Ass",),eta=utc_time)	# 开启任务
print("id  ", res)
```

### 周期任务

> ── Celery_task
>    ├── task.py
>    ├── task_one.py
>    └── task_two.py

```python
# task.py 	
# 执行 $ celery -A task worker -l INFO	
# 执行 $ celery -A task beat	# 创建任务，如果先执行这个再执行上面命令，先创建的任务也会执行
from celery import Celery
from celery.schedules import crontab

celery_task = Celery(
    "tasks",
    broker="redis://:Ass078678@192.168.239.128:6363/0",
    backend="redis://:Ass078678@192.168.239.128:6363/0",
    include=["task_one", "task_two"]
)

celery_task.conf.beat_schedule = {
    "task_1": {		# 名字可用随便写
        "task": "task_one.my_task_one_01",	# 执行的任务
        "schedule": 10,						# 每隔10秒执行一次
        "args": ("task_1",)					# 参数
    },
    "task_2": {
        "task": "task_one.my_task_one_02",
        "schedule": crontab(hour=24), 		# 第24小时执行一次 
        "args": ("task_2",)
    },
    "task_3": {
        "task": "task_two.my_task_one_01",
        "schedule": crontab(minute=1),		# 每小时的第一分钟执行一次
        "args": ("task_3",)
    },
    "task_4": {
        "task": "task_two.my_task_one_02",
        "schedule": 10,
        "args": ("task_4",)
    }
}



# 补充:		# 建议百度
crontab(minute='*', hour='*', day_of_week='*', day_of_month='*', month_of_year='*')		# 默认参数
crontab(second=30)						# 30秒执行
crontab(minute="*")						# 每分钟执行	
crontab(hour="*/2")						# 每2小时
corntab(hour="9,20")					# 每天9点或者20点
crontab(hour="9-20")					# 每天9点到20点
crontab(hour='9-12,20')					# 每天9点到12点和20点
crontab(minute='*', hour='9-12')		# 每天9点到20点的每分钟
crontab(day_of_month='1,3,5,7,9,11')	# 1、3、5、7、9、11月份每天每分钟执行任务
crontab(0, 0, day_of_month='11', month_of_year='5')	# 每年5月11号的0点0分时刻执行1次任务
crontab(minute=0, hour=0, day_of_month='2-31/2') # 每月偶数天数的0点0分时刻执行1次任务
```

```python
# task_one.py
from task import celery_task

@celery_task.task
def my_task_one_01(a):
    return f"my_task_two_01--{a}"

@celery_task.task
def my_task_one_02(a):
    return f"my_task_two_01--{a}"
```

```python
# task_two.py
from task import celery_task

@celery_task.task
def my_task_two_01(a):
    return f"my_task_two_01--{a}"

@celery_task.task
def my_task_two_02(a):
    return f"my_task_two_01--{a}"
```

