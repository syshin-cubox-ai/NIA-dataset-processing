import glob
import os
import shutil

indoor_img_path = 'D:/data/NIA_original/122-1.다중객체3차원표현데이터(실내)/01.원천데이터'
indoor_label_path = 'D:/data/NIA_original/122-1.다중객체3차원표현데이터(실내)/02.라벨링데이터(2D)'
outdoor_img_path = 'D:/data/NIA_original/122-2.다중객체3차원표현데이터(실외)/01.원천데이터'
outdoor_label_path = 'D:/data/NIA_original/122-2.다중객체3차원표현데이터(실외)/02.라벨링데이터(2D)'

indoor_img = [i for i in glob.glob(os.path.join(indoor_img_path, '**'), recursive=True) if
              os.path.splitext(i)[1] == '.JPG']
indoor_label = [i for i in glob.glob(os.path.join(indoor_label_path, '20220928', '**'), recursive=True) if
                os.path.splitext(i)[1] == '.json']
outdoor_img = [i for i in glob.glob(os.path.join(outdoor_img_path, '**'), recursive=True) if
               os.path.splitext(i)[1] == '.JPG']
outdoor_label = [i for i in glob.glob(os.path.join(outdoor_label_path, '20220928', '**'), recursive=True) if
                 os.path.splitext(i)[1] == '.json']
print(f'indoor_img: {len(indoor_img)}')
print(f'indoor_label: {len(indoor_label)}')
print(f'outdoor_img: {len(outdoor_img)}')
print(f'outdoor_label: {len(outdoor_label)}')

# 종류당 한 폴더씩 복사해두기
indoor_img_path_temp = os.path.join(os.path.dirname(indoor_img_path), 'temp_img')
indoor_label_path_temp = os.path.join(os.path.dirname(indoor_label_path), 'temp_label')
outdoor_img_path_temp = os.path.join(os.path.dirname(outdoor_img_path), 'temp_img')
outdoor_label_path_temp = os.path.join(os.path.dirname(outdoor_label_path), 'temp_label')
shutil.rmtree(indoor_img_path_temp, ignore_errors=True)
shutil.rmtree(indoor_label_path_temp, ignore_errors=True)
shutil.rmtree(outdoor_img_path_temp, ignore_errors=True)
shutil.rmtree(outdoor_label_path_temp, ignore_errors=True)
os.makedirs(indoor_img_path_temp, exist_ok=True)
os.makedirs(indoor_label_path_temp, exist_ok=True)
os.makedirs(outdoor_img_path_temp, exist_ok=True)
os.makedirs(outdoor_label_path_temp, exist_ok=True)
for img in indoor_img:
    shutil.copy(img, indoor_img_path_temp)
for label in indoor_label:
    shutil.copy(label, indoor_label_path_temp)
for img in outdoor_img:
    shutil.copy(img, outdoor_img_path_temp)
for label in outdoor_label:
    shutil.copy(label, outdoor_label_path_temp)

# 이미지, 라벨 쌍 맞추기
indoor_output_path = 'D:/data/nia/indoor'
outdoor_output_path = 'D:/data/nia/outdoor'
os.makedirs(indoor_output_path, exist_ok=True)
os.makedirs(outdoor_output_path, exist_ok=True)

indoor_label = glob.glob(os.path.join(indoor_label_path_temp, '*'))
outdoor_label = glob.glob(os.path.join(outdoor_label_path_temp, '*'))
for label in indoor_label:
    filename = os.path.splitext(os.path.basename(label))[0]
    img = os.path.join(indoor_img_path_temp, filename + '.JPG')
    if not os.path.exists(img):
        print(f'Image not found, skip this label: {img}')
        continue
    shutil.move(img, indoor_output_path)
    shutil.move(label, indoor_output_path)
for label in outdoor_label:
    filename = os.path.splitext(os.path.basename(label))[0]
    img = os.path.join(outdoor_img_path_temp, filename + '.JPG')
    if not os.path.exists(img):
        print(f'Image not found, skip this label: {img}')
        continue
    shutil.move(img, outdoor_output_path)
    shutil.move(label, outdoor_output_path)
