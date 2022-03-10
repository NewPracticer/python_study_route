import threading
import time
import datetime

from config import Page_URL
from config import ANALYSER
from spider import Spider

spider = Spider(Page_URL, ANALYSER)
spider.go()