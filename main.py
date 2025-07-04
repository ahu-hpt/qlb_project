import functions
import numpy as np
import ocr_iimgs
import img_to_plot

# input video path
video_path = "./video/qlbdata1.mp4"
output_folder = "./img"

# screenshot/fps
interval = 15  # 默认每隔30帧截取一张图片

# screenshot
extract_frames = functions.extract_frames
extract_frames(video_path, output_folder, interval)

# 计数文件夹里的文件个数
directory = output_folder
count_files_in_directory = functions.count_files_in_directory
file_count = count_files_in_directory(directory) - 1

# 定义要遍历的文件夹路径
folder_path = output_folder
# 每帧计数
frame_count = 0
# 数据数组
data_str = []
# 丢失数组
data_lost = []

# ocr imgs
ocr_imgs = ocr_imgs.ocr_imgs(file_count, folder_path, interval, data_str, data_lost)

data_float = [float(x) for x in data_str]

# 绘图
# 定义万用表绘制的数据列表
Real_time_value = []

Real_time_value = data_float

fps = interval  # 30
Real_time_value = np.array(Real_time_value)

import numpy as np
import pandas as pd

data = data.T
# print(data.shape)
df = pd.DataFrame(data, columns=["Real_time_value"])
df.to_excel("output.xlsx", index=False)

img_del_lj = int(input("Whether to delete imgs of imgs folder( default delete)(1/0): "))
img_del_lj = 1 
if img_del_lj:
    folder_path = output_folder
    del_imgs  = functions.del_imgs(folder_path)
