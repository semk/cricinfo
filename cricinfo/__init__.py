#! /usr/bin/env python
#
# Python library for accessing information from http://cricinfo.com 
#    (Live scores and updates)
#
# @author: Sreejith K
# Created On: 24 Nov 2010

import urllib
from RSS import *

# default live feed
_live_scores_xml = 'http://espncricinfo.com/rss/livescores.xml'

class Innings(object):
    """
    Scorecard for an innings
    """
    pass

class Match(object):
    """
    Contains a match information and iterator gets the 
    per-innings scorecard
    """

    def __init__(self, title, description, link, guid):
        self.title = title
        self.description = description
        self.link = link
        self.guid = guid
        self._innings = 0

    def get_scorecard():
        pass

    def rewind(self):
        self._innings = 0
        self.get_scorecard()

    def next(self):
        pass

    def __iter__(self):
        return self

class CricInfo(object):
    """
    Cricinfo iterator: iterate though the instances for current live 
    cricket scores. On each iteration optionally one can get the match's
    full scorecard and innings information.
    """
    
    def __init__(self, live_scores_xml = _live_scores_xml):
        self.live_scores_xml = live_scores_xml
        self._matches = []
        self.rewind()

    def set_url(self, url):
        """
        Update the scorecard feed url for dynamic updation
        """
        self.live_scores_xml = url
    
    def get_url(self):
        """
        Get the current active live feed
        """
        return self.live_scores_xml

    def update_live_scores(self):
        """
        Update the scores now
        """
        live_channel = self.parse_xml()

    def is_match_url(self, url):
        """
        Checks whether the url is a valid url for a live match
        """
        return isinstance(url, basestring) and \
                url.startswith("http://www.cricinfo.com/ci/engine/match/")

    def parse_xml(self):
        """
        Parse the current live feed and get the live scores
        """
        # parse the xml and populate the dictionary with needed information.
        live_channel = TrackingChannel()
        live_channel.parse(self.get_url())

        for match_url, matches in live_channel.iteritems():
            if self.is_match_url(match_url):
                for match in matches:
                    kwargs = {}
                    for unused, key in match:
                        kwargs[key] = match[(unused, key)]
                    m = Match(**kwargs)
                    self._matches.append(m)

        self._match_count = len(self._matches)
        return live_channel

    def rewind(self):
        """
        Reset the match counter
        """
        self._match_index = 0
        self.update_live_scores()

    def next(self):
        """
        Iterate for the next match. Stop if last mach info
        """
        if self._match_index >= self._match_count:
            raise StopIteration
        match = self._matches[self._match_index]
        self._match_index += 1
        return match

    def __iter__(self):
        """
        A smart and ineractive Python iterator for live cricket scores
        """
        return self


if __name__ == '__main__':
    # instantiate
    matches = CricInfo()
    # iterate thouh current live matches
    for match in matches:
        print '\t\t %s' % match.title
        print '\t\t %s' % match.description
        print '\t\t %s' % match.link
        print '\t\t %s' % match.guid
        
