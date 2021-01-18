# selenium_online
在远程服务器上建立 Chrome 并使用 selenium 进行操控，达到代码调试和执行环境分离的作用。  
使用方法：  

```bash
uvicorn main:app --port 8000 --workers 4
```

*注：需安装和建立 Uvicorn 的软链接，pip 安装的路径一般在 Python 安装目录下，和 pip3 同级，如果你用的是我修改过的 [Python3 一键安装脚本](https://raw.githubusercontent.com/senjianlu/kantan-tools/master/Centos7%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85python3/install.sh)的话，直接执行以下语句即可。*

```bash
ln -f /usr/local/python3/bin/uvicorn /usr/bin/pip3
```