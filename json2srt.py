# -- coding: utf-8 --

import json
import math
import os

def convert_json_to_srt(json_files_path):    
    json_files = os.listdir(json_files_path)
    srt_files_path = os.path.join(json_files_path, 'srt') #更改后缀后字幕文件的路径    
    isExists = os.path.exists(srt_files_path)
    if not isExists:
        os.mkdir(srt_files_path)
    
    for json_file in json_files:        
        file_name = json_file.replace(json_file[-5:], '.srt') #改变转换后字幕的后缀
        file = ''  # 这个变量用来保存数据
        i = 1
        # 将此处文件位置进行修改，加上utf-8是为了避免处理中文时报错
        with open(os.path.join(json_files_path, json_file), encoding='utf-8') as f:
            datas = json.load(f)# 加载文件数据
            f.close()
                    
        for data in datas['body']:
            start = data['from']  # 获取开始时间
            stop = data['to']  # 获取结束时间
            content = data['content']  # 获取字幕内容
            file += '{}\n'.format(i)  # 加入序号
            hour = math.floor(start) // 3600
            minute = (math.floor(start) - hour * 3600) // 60
            sec = math.floor(start) - hour * 3600 - minute * 60
            minisec = int(math.modf(start)[0] * 100)  # 处理开始时间
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(minisec).zfill(2)  # 将数字填充0并按照格式写入
            file += ' --> '
            hour = math.floor(stop) // 3600
            minute = (math.floor(stop) - hour * 3600) // 60
            sec = math.floor(stop) - hour * 3600 - minute * 60
            minisec = abs(int(math.modf(stop)[0] * 100 - 1))  # 此处减1是为了防止两个字幕同时出现
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(minisec).zfill(2)
            file += '\n' + content + '\n\n'  # 加入字幕文字
            i += 1
        with open(os.path.join(srt_files_path, file_name), 'w', encoding='utf-8') as f:
            f.write(file)  # 将数据写入文件
                        
if __name__ == '__main__':   
    json_folder_path = 'D:\\Data\\00Code\Git\\python_scripts\\src' #json字幕文件的路径（注意路径的格式）
    convert_json_to_srt(json_folder_path)
