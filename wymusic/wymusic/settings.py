# -*- coding: utf-8 -*-

# Scrapy settings for wymusic project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wymusic'

SPIDER_MODULES = ['wymusic.spiders']
NEWSPIDER_MODULE = 'wymusic.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wymusic (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wymusic.middlewares.WymusicSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'wymusic.middlewares.WymusicDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wymusic.pipelines.WymusicPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

C={
    "cookie": "JSESSIONID-WYYY=45k5pA9BracFAc%5CTz3PawzgA8Ttneto%2B0WtMeazx05NdgkqVTNx2igkH%2Bu8PZ1UYIFWdsSEBH94O9AsmPSkozYARrkBUmnjP6B8F%2F5sa1u1EiA8OcfNgqqMYhyOOcZZKgkpFSSQa9XYefVBl%2FNXfDbM8U05dj0U4cMVahM30HANPc1fT%3A1565927263575; _iuqxldmzr_=32; _ntes_nnid=4b81edd666e38f5522e93604c2381084,1565925463606; _ntes_nuid=4b81edd666e38f5522e93604c2381084; WM_NI=IGg6dnOXSC8TCxgd8m%2BqZqbWz4%2FO6Z0k6s7fKcbsfH5hEPh90kQlSlrYk2j5VTXa9QlZA%2FiAqHWKtC%2F9midaYTmsed2Pf5fkKjajTCjJyr71q0UBW8eF6GCsFp%2F%2F5%2BrHRWw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5ae44a198a3b8b34985a88ba6c45b978b9e84bb659b958b86e13cf7bc8887ee2af0fea7c3b92a8b99a9d7e7668d889da4bb6081a8a985bb67e9af9692e15dbaece1b0b552f4b5fa94b66e89bdae94e544f7b88bb1eb33f4b59f8dd268b287a5d3e93f968c9882bc5bb0868fd0ec4bb39899acf749ede7a38ae76b9b8ca394e870f290aad6e56189b6af8bd749aa96b793b63bb3f09ba3d634a79afaa8c27986b0e1d0b821b2989eb8f637e2a3; WM_TID=cRxKZEROxL1BRUAUFUN88dOEffkoISas"
}