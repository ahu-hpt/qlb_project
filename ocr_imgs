from cnocr import CnOcr
import re


def ocr_imgs(file_count, folder_path, interval, data_str, data_lost):
    # 遍历文件夹文件(图片)，进行文字识别
    for frame_count in range(file_count):
        img_fp = f"{folder_path}/frame_{interval}_{frame_count}.jpg"
        ocr = CnOcr()  # 所有参数都使用默认值
        out_list = ocr.ocr(img_fp)
        data_list = []
        for dict in out_list:
            text = dict.get('text')
            # 2A 档位 小数点后4位   0.000  
            match = re.search(r'[0-9Oo][.,][0-9Oo][0-9Oo][0-9Oo]|[Q][0-9Oo][0-9Oo][0-9Oo]', text)  # 正则化匹配
            # 20A 档位 小数点后2位  00.00
            if not match:
            match = re.search(r'[0-9Oo][0-9Oo][.,][0-9Oo][0-9Oo]|[0-9Oo][0-9Oo][Q][0-9Oo][0-9Oo]', text)  # 正则化匹配
            # 200A 档位 小数点后2位  000.0
                if not match:
                match = re.search(r'[0-9Oo][0-9Oo][0-9Oo][.,][0-9Oo]|[0-9Oo][0-9Oo][0-9Oo][Q][0-9Oo]', text)  # 正则化匹配
            if match:
                result = match.group()
                result = result.replace('O', '0').replace('o', '0').replace(',', '.')  # 修正数据
                data_list.append(result)
                data_str += data_list
