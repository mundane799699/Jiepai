#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @date    : 2017/12/16
# @file    : spider.py
import codecs
import json
import re

import os
from hashlib import md5

import requests
from requests import RequestException
from bs4 import BeautifulSoup
from jiepai.config import *
from multiprocessing import Pool

dir_name = '图片相册'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}

if not os.path.exists(dir_name):
    try:
        os.mkdir(dir_name)
    except Exception as e:
        print('exception:', e)


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    try:
        response = requests.get(url='https://www.toutiao.com/search_content', params=data, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页错误')
        return None
        pass


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            if item and 'article_url' in item.keys():
                yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
        # response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页错误', url)
        return None
        pass


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print('title:', title)
    images_pattern = re.compile(r'gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(images_pattern, html)
    if result:
        # group(0)是原始字符串, group(1)是第一个括号匹配到的字符串
        # groups()以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)
        # codecs: 使不具有转义的反斜杠具有转义功能
        data_str = codecs.getdecoder('unicode_escape')(result.group(1))[0]
        json_data = json.loads(data_str)
        if json_data and 'sub_images' in json_data.keys():
            sub_images = json_data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                'title': title,
                'images': images,
                'url': url
            }
    else:
        print('没有搜索到符合条件的gallery数据', end='\n\n')


def download_image(url):
    print('正在下载图片', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
    except RequestException:
        print('请求图片错误', url)
        pass


def save_image(content):
    # getCurrentDirectory
    # file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    file_path = '{0}/{1}.{2}'.format(dir_name, md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    json_str = get_page_index(offset, KEYWORD)
    json_data = json.loads(json_str)
    if json_data and 'data' in json_data.keys():
        for dataItem in json_data.get('data'):
            if dataItem and 'title' in dataItem.keys():
                title = dataItem.get('title')
                if '街拍' in title:
                    if 'article_url' in dataItem.keys():
                        article_url = dataItem.get('article_url')
                        detail_page = get_page_detail(article_url)
                        images_pattern = re.compile(r'gallery: JSON.parse\("(.*?)"\),', re.S)
                        result = re.search(images_pattern, detail_page)
                        if result:
                            data_str = codecs.getdecoder('unicode_escape')(result.group(1))[0]
                            json_images = json.loads(data_str)
                            if 'sub_images' in json_images:
                                sub_images = json_images.get('sub_images')
                                for sub_image in sub_images:
                                    image_url = sub_image.get('url')
                                    print('image_url =', image_url)
                                    download_image(image_url)



if __name__ == '__main__':
    groups = [x * 20 for x in range(GROUP_START, GROUP_END)]
    pool = Pool()
    pool.map(main, groups)
