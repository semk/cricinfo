# Cricinfo

ESPNcricinfo is the largest cricket-related website. It includes news and articles, live scorecards, and a comprehensive and queriable database of historical matches and players from the 18th century to the present.

This Python libary provides an api for accessing information from CricInfo like live scores, news updates and player profiles.

## Usage

    # instantiate
    matches = CricInfo()
    # iterate though matches
    for match in matches:
        print match.title
        print match.description
        print match.link
        print match.guid

Simple as that !
