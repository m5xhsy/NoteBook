# Scrapy

**scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架,集成了高性能异步下载、队列、分布式、解析、持久化等，具有很强的通用性**

- 高性能的数据解析操作(xpath)
- 高性能数据下载(异步)
- 高性能持久化存储
- 中间件
- 全站数据爬取操作
- 分布式
- 请求传参(深度爬取)
- scrapy中合理应用selenium

## 安装

### linux

```shell
$ pip3 install scrapy
```

### windows

1. **下载wheel**

   ```shell
   $ pip3 install wheel
   ```

2. **下载Twisted**

   *打开https://www.lfd.uci.edu/~gohlke/pythonlibs/*

   *Ctrl+F搜索Twisted，找到Twisted‑20.3.0‑cp38‑cp38‑win_amd64.whl并下载(cp38表示python3.8版本)*

3. **进入下载目录并安装Twisted**

   ```shell
   $ pip3 install Twisted-20.3.0-cp38-cp38-win_amd64.whl
   ```

4. **安装pywin32**

   ```shell
   $ pip3 install pywin32
   ```

5. **安装scrapy**

   ```shell
   $ pip3 install scrapy
   ```

## 使用

### scrapy创建工程

```shell
$ scrapy startproject ScrapyDemo			# 创建工程，ScrapyDemo为工程名
$ cd ScrapyDemo								# 进入目录
$ scrapy genspider demo https:www.baidu.com	# 创建爬虫文件，demo为文件名，url为初始url，后续可修改
$ scrapy crawl demo							# 执行爬虫文件
目录结构
├── ScrapyDemo
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       └── __init__.py
└── scrapy.cfg
```

### scrapy数据操作

```python
# 和lxml中xpath使用方式一样，返回的是Selector对象，需要用以下方法获取值
response.xpath("./a/text()")[2].extract()			# 第三个元素的值
response.xpath("./a/text()").extract_first()		# 第一个元素的值
response.xpath("./a/text()").extract()				# 返回的是列表
```

### scrapy持久化存储

- **基于终端指令**

  **命令**

  ```shell
  $ scrapy crawl demo -o file.csv				
  # 将parse方法返回值存储到文件中文件格式(json,csv，xml)
  # 且只能将parse的返回值存储
  ```

  **代码示例**

  ```python
  # demo.py
  import scrapy
  from ScrapyProject.items import ScrapyprojectItem		# 导入items中的类
  
  class DemoSpider(scrapy.Spider):
      name = 'demo'
      allowed_domains = ['dig.chouti.com']
      start_urls = ['http://dig.chouti.com/']
  
      def parse(self, response):
          item = ScrapyprojectItem()	# 实例化items类
          src = response.xpath('//img[@class="matching image-scale"]/@src').extract()	# 爬取数据
          item["content"] = src	# 调用setitem方法赋值
          yield item
  ```

  ```python
  # items.py
  import scrapy
  
  class ScrapyprojectItem(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
      content = scrapy.Field()
  ```

- **基于管道**

  **流程**

  1. *数据解析*
  2. *在item中定义相关属性*
  3. *将解析的数据存储封装到item类型的对象中 item["xxx"] = xxx*
  4. *将数据提交给管道*
  5. *在管道类中的process_item方法负责接收item对象，然后对item对象进行任意形式的持久化存储*
  6. *在配置文件中开启管道*

  **代码示例**

  ```
  # demo.py
  import scrapy
  from ScrapyHY.items import ScrapyhyItem
  
  class DemoSpider(scrapy.Spider):
      name = 'demo'
      # allowed_domains = ['www.huya.com/l']
      start_urls = ['http://www.huya.com/l/']
  
      def parse(self, response):
          li_list = response.xpath('//div[@class="box-bd"]/ul/li[@class="game-live-item"]')
          msg_list = list()
  
          for li in li_list:
              item = ScrapyhyItem()		# 示例化items类
              msg = {						# 解析数据
                  "title": li.xpath('./a[@class="title"]/text()').extract_first(),
                  "url": li.xpath('./a[@class="video-info "]/@href').extract_first(),
                  "anchor": li.xpath('./span[@class="txt"]//i[@class="nick"]/text()').extract_first(),
                  "heat": li.xpath('./span[@class="txt"]//i[@class="js-num"]/text()').extract_first(),
                  "type": li.xpath('./span[@class="txt"]/span[@class="game-type fr"]/a/text()').extract_first()
              }
              item["liveBroadcast"] = msg	# 将msg封装到item中
              yield item					# 将item提交给管道
  ```
  
  
  
  ```
  # pipelines.py
  from redis import Redis
  class ScrapyhyPipeline:
      fp = None
  
      def open_spider(self, spider):		# 打开文件
          print("open file!")
          self.fp = open("liveBroadcast.csv", mode="w", encoding="utf-8")
          self.fp.write("anchor,heat,title,type,url\n")
  
      def process_item(self, item, spider):		# 写入数据
          msg = item["liveBroadcast"]
          self.fp.write(f"{msg.get('anchor')},{msg.get('heat')},{msg.get('title')},{msg.get('type')},{msg.get('url')}\n")
          return item
  
      def close_spider(self, spider):			# 关闭文件
          print("close file!")
          self.fp.close()
  
  
  class RedisPipeline:
      redis = None
      id = 0
  
      def open_spider(self, spider):		# 连接redis
          self.redis = Redis(host="127.0.0.1", port="6379", db=5)
          print("link redis!")
  
      def process_item(self, item, spider):	# 写数据
          if item['liveBroadcast'].get("url") is None:		# 获取出来的url可能为空，所以判断一下
              item["liveBroadcast"]["url"] = "null"
          self.redis.hmset(str(self.id), item["liveBroadcast"])		
          print(item)
          self.id += 1
          return item
  
      def close_spider(self, spider):		# 关闭redis
          self.redis.close()
          print("close redis!")
  ```
  
  
  
  ```
  # items.py
  import scrapy
  
  class ScrapyhyItem(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
      liveBroadcast = scrapy.Field()
  ```
  
  
  
  ```
  # settings.py
  ITEM_PIPELINES = {
     'ScrapyProject.pipelines.ScrapyprojectPipeline': 300,		# 配置本地存储
     'ScrapyHY.pipelines.RedisPipeline': 400,			# 配置redis存储
     # 300和400表示优先级，值越小优先级越高
     # (管道文件中可配置多个类)比如爬取文件分别存在本地和数据库等等
     
  }
  ```

### scrapy手动发送请求

```
import scrapy
from ScrapyHY.items import ScrapyhyItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['www.huya.com/l']
    start_urls = ['http://www.huya.com/l/']

    def parse(self, response):
        # item = ScrapyhyItem()
        li_list = response.xpath('//div[@class="box-bd"]/ul/li[@class="game-live-item"]')
        msg_list = list()

        for li in li_list:
            item = ScrapyhyItem()
            msg = {
                "title": li.xpath('./a[@class="title"]/text()').extract_first(),
                "url": li.xpath('./a[@class="video-info "]/@href').extract_first(),
                "anchor": li.xpath('./span[@class="txt"]//i[@class="nick"]/text()').extract_first(),
                "heat": li.xpath('./span[@class="txt"]//i[@class="js-num"]/text()').extract_first(),
                "type": li.xpath('./span[@class="txt"]/span[@class="game-type fr"]/a/text()').extract_first()
            }
            item["liveBroadcast"] = msg
            yield item

        # 手动发送请求获取其他页面的数据	
        url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page=%d"
        for i in range(2, 3):
            # scrapy.FormRequest(url=url,method="POST",body="",callback=xxx)			# 发送post请求
            yield scrapy.Request(url=url % i, callback=self.get_other_page)				# 通过yield触发，回调函数用来解析数据

    def get_other_page(self, response):
        page_info = response.json()
        live_info = page_info.get("data").get("datas")
        item = ScrapyhyItem()

        for info in live_info:
            # print("------------------------------------------------\n",info)
            x = {
                "title": info.get("introduction"),
                "anchor": info.get("nick"),
                "url": "https://www.huya.com/" + info.get("profileRoom"),
                "heat": str(int(info.get("totalCount")) // 1000 / 10) + "万" if int(
                    info.get("totalCount")) > 10000 else info.get("totalCount"),
                "type": info.get("gameFullName")
            }

            item["liveBroadcast"] = x
            # print(item)
            yield item

```

### scrapy请求传参

**持久化和settings配置和上面差不多**

```python
# items.py
import scrapy

class ScrapymovieItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    detail = scrapy.Field()
    url = scrapy.Field()
```

```
# demo.py
import scrapy
from ScrapyMovie.items import ScrapymovieItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']
    url = "http://www.4567kan.com/frim/index1-%d.html"
    page = 2
    def parse(self, response):
        li_list = response.xpath("/html/body/div[1]/div/div/div/div[2]/ul/li")
        # print(li_list)
        for li in li_list:	# 数据解析
            item = ScrapymovieItem()
            item["name"] = li.xpath('.//div[@class="stui-vodlist__detail"]/h4/a/text()').extract_first()
            item['url'] = "http://www.4567kan.com" + li.xpath('.//a[@class="stui-vodlist__thumb lazyload"]/@href').extract_first()
            yield scrapy.Request(url=item['url'], callback=self.get_movie_detail,meta={"item":item})	# 请求传参(meta为字典)

        if self.page < 6:		# 爬取其他4页
            other_page_url = self.url % self.page
            self.page +=1
            yield scrapy.Request(url=other_page_url, callback=self.parse)		# 解析操作相同，所以调用parse

        # for i in range(2,6):	# 按理来说这个方法会无限循环下去，但是爬取的数据和上面if来爬取的都是171条? ? ?
        #     other_page_url =  self.url%i
        #     yield scrapy.Request(url=other_page_url,callback=self.parse)

    def get_movie_detail(self, response):
        item = response.meta["item"]	# 在response.meta中获取item
        item['detail'] = response.xpath("/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()").extract_first()	# 获取电影详情
        yield item	# 传给管道
```

### scrapy中间件

- **下载中间件**

  位于引擎和下载器之间，用于拦截请求，可用于UA伪装和代理IP

  ```python
  import random
  user_agent_list = [
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
      "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
      "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
      "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
      "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
      "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
      "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
      "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
      "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
      "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
      "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
      "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
  ]
  
  
  class ScrapymiddlewareDownloaderMiddleware:
      def process_request(self, request, spider):
          """
          拦截正常请求
          """
          # UA伪装
          request.headers["User-Agent"] = random.choice(user_agent_list)	# 从UA池中随机获取UA
          print(request.headers)
  
          # IP代理		(这里的IP代理可以放在process_exception中)
          # request.meta["proxy"] = "http://175.42.158.226:9999"
          # print(request.meta["proxy"])
          return None
  
      def process_response(self, request, response, spider):
          """
          拦截所有的响应
          """
          return response
  
      def process_exception(self, request, exception, spider):
          """
          拦截异常请求
          """
          print(request.url)
          print("exception",exception)
          return request		# 将错误的请求处理后返回
  ```

  

- **爬虫中间件**

  位于引擎和爬虫之间

### scrapy中使用selenium

```python
# demo.py
import scrapy
from selenium import webdriver
from ScrapyNetease.items import ScrapyneteaseItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/uav/']
    plate_url = []
	
    # 无头浏览器
    # Chrome = webdriver.ChromeOptions()
    # Chrome.add_argument("headless")
    # br = webdriver.Chrome(options=Chrome,executable_path="G:/chromedriver.exe")
    br = webdriver.Chrome(executable_path="G:/chromedriver.exe")	# 有界面浏览器

    def parse(self, response):
        li_list = response.xpath("/html/body/div/div[3]/div[1]/div[2]/div/ul/li")
        index = [3, 4, 6, 7]	# 国内 国际 军事 航空
        for i in index:	
            item = ScrapyneteaseItem()
            li = li_list[i]		
            href = li.xpath("./a/@href").extract_first()
            self.plate_url.append(href)	# 将url添加进self.plate_url
            yield scrapy.Request(url=href, callback=self.get_news_details, meta={"item": item})	# 手动发送请求获取数据

    def get_news_details(self, response):
        item = response.meta["item"]		# 获取parse中的item
        div_list = response.xpath('//div[@class="ndi_main"]/div[@class="data_row news_article clearfix "]')
        for div in div_list:		# 数据解析
            item["title"] = div.xpath(".//h3/a/text()").extract_first()
            item["href"] = div.xpath(".//h3/a/@href").extract_first()
            yield item		# 提交数据给管道

    def closed(self, spider):  # 方法只在爬虫结束时执行
        self.br.quit()		# 关闭浏览器
```

```python
# items.py
import scrapy
class ScrapyneteaseItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    href = scrapy.Field()
```

```python
# pipeline.py	# 持久化存储
from itemadapter import ItemAdapter

class ScrapyneteasePipeline:
    fp = None

    def open_spider(self, spider):
        self.fp = open("msg.csv",mode="w",encoding="utf-8")
        self.fp.write("title,href\n")

    def process_item(self, item, spider):
        self.fp.write(f'{item["title"]},{item["href"]}\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
```

```python
# middlewares.py		# 中间件
import time
from scrapy import signals
from scrapy.http import HtmlResponse
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyneteaseDownloaderMiddleware:
    def process_response(self, request, response, spider):
        if request.url in spider.plate_url:		# 这里的spider为爬虫文件中的对象,如果请求url在这个列表就重新构建response
            spider.br.get(request.url)	# 打开请求的url

            for i in range(5):	# 循环五次对页面进行翻页，加载动态加载的数据
                spider.br.execute_script("window.scrollTo(0,200000)")
                try:
                    time.sleep(1)	
                    spider.br.find_element_by_class_name('post_addmore').click()	# 个别页面需要点按钮才能加载(这里需要try一下)
                except Exception as e:
                    pass
                
            # url = "",  响应对象对应请求的url
            # body = "", 响应数据
            # encoding = "utf-8",
            # request = request    
            new_response = HtmlResponse(url=request.url, body=spider.br.page_source, encoding="utf-8", request=request)
            return new_response	
        else:
            return response


    def process_exception(self, request, exception, spider):

        pass
```

```python
# settings.py		# 开启管道和中间件
DOWNLOADER_MIDDLEWARES = {
   'ScrapyNetease.middlewares.ScrapyneteaseDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {
   'ScrapyNetease.pipelines.ScrapyneteasePipeline': 300,
}
ROBOTSTXT_OBEY = False
LOG_LEVEL = "ERROR"
```

### scrapy二进制流存储

```python
# pipelines.py

from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ScrapyimagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """
        用来对媒体资源进行请求
        :param item: 接收到爬虫类提交的item
        """
        print("get_media_requests")
        yield scrapy.Request(item["src"])	# 对item中的src发起请求

    def file_path(self, request, response=None, info=None, *, item=None):
        """
        指明数据存储路径
        :return:  返回图片名称
        """
        print("file_path")
        return request.url.split("/")[-1]

    def item_completed(self, results, item, info):
        """
        这个方法可有可无(将item传给下一个即将被执行的管道类)
        """
        print("item_completed")
        return item
```

```python
ITEM_PIPELINES = {		# 开启管道
   'ScrapyImage.pipelines.ScrapyimagePipeline': 300,
}
IMAGES_STORE = "./images"	# 配置存储的文件夹
```

## Scray五大核心组件

![](F:\notebook\notebook\image\爬虫\01.png)

- **引擎(Scrapy)**

  *用来处理整个系统的数据流处理, 触发事务(框架核心)*

- **调度器(Scheduler)**

  *用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址*

- **下载器(Downloader)**

  *用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)*

- **爬虫(Spiders)**

  *爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面*

- **项目管道(Pipeline)**

  *负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。*

## Scrapy配置

```py
# 设置并发(默认情况下32个，提高并发可提高爬虫效率)
CONCURRENT_REQUESTS = 32

# 配置日志输出等级(可设置INFO和ERROR提升爬虫效率)
LOG_LEVEL = "ERROR"			

# 将日志输出到文件(一般不用)
LOG_FILE = "demo.log"

# 禁止cookie可提高效率,有的时候可用不用cookie
COOKIES_ENABLED = False

# 禁止重试
RETRY_ENABLED = False

# 减少下载超时(如果请求时间超过3秒就不要了)
DOWNLOAD_TIMEOUT = 5
```

## CrawlSpider

- 一种基于scrapy进行全站数据爬取的新技术手段
- CrawlSpider就是spider的一个子类
  - LinkExtractor 链接接提取
  - Rule		规则提取

- 流程命令

  ```shell
  $ scrapy startproject ScraptDemo
  $ cd ScraptDemo
  $ scrapy genspider -t crawl demo www.xxx.com
  ```

- 相关代码

  ```python
  import scrapy
  from scrapy.linkextractors import LinkExtractor
  from scrapy.spiders import CrawlSpider, Rule
  
  
  class DemoSpider(CrawlSpider):
      name = 'demo'
      # allowed_domains = ['www.xxx.com']
      start_urls = ['https://www.xxx.com']
  
      rules = (
      	# 将链接提取器提取到的链接进行请求发送且根据指定规则对请求到的数据进行解析
      	# follow=True :将连接提取器 继续作用到提取到的链接所对应的页面
          Rule(LinkExtractor(allow=r'id=\d+&page=\d+'), callback='parse_item', follow=True),
          Rule(LinkExtractor(allow=r'audio/.+'), callback='parse_detail', follow=False),
      )
  
      def parse_item(self, response):
          item = {}
          print(response)
          # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
          # item['name'] = response.xpath('//div[@id="name"]').get()
          # item['description'] = response.xpath('//div[@id="description"]').get()
          return item
          
      def parse_detail(self, response):
          item = {}
          print(response)
          # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
          # item['name'] = response.xpath('//div[@id="name"]').get()
          # item['description'] = response.xpath('//div[@id="description"]').get()
          return item
  ```

## 分布式爬虫

- **搭建一个分布式的机群，然后再机群的每一台电脑上执行同一组程序，让其对某一个网站的数据进行联合分布爬**

- **如何实现分布式？**

  scrapy+scrapy-redis

  ```shell
  $ pip3 install scrapy-redis
  ```

- **步骤**

  ```python
  import scrapy
  # 1.导包
  from scrapy_redis.spiders import RedisSpider
  # from scrapy_redis.spiders import RedisCrawlSpider		# CrawlSpider 
  
  # 2.继承RedisSpider
  class DemoSpider(RedisSpider):
      name = 'demo'
      # 3.注释掉下面2个
      # allowed_domains = ['www.xxx.com']
      # start_urls = ['http://www.xxx.com/']
  
      # 4.设置redis_key
      redis_key = "m5xhsy"       # 可被共享的调度器队列的名称（redis中添加起始url就是用这个名称）
  
      def parse(self, response):
          # 5.数据解析操作
  ```

  ```python
  # settings.py
  # 6 配置共享管道
  ITEM_PIPELINES = {
      "scrapy_redis.pipelines.RedisPipeline":400
  }
  
  # 7.指定scrapy-redis组件中封装好的调度器
  DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"	# 使用scrapy-redis组件的去重队列
  SCHEDULER = "scrapy_redis.scheduler.Scheduler"	# 使用scrapy-redis组件自己的调度器
  SCHEDULER_PERSIST = True	# 是否允许暂停
  
  # 8.配置redis
  REDIS_HOST = '192.168.239.128'
  REDIS_PORT = 6379
  REDIS_ENCODING = ‘utf-8’
  REDIS_PARAMS = {‘password’:’123456’}
  ```

  ```
  # 9.配置redis.conf
  # bind 127.0.0.1
  protected-mode no		# 关闭保护模式
  ```

  ```shell
  # 10.启动redis
  $ redis-server redis.conf
  $ redis-cli
  
  # 11.启动程序
  $ scrapy runspider demo.py
  
  # 12.打开redis-cli向调度器队列放入起始url
  $ lpush m5xhsy https://www.baidu.com
  
  # 13.查看redis中的数据
  $ keys *					# 查看所有健
  $ llen demo:items			# 查看列表长度
  $ lrange demo:items 0 5 	# 查看列表第0-5个元素
  ```


## 增量式爬虫

```python
# demo.pu
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis

class DemoSpider(CrawlSpider):
    name = 'demo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']

    rules = (
        Rule(LinkExtractor(allow=r'frim/index(1|1-\d)\.html'), callback='parse_item', follow=False),	# 解析所有页码
    )
    redis = Redis(host="127.0.0.1",port=6379,password="123456",db=8)	# 实例化一个redis对象

    def parse_item(self, response):
        li_list = response.xpath('//div[@class="stui-pannel_bd"]/ul/li')		# 解析页面对应请求的页面中每一个电影对应的li标签

        for li in li_list:
            url = "http://www.4567kan.com"+li.xpath('./div/a/@href').extract_first()	# 获取电影url
            # 将电影url添加进redis的集合中，如果存在返回0，不存在则返回1并添加 			
            status = self.redis.sadd("url_set", url)				

            if status == 1:		
                item = {
                    "item": {
                        'title': li.xpath('./div/a/@title').extract_first(),	# 解析电影名字
                        'url': url,
                    }
                }
                yield scrapy.Request(url=url,callback=self.get_detail, meta=item)	# 请求传参并对url发起请求
            else:	# 数据以及爬取过，不处理
                pass

    def get_detail(self, response):
        item = response.meta["item"]	# 获取item
        item["detail"] = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item["director"] = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[3]/a/text()').extract_first()
        yield item	# 提交給管道
```

