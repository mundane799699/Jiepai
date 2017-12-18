#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @date    : 2017/12/16
# @file    : test.py

import re
import json
import urllib.parse
import codecs

if __name__ == '__main__':
    html = r"""
    BASE_DATA.galleryInfo = {
    title: '街拍：身材丰满的性感长发美女',
    isOriginal: false,
    mediaInfo: BASE_DATA.mediaInfo,
    gallery: JSON.parse("{\"count\":5,\"sub_images\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\"}],\"uri\":\"origin\\/4e6e0002b61ae1a551f5\",\"height\":1080},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6c0003044e6af41594\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6c0003044e6af41594\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e6c0003044e6af41594\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e6c0003044e6af41594\"}],\"uri\":\"origin\\/4e6c0003044e6af41594\",\"height\":1080},{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/4e6e0002b620c086a13d\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/4e6e0002b620c086a13d\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e6e0002b620c086a13d\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/4e6e0002b620c086a13d\"}],\"uri\":\"origin\\/4e6e0002b620c086a13d\",\"height\":1080},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012babb02be80f\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012babb02be80f\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e7100012babb02be80f\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e7100012babb02be80f\"}],\"uri\":\"origin\\/4e7100012babb02be80f\",\"height\":1080},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012baeafc4412a\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012baeafc4412a\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e7100012baeafc4412a\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e7100012baeafc4412a\"}],\"uri\":\"origin\\/4e7100012baeafc4412a\",\"height\":1080}],\"max_img_width\":720,\"labels\":[\"\\u7f8e\\u5973\",\"\\u6444\\u5f71\"],\"sub_abstracts\":[\" \",\" \",\" \",\" \",\" \"],\"sub_titles\":[\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\"]}"),
    siblingList: [],
    publish_time: '2017-12-16 10:39:57',
    group_id: '6499969132417516045',
    item_id: '6499969132417516045',
    share_url: 'https://m.toutiao.com/group/6499969132417516045/',
    abstract: ''.replace(/<br \/>/ig, ''),
    repin: 0
  }
    """
    # pattern = re.compile('gallery: JSON\.parse\("(.*?)"\),', re.S)
    pattern = re.compile(r'gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(pattern, html)
    if result:
        # print(result.groups())
        # print(result.group(0))
        group1 = result.group(1)
        print(group1)
        # print(urllib.parse.unquote(group1))
        # group2 = '{\"count\":5,\"sub_images\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e6e0002b61ae1a551f5\"}],\"uri\":\"origin\\/4e6e0002b61ae1a551f5\",\"height\":1080},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6c0003044e6af41594\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e6c0003044e6af41594\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e6c0003044e6af41594\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e6c0003044e6af41594\"}],\"uri\":\"origin\\/4e6c0003044e6af41594\",\"height\":1080},{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/4e6e0002b620c086a13d\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/4e6e0002b620c086a13d\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e6e0002b620c086a13d\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/4e6e0002b620c086a13d\"}],\"uri\":\"origin\\/4e6e0002b620c086a13d\",\"height\":1080},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012babb02be80f\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012babb02be80f\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e7100012babb02be80f\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e7100012babb02be80f\"}],\"uri\":\"origin\\/4e7100012babb02be80f\",\"height\":1080},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012baeafc4412a\",\"width\":720,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/4e7100012baeafc4412a\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/4e7100012baeafc4412a\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/4e7100012baeafc4412a\"}],\"uri\":\"origin\\/4e7100012baeafc4412a\",\"height\":1080}],\"max_img_width\":720,\"labels\":[\"\\u7f8e\\u5973\",\"\\u6444\\u5f71\"],\"sub_abstracts\":[\" \",\" \",\" \",\" \",\" \"],\"sub_titles\":[\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\",\"\\u8857\\u62cd\\uff1a\\u8eab\\u6750\\u4e30\\u6ee1\\u7684\\u6027\\u611f\\u957f\\u53d1\\u7f8e\\u5973\"]}'
        # print(group2)
        str = r'{\"count\":5}'
        str2 = '{\"count\":5}'
        # print(str)
        # print(str2)
        # print('%s' % group1)
        # print('{}'.format(group1))
        # print(type(json.loads('"' + group1 + '"')))
        # data = json.loads(group1)
        data = codecs.getdecoder('unicode_escape')(group1)[0]
        json_data = json.loads(data)
        if json_data and 'sub_images' in json_data.keys():
            sub_images = json_data.get('sub_images')
            for item in sub_images:
                print(item.get('url'))


