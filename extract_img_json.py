import os
import glob
import shutil

indoor_img_path = 'D:/data/NIA_2022_1/122-1.다중객체3차원표현데이터(실내)/01.원천데이터'
indoor_label_path = 'D:/data/NIA_2022_1/122-1.다중객체3차원표현데이터(실내)/02.라벨링데이터(2D)'
outdoor_img_path = 'D:/data/NIA_2022_1/122-2.다중객체3차원표현데이터(실외)/01.원천데이터'
outdoor_label_path = 'D:/data/NIA_2022_1/122-2.다중객체3차원표현데이터(실외)/02.라벨링데이터(2D)'

indoor_img = [i.replace('.JPG', '.jpg') for i in glob.glob(os.path.join(indoor_img_path, '**'), recursive=True) if os.path.splitext(i)[1] == '.JPG']
indoor_label = [i for i in glob.glob(os.path.join(indoor_label_path, '**'), recursive=True) if os.path.splitext(i)[1] == '.json']
outdoor_img = [i.replace('.JPG', '.jpg') for i in glob.glob(os.path.join(outdoor_img_path, '**'), recursive=True) if os.path.splitext(i)[1] == '.JPG']
outdoor_label = [i for i in glob.glob(os.path.join(outdoor_label_path, '**'), recursive=True) if os.path.splitext(i)[1] == '.json']

indoor_img_path_temp = os.path.join(indoor_img_path, 'temp')
outdoor_img_path_temp = os.path.join(outdoor_img_path, 'temp')
os.makedirs(indoor_img_path_temp, exist_ok=True)
os.makedirs(outdoor_img_path_temp, exist_ok=True)
for img in indoor_img:
    shutil.copy(img, indoor_img_path_temp)
for img in outdoor_img:
    shutil.copy(img, outdoor_img_path_temp)

indoor_output_path = 'D:/data/nia/indoor'
outdoor_output_path = 'D:/data/nia/outdoor'
os.makedirs(indoor_output_path, exist_ok=True)
os.makedirs(outdoor_output_path, exist_ok=True)
for label in indoor_label:
    shutil.copy(label, indoor_output_path)
    filename = os.path.splitext(os.path.basename(label))[0]
    shutil.move(os.path.join(indoor_img_path_temp, filename + '.jpg'), indoor_output_path)
for label in outdoor_label:
    try:
        filename = os.path.splitext(os.path.basename(label))[0]
        shutil.move(os.path.join(outdoor_img_path_temp, filename + '.jpg'), outdoor_output_path)
        shutil.copy(label, outdoor_output_path)
    except:
        pass
