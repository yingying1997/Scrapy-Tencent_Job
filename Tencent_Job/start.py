from scrapy import cmdline # 使用 cmdline 模块来执行命令行命令

# 使用 Scrapy 执行名为 spider 的爬虫
cmdline.execute('scrapy crawl spider'.split())