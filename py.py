import BeautifulSoup
import dateutil
import base64
import chardet
import codecs
import collections
import copy
import csv
import datetime
import encodings
import feedparser
import getopt
import glob
import gzip
import html2text
import htmlentitydefs
import itertools
import mailbox
import md5
import mimetypes
import operator
import os
import pytz
import quopri
import random
import re
import sets
import socket
import string
import StringIO
import sys
import textwrap
import time
import unescape
import unicodedata
import urllib
import urllib2
import urlparse
import xml
import zlib
from os import path
from xml.dom import minidom

from google.appengine import api

import base

class Main(base.RequestHandler):

    def get(self, *args):
        command = args[1] or ""
        command = urllib.unquote(command)
        try:
            try:
                self.ok(str(eval(command)))
            except SyntaxError:
                output = StringIO.StringIO()
                sys.stdout = output
                sys.stderr = output
                exec(command)
                output.seek(0)
                self.ok(output.readline())
        except Exception, error:
            return self.ok("error: " + str(error))