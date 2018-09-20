# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'构建和运营一门edX课程'

tags.add('Partners')
set_audience(PARTNER, COURSE_TEAMS)

product = 'Partners'


def setup(app):
    app.add_config_value('product', '', True)
