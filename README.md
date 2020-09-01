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

# ubuntu
```
apt-get install tesseract-ocr
```

# centos
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

cd /usr/local/share/tessdata/

wget --no-check-certificate https://github.com/tesseract-ocr/tessdata/raw/master/chi_sim.traineddata 

```




# 语言包下载地址 依赖 chi_sim.traineddata
### https://github.com/tesseract-ocr/tessdata
### 下载完成放在安装目录下的tessdata目录下即可


# 安装python第三方包
`
pip install requests
`


demo
在ubuntu下 测试
```
git clone https://github.com/luopeixiong/universal_font_anti_aliasing.git
apt-get -y install tesseract-ocr
cd  universal_font_anti_aliasing
cp lang/chi_sim.traineddata /usr/share/tesseract-ocr/tessdata/chi_sim.traineddata
python3 test_ocr.py
```





