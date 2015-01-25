#!/usr/bin/python2.7

import os


def run(**args):
    print "[*] In dirlister mod"
    files = os.listdir(".")

    return str(files)
