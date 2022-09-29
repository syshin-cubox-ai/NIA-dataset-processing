import collections
import datetime
import glob
import json
import os

import cv2
import numpy as np
import tqdm

TYPE = 'indoor'
DATA_ROOT = 'D:/data/nia/' + TYPE

coco_format_json = collections.OrderedDict(
    {
        'info': {
            'date_created': datetime.datetime.now().strftime('%Y/%m/%d'),
            'description': 'NIA4-1 Dataset',
            'version': '1.0',
            'year': datetime.date.today().year,
        },
        'images': [],
        'annotations': [],
        'categories': [
            {'id': 1, 'name': 'human'},
            {'id': 2, 'name': 'lefthand'},
            {'id': 3, 'name': 'righthand'},
        ],
    }
)

if __name__ == '__main__':
    label_paths = sorted(glob.glob(os.path.join(DATA_ROOT, '*.json')))
    for idx, label_path in enumerate(tqdm.tqdm(label_paths, 'Convert format')):
        with open(label_path, 'r', encoding='utf-8') as f:
            label = json.load(f)
            label = collections.OrderedDict(sorted(label.items(), key=lambda t: t[0]))

        img = cv2.imread(os.path.join(DATA_ROOT, label['info.image.id']))
        image = {
            'file_name': label['info.image.id'],
            'height': img.shape[0],
            'width': img.shape[1],
            'id': idx
        }

        """
        try:
            image = {
                'file_name': label['info.image.id'],
                'height': int(label['info.image.height']),
                'width': int(label['info.image.width']),
                'id': idx
            }
        except KeyError:
            image = {
                'file_name': label['meta']['info.image.id'],
                'height': int(label['meta']['info.image.height']),
                'width': int(label['meta']['info.image.width']),
                'id': idx
            }
        """
        coco_format_json['images'].append(image)

        human_bbox = None
        human_segmentation = None
        lefthand_bbox = None
        righthand_bbox = None
        for o in label['objects']:
            if list(o.keys())[0] == 'annotation.human.bbox.2d':
                assert human_bbox is None
                human_bbox = list(o['annotation.human.bbox.2d'].values())
            elif list(o.keys())[0] == 'annotation.human.segmentation':
                assert human_segmentation is None
                human_segmentation = []
                for polygon in o['annotation.human.segmentation'][0]:
                    human_segmentation.append(np.array([list(i.values()) for i in polygon]).flatten().tolist())

            elif list(o.keys())[0] == 'annotation.human.bbox.lefthand':
                assert lefthand_bbox is None
                lefthand_bbox = list(o['annotation.human.bbox.lefthand'].values())
            elif list(o.keys())[0] == 'annotation.human.bbox.righthand':
                assert righthand_bbox is None
                righthand_bbox = list(o['annotation.human.bbox.righthand'].values())

        annotation_human = {
            'segmentation': human_segmentation,
            'area': human_bbox[2] * human_bbox[3],
            'iscrowd': 0,
            'image_id': idx,
            'bbox': human_bbox,
            'category_id': 1,
            'id': len(coco_format_json['annotations'])
        }
        coco_format_json['annotations'].append(annotation_human)
        annotation_lefthand = {
            'area': lefthand_bbox[2] * lefthand_bbox[3],
            'iscrowd': 0,
            'image_id': idx,
            'bbox': lefthand_bbox,
            'category_id': 2,
            'id': len(coco_format_json['annotations'])
        }
        coco_format_json['annotations'].append(annotation_lefthand)
        annotation_righthand = {
            'area': righthand_bbox[2] * righthand_bbox[3],
            'iscrowd': 0,
            'image_id': idx,
            'bbox': righthand_bbox,
            'category_id': 3,
            'id': len(coco_format_json['annotations'])
        }
        coco_format_json['annotations'].append(annotation_righthand)

    output_path = os.path.join(os.path.dirname(DATA_ROOT), 'annotations')
    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, TYPE + '_trainval.json'), 'w', encoding='utf-8') as f:
        json.dump(coco_format_json, f)
