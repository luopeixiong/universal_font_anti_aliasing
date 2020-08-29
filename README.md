# 环境依赖

# 需要安装依赖
安装tesseract 已经chi_sim数据包

# mac
# brew install tesseract
# brew install tesseract-lang

`
pip install requests
`

使用方法
`
from universal_font_anti_aliasing.anti_aliasing import anti


url = "https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/85226b1a.woff"
s = "丙232"
anti(url, s)

`


