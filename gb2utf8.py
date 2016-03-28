#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 13:55:05 2016-03-28

@author: heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""


import sys
import codecs

# Convert GB2312 file to UTF-8


def encode_utf8(src_file, out_file):
    # Open and encode the origianl content
    file_source = codecs.open(src_file, mode='r', encoding="gb2312")
    file_content = file_source.read()
    file_source.close()

    # Write the UTF8 file with encoded content
    file_target = codecs.open(out_file, mode='w', encoding='utf-8')
    file_target.write(file_content)
    file_target.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Not enough parameters."
        print "Usage: python gb2utf8.py src_file [out_file]"
        print "       out_file: if out_file has not been set, the output file"
        print "                 will be save as src_file.utf8"
        sys.exit(0)
    src_file = sys.argv[1]
    if len(sys.argv) == 2:
        out_file = sys.argv[1] + ".utf8"
    else:
        out_file = sys.argv[2]

    encode_utf8(src_file, out_file)
    print "UTF8 enconding done for:%s" % src_file
