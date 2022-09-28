import json
import os
import numpy as np
import collections

in_dict = collections.OrderedDict()
out_dict = collections.OrderedDict()

json_dirs = ['indoor/', 'outdoor/']

for cur_folder in json_dirs:
    json_list = os.listdir(cur_folder)
    json_list = [file for file in json_list if file.endswith(".json") or file.endswith(".JSON")]

    for cur_json in json_list:
        with open(cur_folder + cur_json, 'r') as file:
            data = json.load(file)
            obj_anno = data['objects']
            data_cls = data['info.object1.id']
        for cur_anno in obj_anno:
            if 'annotation.object.segmentation' in cur_anno:
                seg_data = cur_anno['annotation.object.segmentation'][0]
                if len(seg_data) > 1:
                    tmp_points_arr = np.zeros((len(seg_data), 2), dtype=np.float32)
                    for i, cur_point in enumerate(seg_data):
                        tmp_points_arr[i] = [cur_point['x'], cur_point['y']]

                    # left, top, w, h
                    left, top = np.min(tmp_points_arr[:, 0]), np.min(tmp_points_arr[:, 1])
                    right, bottom = np.max(tmp_points_arr[:, 0]), np.max(tmp_points_arr[:, 1])
                    w, h = right - left, bottom - top

                    if w < 1:
                        w = 1
                    if h < 1:
                        h = 1

                    bbox = [left, top, w, h]
                    print()
