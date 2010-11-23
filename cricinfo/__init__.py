#! /usr/bin/env python
#
# Python library for accessing information from http://cricinfo.com 
#    (Live scores and updates)
#
# @author: Sreejith K
# Created On: 24 Nov 2010

import urllib

live_scores_xml = 'http://espncricinfo.com/rss/livescores.xml'

class CricInfo:

    def __init__(self, live_scores_xml = live_scores_xml):
        self.live_scores_xml = live_scores_xml
        self.xml_data = None
        self.live_scores = {}

    def get_xml_data(self):
        self.xml_data = urllib.urlopen(self.live_scores_xml)

    def update_live_scores(self):
        self.get_xml_data()
        self.live_scores = self.parse_xml()

    def parse_xml(self):
        # parse the xml and populate the dictionary with needed information.
        pass
        
