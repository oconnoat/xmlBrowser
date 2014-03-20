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
from lxml import etree

import xmlBrowser

@step('I have the path (.+)')
def have_the_path(step, path):
    """have_the_path: get the directory"""
    world.path = str(path)

@step('I open it and count the files')
def open_and_count(step):
    world.number = len(xmlBrowser.open_dir(world.path))

@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert expected == world.number, "expecteed %d, got %d" % (expected, world.number)

@step('I see the text (.*)')
def check_text(step, expected):
    expected = str(expected)
    assert expected == world.text, '\nexp %s\ngot %s' % (expected, world.text)

#filecount steps

@step(u'When I open it and count the valid xml files')
def when_i_open_it_and_count_the_valid_xml_files(step):
    world.number = len(xmlBrowser.load_xml_dir(xmlBrowser.open_dir(world.path)))

@step(u'When I open it and get the list of namespaces from all the trees')
def when_i_open_it_and_get_the_list_of_namespaces_from_all_the_trees(step):
    world.text = xmlBrowser.get_namespace_list(xmlBrowser.load_xml_dir(xmlBrowser.open_dir(world.path)))


#taganalysis steps

@step(u'When I open it and count the tags in the files')
def when_i_open_it_and_count_the_tags_in_the_files(step):
    world.number = len(xmlBrowser.get_tag_list(xmlBrowser.load_xml_dir(xmlBrowser.open_dir(world.path))))

#fileops steps

@step(u'I have the path \'([^\']*)\' and the url \'([^\']*)\'')
def i_have_the_path_group1_and_the_url_group2(step, group1, group2):
    world.path = str(group1)
    world.urls = [str(group2)]


@step(u'I run the xpath query \'([^\']*)\'')
def i_open_it_and_run_the_xpath_query_group1(step, group1):
    world.text = str(etree.tostring(xmlBrowser.xpath_query(xmlBrowser.load_xml_dir(xmlBrowser.open_dir(world.path)), world.urls, group1)[world.urls[0]][0]))

