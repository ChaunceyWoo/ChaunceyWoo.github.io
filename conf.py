# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "ChaunceyWoo/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "Duseus's Wiki."
site_logo = "${static_prefix}logo.png"
site_build_date = "2021-03-16T16:51+08:00"
author = "Duseus"
email = "Duseus@scxho.cn"
author_homepage = "https://wiki.scxho.cn"
description = "快让我在雪地上撒点儿野."
key_words = ['Duseus', 'Duseus Wiki', 'wiki', 'scxho']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "山川行貉",
        "url": "https://scxho.cn",
        "brief": "Duseus's Blog"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
            "url": "https://github.com/Duseus",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5144940289/",
        "icon": "gi gi-weibo"
    }
]
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "ywaBjDb93hiusityKRJaXIie-gzGzoHsz",
    "appKey": "m5AKclj0ME0W4wb8XzNhUOGo",
    "visitor": True,
    "recordIP": True
}


head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css">
<script src="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/meting@2/dist/Meting.min.js"></script>
'''

footer_addon = ''

body_addon = ''
