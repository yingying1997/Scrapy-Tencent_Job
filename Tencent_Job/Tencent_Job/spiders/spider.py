# 目标网站：腾讯招聘网站 https://careers.tencent.com/search.html?pcid=40001
# 需求翻页获取前10页数据：
# 爬取首页的职位名字-详情页的工作职责和工作要求

import scrapy # 导入 scrapy 库，用于构建爬虫
import json # 导入 json 库，用于处理 JSON 数据
import datetime # 导入 datetime 库，用于获取当前时间
from Tencent_Job.items import TencentJobItem # 导入自定义的数据项类 TencentJobItem

# 定义 SpiderSpider 类，继承自 scrapy.Spider 类
class SpiderSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'spider'
    # 允许爬取的域名
    allowed_domains = ['careers.tencent.com']
    # 获取当前时间
    current_time = datetime.datetime.now()
    # 将当前时间转换为时间戳字符串
    post_time = str(int(current_time.timestamp()))
    # 初始页码
    page = 1
    # 链接 url
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area='
    # 起始 url
    start_urls = [base_url.format(post_time,page)]

    # 定义解析函数，用于解析响应数据
    def parse(self, response):
        # 从响应中获取数据列表
        datas = json.loads(response.text)['Data']['Posts']
        # 遍历数据列表
        for data in datas:
            # 职位名字
            title = data['RecruitPostName']
            # PostId
            post_id = data['PostId']
            # 详情页 url
            post_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=' + self.post_time + '&postId=' + post_id + '&language=zh-cn'
            # 发送请求并指定回调函数以及传递的参数
            yield scrapy.Request(post_url, callback=self.detail_pages, cb_kwargs={'title': title})

        # 判断页码
        if self.page < 10:
            # 页码
            self.page = self.page + 1
            # 发送请求并指定回调函数
            yield scrapy.Request(self.base_url.format(self.post_time,self.page), callback=self.parse)

    # 定义职位详情页解析函数
    def detail_pages(self, response, **title):
        # 创建爬取的数据项
        item = TencentJobItem()
        # 职位名字
        item['title'] = title['title']
        # 工作职责
        item['responsibility'] = json.loads(response.text)['Data']['Responsibility']
        # 工作要求
        item['requirement'] = json.loads(response.text)['Data']['Requirement']
        # 返回数据项
        yield item
