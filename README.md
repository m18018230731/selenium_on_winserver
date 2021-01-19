# selenium_online
在远程服务器上建立 Chrome 并使用 selenium 进行操控，达到代码调试和执行环境分离的作用。  

**环境准备（Windows 下的环境配置较为简单，不作记录）**
```bash
# psycopg2 模块环境
yum install postgresql postgresql-devel python-devel python3-devel
# Python3 依赖包
pip3 install requests
pip3 install selenium
pip3 insatll beautifulsoup4
pip3 install psycopg2
# rab_chrome.py 所需的 Chrome 无界面浏览器运行环境
# 具体教程：https://my.oschina.net/u/4411210/blog/4286772
# 主要目的为安装 Chrome 和下载同版本 chromedriver 并建立软链接
yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
wget  https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
ln -f /root/chromedriver /usr/bin/chromedriver
```

**Linux 启动方法：**  

```bash
uvicorn main:app --port 8000 --workers 4
```

*注：需安装和建立 Uvicorn 的软链接，pip 安装的路径一般在 Python 安装目录下，和 pip3 同级，如果你用的是我修改过的 [Python3 一键安装脚本](https://raw.githubusercontent.com/senjianlu/kantan-tools/master/Centos7%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85python3/install.sh)的话，直接执行以下语句即可。*

```bash
ln -f /usr/local/python3/bin/uvicorn /usr/bin/uvicorn
```  

**Windows 启动方法：**  
直接运行 [启动.bat](https://raw.githubusercontent.com/senjianlu/selenium-online/main/%E5%90%AF%E5%8A%A8.bat)，视服务器情况适当修改线程数，同时注意多线程情况下如果访问网站不同请尽量使用不同端口，以免发生 driver 失效的情况。
