import os

## 清华源
install_source = 'https://pypi.tuna.tsinghua.edu.cn/simple'

## 读取 requirements.txt 文件
with open('requirements.txt', 'r') as f:
    lines = f.readlines()
   
    for line in lines:
        # 去除行尾换行符并安装依赖
        package = line.strip()
        if package:
            os.system(f'pip install {package} -i {install_source}')