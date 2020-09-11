#!/usr/bin/python

import sys

if len(sys.argv) == 4:
    inputFile = sys.argv[1]
    stringVal = sys.argv[2]
    outputFile = sys.argv[3]
    counter = 0;
    with open(inputFile) as fp:
        counter += 1
        for line in fp:
            if stringVal in line:
                with open(outputFile + '\n', "a") as of:
                    of.write(line)
else:
    print("The input format is as following:\ninputFile stringTosearch outputFile");
