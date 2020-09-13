'''
Download image from url that is in markdown file to local folder
AND change url path. 
'''

import os
import requests
from bs4 import BeautifulSoup

ASSETS_FOLDER = './assets/'

def get_files_list(dir):
    """
    获取一个目录下所有文件列表，包括子目录
    :param dir:
    :return:
    """
    files_list = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for file in files:
            if(file.endswith('.md')):
                files_list.append(os.path.join(root, file))
    return files_list


def get_pics_list(html):
    soup = BeautifulSoup(html, features='html.parser')
    pics_list = []
    for img in soup.find_all('img'):
        pics_list.append(img.get('src'))
    return pics_list


def download_imgs(url):
    local_path = ASSETS_FOLDER + os.path.basename(url)
    
    if not os.path.exists(ASSETS_FOLDER):
        os.mkdir(ASSETS_FOLDER)

    if os.path.exists(local_path):
        print('file exist')
        return
    img_data = requests.get(url).content
    with open(local_path, 'w+') as f:
        f.buffer.write(img_data)


def replace_url(file_path, file_text, img_urls):
    for url in img_urls:
        if(url.startswith('http')):
            file_text = file_text.replace(url, ASSETS_FOLDER + os.path.basename(url))
    with open(file_path, 'w') as f:
        f.write(file_text)
    print(f'处理完成。')


def read_md(file_path):
    text = ""
    img_urls = []
    print(f'正在处理：{file_path}')
    with open(file_path, encoding='utf-8') as f:
        text = f.read()
        img_urls = get_pics_list(text)
    for p in img_urls:
        download_imgs(p)
    return text, img_urls


def run():
    flist = get_files_list('./')
    for file_path in flist:
        file_text, imgs = read_md(file_path)
        replace_url(file_path, file_text, imgs)

if __name__ == '__main__':
    run()
