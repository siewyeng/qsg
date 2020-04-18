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
        lines[i] = lines[i].replace('_glass_n_1_rel', '_glass_n_rel')
        lines[i] = lines[i].replace('_thing_n_1_rel', '_thing_n_rel')
        lines[i] = lines[i].replace('_he_n_1_rel', '_he_n_rel')
        lines[i] = lines[i].replace('_she_n_1_rel', '_she_n_rel')
        lines[i] = lines[i].replace('_it_n_1_rel', '_it_n_rel')
        lines[i] = lines[i].replace('_I_n_1_rel', '_I_n_rel')
        lines[i] = lines[i].replace('_me_n_1_rel', '_I_n_rel')
        lines[i] = lines[i].replace('_him_n_1_rel', '_he_n_rel')
        lines[i] = lines[i].replace('_her_n_1_rel', '_she_n_rel')
        lines[i] = lines[i].replace('_roughly_rel', '_roughly_v_rel')
        lines[i] = lines[i].replace('_can_v_rel', '_can_v_2_rel')



    #print lines
    return lines

def main():
    lines = read_in()
    print lines

if __name__ == '__main__':
    main()
