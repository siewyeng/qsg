#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
usage:
cat about.txt | python soinput.py
'''

import sys

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        lines[i] = lines[i].replace('_cat_n_1_rel', '_cat_n_rel')
        lines[i] = lines[i].replace('_dog_n_1_rel', '_dog_n_rel')
        lines[i] = lines[i].replace('_exist_q_rel', 'exist_q_rel')
    #print lines
    return lines

def main():
    lines = read_in()
    for l in lines:
        print(l)

if __name__ == '__main__':
    main()
