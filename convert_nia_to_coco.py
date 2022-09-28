import collections
import datetime
import glob
import os
import json

with open('D:/data/indoor/coco.json', 'r', encoding='utf-8') as f:
    coco = json.load(f)

with open('D:/data/indoor/nia.json', 'r', encoding='utf-8') as f:
    nia = json.load(f)

with open('D:/data/debug.json', 'r', encoding='utf-8') as f:
    a = json.load(f)

convert_json = collections.OrderedDict(
    {
        'info': {
            'date_created': datetime.datetime.now().strftime('%Y/%m/%d'),
            'description': 'NIA4-1 Dataset',
            'version': '1.0',
            'year': datetime.date.today().year,
        },
        'images': [],
        'annotations': [],
        'categories': [],
    }
)

# 예시
image = {
    'file_name': 'COCO_val2014_000000001268.jpg',
    'height': 427,
    'width': 640,
    'id': 1268  # image마다 id 설정
}
annotation = {
    'segmentation': [
        [
            192.81,
            247.09,
            219.03,
            249.06
        ]
    ],
    'area': 1035.749,
    'iscrowd': 0,
    'image_id': 1268,  # image의 id를 연결
    'bbox': [  # upper-left x,y and wh
        192.81,
        224.8,
        74.73,
        33.43
    ],
    'category_id': 0,  # category의 id를 연결
    'id': 42986  # annotation마다 id 설정
}
category = {
    'id': 0,  # category마다 id 설정
    'name': 'person',
}

exit()
