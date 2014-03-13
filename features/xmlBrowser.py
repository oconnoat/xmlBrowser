#!/usr/bin/python

# -*- coding: utf-8 -*-

""" Tool for rapidly examining a large collection of xml files. """

import os
import sys
from glob import glob
from lxml import etree


__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2014, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"


directory_trees = {}

def open_dir(path):
    assert os.path.isdir(path), 'Invalid Path or Directory not Found'
    dir_glob = glob(os.path.join(path,'*.xml'))
    return dir_glob


def get_tree(filename):
    try:
        return (filename, etree.parse(filename))
    except etree.XMLSyntaxError, e:
        return None

def load_xml_dir(path):
    """docstring for load_xml_dir"""
    dir_glob = glob(os.path.join(path,'*.xml'))
    dir_trees = filter(None, map(get_tree, dir_glob))
    print "%d trees" % len(dir_trees)
    return dir_trees

if __name__ == '__main__':
    pass
