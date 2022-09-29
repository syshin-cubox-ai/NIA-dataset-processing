import collections
import copy
import json
import os

TYPE = 'indoor'
input_json_path = f'D:/data/nia/annotations/{TYPE}_trainval.json'

with open(input_json_path, 'r', encoding='utf-8') as f:
    coco_format_json = json.load(f)

template = collections.OrderedDict(
    {
        'info': coco_format_json['info'],
        'images': [],
        'annotations': [],
        'categories': coco_format_json['categories']
    }
)
train_label = copy.deepcopy(template)
val_label = copy.deepcopy(template)
del template

val_img_id = []
for i in range(len(coco_format_json['images'])):
    if i % 10 == 0:
        val_img_id.append(i)
        val_label['images'].append(coco_format_json['images'][i])
    else:
        train_label['images'].append(coco_format_json['images'][i])

for ann in coco_format_json['annotations']:
    if ann['image_id'] in val_img_id:
        val_label['annotations'].append(ann)
    else:
        train_label['annotations'].append(ann)

with open(os.path.join(os.path.dirname(input_json_path), f'{TYPE}_train.json'), 'w', encoding='utf-8') as f:
    json.dump(train_label, f)
with open(os.path.join(os.path.dirname(input_json_path), f'{TYPE}_val.json'), 'w', encoding='utf-8') as f:
    json.dump(val_label, f)
