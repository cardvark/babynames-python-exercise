#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import urllib

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    # call 'htmlText' function to extract raw text from html file.
    htmlSource = htmlText(filename)

    # simple regex to find year; grouped for ease of extraction.
    tempMatchYear = re.search(r'(Popularity\sin\s)(\d*)', htmlSource)
    sourceYear = tempMatchYear.group(2)


    totalList = findList(r'(<tr align="right"><td>)(\d*)(</td><td>)(\w*)(</td><td>)(\w*)', htmlSource)
    outputList = outputListMaker(totalList, sourceYear)
    outputText = '\n'.join(outputList) + '\n'
    return outputText


def outputListMaker(totalList, sourceYear):
    maleList = [x[1] + ' ' + x[0] for x in totalList]
    femList = [x[2] + ' ' + x[0] for x in totalList]
    combList = maleList + femList
    sortedCombList = sorted(combList)
    sortedCombList.insert(0, sourceYear)
    return sortedCombList


def htmlText(filename):
    # calls urllib library to open the html file by name.
    tempDoc = urllib.urlopen(filename)
    htmlSource = tempDoc.read()
    tempDoc.close()
    return htmlSource


def findList(searchStr, htmlSource):
    tempMatchList = re.findall(searchStr, htmlSource)
    newList = map(lambda listItem: [listItem[1], listItem[3], listItem[5]], tempMatchList)
    return newList


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    summary = False

    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    if summary:
        # creates summary files if requested by user input.
        for arg in args:
            print 'opening file ' + arg
            outputFile = open(arg + '.summary.txt', 'w')
            outputFile.write(extract_names(arg))
            outputFile.close()
    else:
        # prints summary for each requested file.
        for arg in args:
            print extract_names(arg)


if __name__ == '__main__':
    main()
