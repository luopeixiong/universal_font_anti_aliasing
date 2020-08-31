# 环境依赖

# 需要安装依赖
安装tesseract 已经chi_sim数据包

# mac
### brew install tesseract
### brew install tesseract-lang

# window
下载安装包
https://github.com/UB-Mannheim/tesseract/wiki
### 配置环境变量

# linux
### 请参考 https://blog.csdn.net/wanght89/article/details/78329546
```console
wget http://www.leptonica.org/source/leptonica-1.74.4.tar.gz

tar -xvf leptonica-1.74.4.tar.gz

cd leptonica-1.74.4

./configure

make 

make install

yum install automake

yum install libtool


wget https://github.com/tesseract-ocr/tesseract/archive/3.04.00.tar.gz

tar -xvf 3.04.00.tar.gz

cd tesseract-3.04.00

./configure

make 

make install

wget --no-check-certificate https://github.com/tesseract-ocr/tessdata/raw/master/chi_sim.traineddata 

```




# 语言包下载地址 依赖 chi_sim.traineddata
### https://github.com/tesseract-ocr/tessdata
### 下载完成放在安装目录下的tessdata目录下即可


# 安装python第三方包
`
pip install requests
`

```python
from universal_font_anti_aliasing.anti_aliasing import anti



url = "https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/85226b1a.woff"
s = "丙232"
anti(url, s)

```




