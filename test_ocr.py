# coding:utf-8

from universal_font_anti_aliasing.anti_aliasing import anti


if __name__ == '__main__':
    url = "https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/85226b1a.woff"
    s = "丙232"
    print("result is :", anti(url, s).decode("utf-8"))
