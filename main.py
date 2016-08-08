#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import MySQLdb
import json
from collections import OrderedDict

class MainHandler(webapp2.RequestHandler):
    def get(self):
        dia = self.request.get('dia')
        self.response.headers['Content-Type'] = 'application/json'   
        if(dia.isnumeric() == 0):
            self.response.out.write(json.dumps({'error':'El parametro dia debe ser numerico'}))
            return
        dia = int(dia)
        if(dia < 0):
            self.response.out.write(json.dumps({'error':'El parametro dia debe ser mayor o igual a 0'}))
            return
        if(dia > 3649):
            self.response.out.write(json.dumps({'error':'El parametro dia debe ser menor o igual a 3649'}))
            return
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(
                unix_socket='/cloudsql/mltest-planets:mltest',
                user='root')
        else:
            db = MySQLdb.connect(host='localhost', user='root',passwd='juan314')

        cursor = db.cursor()
        cursor.execute('select * from `mltest`.`data` where `day`  = %s ',(dia, ))
        

        for r in cursor.fetchall():
            obj =OrderedDict([
              ( "dia", r[0]),  ("clima",  r[1])
            ])
            self.response.out.write(json.dumps(obj))

app = webapp2.WSGIApplication([
    ('/clima', MainHandler)
], debug=False)
