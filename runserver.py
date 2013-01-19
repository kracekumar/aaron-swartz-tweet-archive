#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from archive import app
from archive.models import db
db.create_all()
if app.config['ENVIRONMENT'] == 'production':
    app.run('0.0.0.0', debug=False, port=app.config['PORT'])
app.run('0.0.0.0', debug=True, port=app.config['PORT']) # Dev env
