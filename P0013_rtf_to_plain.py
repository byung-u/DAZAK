#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import glob

from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter


def rtf_to_plain_text(file_name):
    print file_name
    out_file_name = './PlainText/%s.txt' % (file_name[:-4])
    fw = open(out_file_name, 'w')

    doc = Rtf15Reader.read(open(file_name, "r"))

    res = PlaintextWriter.write(doc).getvalue()
    fw.write(res)
    fw.close()


if __name__ == '__main__':
    entries = glob.glob('./*.rtf')
    for entry in entries:
        rtf_to_plain_text(entry[2:])

sys.exit(0)
