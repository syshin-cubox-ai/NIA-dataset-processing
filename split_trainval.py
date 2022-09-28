import collections
import copy
import json
import os

input_json_path = 'D:/data/nia/indoor_trainval.json'

with open(input_json_path, 'r', encoding='utf-8') as f:
    coco_format_json = json.load(f)

template = collections.OrderedDict(
    {
        'info': coco_format_json['info'],
        'images': None,
        'annotations': None,
        'categories': coco_format_json['categories']
    }
)
train_label = copy.deepcopy(template)
val_label = copy.deepcopy(template)
del template

val_label['images'] = coco_format_json['images'][:10]
val_label['annotations'] = coco_format_json['annotations'][:30]
train_label['images'] = coco_format_json['images'][10:]
train_label['annotations'] = coco_format_json['annotations'][30:]

with open(os.path.join(os.path.dirname(input_json_path), 'indoor_train.json'), 'w', encoding='utf-8') as f:
    json.dump(train_label, f)
with open(os.path.join(os.path.dirname(input_json_path), 'indoor_val.json'), 'w', encoding='utf-8') as f:
    json.dump(val_label, f)
