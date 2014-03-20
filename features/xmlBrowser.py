#!/usr/bin/python

# -*- coding: utf-8 -*-

""" Tool for rapidly examining a large collection of xml files. """

import os
import sys
from glob import glob
from lxml import etree
# from itertools import imap

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
    """parse an xml file and if it's valid return it, otherwise return none"""
    try:
        return (filename, etree.parse(filename))
    except etree.XMLSyntaxError, e:
        return None

def load_xml_dir(dir_glob):
    """load the xml files and parse them, return a dictionary of files and their trees"""
    #would love to find a more efficient way to do this :)
    dir_trees = filter(None, map(get_tree, dir_glob))
#    dir_trees = [tree for tree in imap(get_tree, dir_glob)  if tree is not None]
    return dict(dir_trees)

def get_namespace_list(dir_trees):
    """For each tree, get the namespace statements for the root node, if any"""
    nsURIs = set([ns for url in dir_trees for ns in dir_trees[url].getroot().nsmap.values()])
    return str(nsURIs)

def get_tag_list(dir_trees):
    """For each tree, iterate and collect all the tag names TODO: Decide on whether Qname, Localname or full name"""
    assert False, 'figure out how to walk the tree!'
if __name__ == '__main__':
  get_tag_list(load_xml_dir(open_dir('/Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData')))

