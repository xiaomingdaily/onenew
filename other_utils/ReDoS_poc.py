#!/usr/bin/env python
# coding: utf-8

import re
import time

def exp(target_str):
    """
    """
    s1 = time.time()
    flaw_regex = re.compile('(/.*)*')
    print(flaw_regex.match(target_str))
    s2 = time.time()
    print("Consuming time: %.4f" % (s2-s1))


if __name__ == '__main__':
    str_list = (
        'axaxaxa!',           # 2^16
        'axaxaxaaaaaaaaaaaaaaaaaaaaa!',         # 2^18  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!',         # 2^18
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!',         # 2^18
    )
    for evil_str in str_list:
        print('Current: %s' % evil_str)
        exp(evil_str)
        print('--'*40)