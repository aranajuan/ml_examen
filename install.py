import os
import webapp2
import MySQLdb

from system import System

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(
                unix_socket='/cloudsql/mltest-planets:mltest',
                user='root')
        else:
            db = MySQLdb.connect(host='localhost', user='root',passwd='juan314')
            
        cursor = db.cursor()
        cursor.execute(' DROP TABLE IF EXISTS `mltest`.`data`')
        cursor.execute('CREATE TABLE `mltest`.`data` (`day` INT NOT NULL,`weather` VARCHAR(45) NOT NULL,PRIMARY KEY (`day`));')

        
        s = System()
        
        #ultimo estado
        lastS = -4
        
        #cantidad invalidos, sequias,buen clima, lluvias
        cw = [0, 0, 0, 0];
        
        #pico lluvia
        pll = 0
        pllD = 0
        
        ctest=0
        
        for i in range(10*365):
            cursor = db.cursor()
            weather = s.setDay(i)
            if( weather > 0 ):
                #lluvia
                weatherTXT = 'lluvia'
                if( weather > pll):
                    pll = weather
                    pllD=i
                weather = 0
            elif(weather == -1):
                weatherTXT = 'buen clima'
            elif(weather == -2):
                weatherTXT = 'sequia'
            else:
                weatherTXT = 'invalido'
            if( weather != lastS):
                lastS = weather
                cw[weather+3] += 1
            cursor.execute('INSERT INTO `mltest`.`data` (`day`,`weather`) values (%s ,%s);', (i, weatherTXT))
            cursor.close()
        self.response.write('Sequias : '+str(cw[1]) + '| Buen Clima: '
        +str(cw[2]) + '| Lluvias: '+str(cw[3]) + '| Dia pico lluvia: '
        +str(pllD)+'| Invalidos: '+str(cw[0]))
        db.commit()
        db.close()
app = webapp2.WSGIApplication([
    ('/install', MainHandler)
], debug=False)
