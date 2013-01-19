#! -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

import archive.views

app.config.from_pyfile('../settings.py')
