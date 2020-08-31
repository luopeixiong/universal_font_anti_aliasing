# coding:utf-8

import os

import platform
from ctypes import CDLL, c_char_p, RTLD_GLOBAL
from . import woff2tff



base_dir = os.path.dirname(__file__)


def load_dll():
    sys = platform.system()
    print(sys)
    if sys == "Windows":
        dll = CDLL(os.path.join(base_dir, "tyc_ocr_win.so"), RTLD_GLOBAL)
    elif sys == "Linux":
        dll = CDLL(os.path.join(base_dir, "tyc_ocr_linux.so"), RTLD_GLOBAL)
    elif sys == "Darwin":
        dll = CDLL(os.path.join(base_dir, "tyc_ocr.so"), RTLD_GLOBAL)
    else:
        raise ValueError("Unkown platform")
    return dll

dll = load_dll()
dll.NewOcr.argtype = c_char_p
dll.NewOcr.restype = c_char_p


# 需要安装依赖
# mac
# brew install tesseract
# brew install tesseract-lang


def anti(url, s):
    """
    目前只支持 ttf woff文件 其他不支持
    :param url:
    :param s:
    :return:
    """
    if url.endswith(".ttf"):
        return dll.NewOcr(url.encode("utf-8"), s.encode("utf-8"))
    return dll.NewOcr(woff2tff(url).encode("utf-8"), s.encode("utf-8"))


if __name__ == '__main__':
    url = "https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/85226b1a.woff"
    s = "丙232"
    anti(url, s)

