
import struct
import zlib
import os
from hashlib import md5
from io import BytesIO


import requests


base_dir = os.path.dirname(__file__)


def convert_streams(infile, outfile):
    WOFFHeader = {'signature': struct.unpack(">I", infile.read(4))[0],
                  'flavor': struct.unpack(">I", infile.read(4))[0],
                  'length': struct.unpack(">I", infile.read(4))[0],
                  'numTables': struct.unpack(">H", infile.read(2))[0],
                  'reserved': struct.unpack(">H", infile.read(2))[0],
                  'totalSfntSize': struct.unpack(">I", infile.read(4))[0],
                  'majorVersion': struct.unpack(">H", infile.read(2))[0],
                  'minorVersion': struct.unpack(">H", infile.read(2))[0],
                  'metaOffset': struct.unpack(">I", infile.read(4))[0],
                  'metaLength': struct.unpack(">I", infile.read(4))[0],
                  'metaOrigLength': struct.unpack(">I", infile.read(4))[0],
                  'privOffset': struct.unpack(">I", infile.read(4))[0],
                  'privLength': struct.unpack(">I", infile.read(4))[0]}

    outfile.write(struct.pack(">I", WOFFHeader['flavor']))
    outfile.write(struct.pack(">H", WOFFHeader['numTables']))
    maximum = list(filter(lambda x: x[1] <= WOFFHeader['numTables'], [(n, 2**n) for n in range(64)]))[-1]
    searchRange = maximum[1] * 16
    outfile.write(struct.pack(">H", searchRange))
    entrySelector = maximum[0]
    outfile.write(struct.pack(">H", entrySelector))
    rangeShift = WOFFHeader['numTables'] * 16 -  searchRange
    outfile.write(struct.pack(">H", rangeShift))

    offset = outfile.tell()

    TableDirectoryEntries = []
    for i in range(0, WOFFHeader['numTables']):
        TableDirectoryEntries.append({'tag': struct.unpack(">I", infile.read(4))[0],
                               'offset': struct.unpack(">I", infile.read(4))[0],
                               'compLength': struct.unpack(">I", infile.read(4))[0],
                               'origLength': struct.unpack(">I", infile.read(4))[0],
                               'origChecksum': struct.unpack(">I", infile.read(4))[0]})
        offset += 4*4

    for TableDirectoryEntry in TableDirectoryEntries:
        outfile.write(struct.pack(">I", TableDirectoryEntry['tag']))
        outfile.write(struct.pack(">I", TableDirectoryEntry['origChecksum']))
        outfile.write(struct.pack(">I", offset))
        outfile.write(struct.pack(">I", TableDirectoryEntry['origLength']))
        TableDirectoryEntry['outOffset'] = offset
        offset += TableDirectoryEntry['origLength']
        if (offset % 4) != 0:
            offset += 4 - (offset % 4)

    for TableDirectoryEntry in TableDirectoryEntries:
        infile.seek(TableDirectoryEntry['offset'])
        compressedData = infile.read(TableDirectoryEntry['compLength'])
        if TableDirectoryEntry['compLength'] != TableDirectoryEntry['origLength']:
            uncompressedData = zlib.decompress(compressedData)
        else:
            uncompressedData = compressedData
        outfile.seek(TableDirectoryEntry['outOffset'])
        outfile.write(uncompressedData)
        offset = TableDirectoryEntry['outOffset'] + TableDirectoryEntry['origLength'];
        padding = 0
        if (offset % 4) != 0:
            padding = 4 - (offset % 4)
        outfile.write(bytearray(padding))


def convert(infilename, outfilename):
    with open(infilename , mode='rb') as infile:
        with open(outfilename, mode='wb') as outfile:
            convert_streams(infile, outfile)


def woff2tff(url):
    file_md = os.path.join(base_dir, "tmp", md5(url.encode("utf-8")).hexdigest() + ".ttf")
    if os.path.exists(file_md):
        return file_md
    res = requests.get(url)
    infile = BytesIO(res.content)
    with open(file_md, "wb") as outfile:
        convert_streams(infile, outfile)
    infile.close()
    return file_md