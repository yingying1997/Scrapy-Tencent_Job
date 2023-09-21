# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # 导入 itemadapter 库，用于适配数据项
import csv # 导入 csv 库，用于处理 CSV 文件

# 定义 TencentJobPipeline 类
class TencentJobPipeline:
    # 构造函数，初始化操作
    def __init__(self):
        # 打开 CSV 文件，以追加模式写入，指定编码为 utf-8-sig，确保中文不乱码，设置换行符为空
        self.f = open("腾讯.csv", "a", encoding='utf-8-sig', newline="")
        # 定义 CSV 文件的字段名
        self.fieldnames = ['title', 'responsibility', 'requirement']
        # 创建 DictWriter 对象，用于写入 CSV 文件
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # 写入表头
        self.writer.writeheader()

    # 数据处理函数，用于处理爬取到的数据项
    def process_item(self, item, spider):
        # 写入数据
        self.writer.writerow(item)
        # 返回数据项
        return item
