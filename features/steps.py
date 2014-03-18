#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
File: steps.py
Author: Alexander O'Connor <Alex.OConnor@scss.tcd.ie>
Email: Alex.OConnor@scss.tcd.ie
Github: http://www.github.com/oconnoat
Description: The stepfile for nosing around my xmlBrowser
"""

import os, sys

from lettuce import *

import xmlBrowser

@step('I have the path (.+)')
def have_the_path(step, path):
    """have_the_path: get the directory"""
    world.path = str(path)

@step('I open it and count the files')
def open_and_count(step):
    world.number = len(xmlBrowser.open_dir(world.path))

@step(u'When I open it and count the valid xml files')
def when_i_open_it_and_count_the_valid_xml_files(step):
    world.number = len(xmlBrowser.load_xml_dir(xmlBrowser.open_dir(world.path)))

@step(u'When I open it and get the list of namespaces from all the trees')
def when_i_open_it_and_get_the_list_of_namespaces_from_all_the_trees(step):
    world.text = 'test'

@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert expected == world.number, "got %d" % world.number

@step('I see the text \'([^\']*)\'')
def check_text(step, expected):
    expected = unicode(expected)
    assert expected == world.text, u'got %s' % world.text
