from flask import Flask, render_template, request, escape
from vsearch import search4letters

 from DBcm import UseDatabase

 app = Flask(__name__)

 app.config['dbconfig'] = {'host': '127.0.0.1',
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }

 def log_request(req: 'flask_request', res: str) -> None:
     with UseDatabase(app.config['dbconfig']) as cursor:
         _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
         cursor.execute(_SQL, (req.form['phrase'],
                               req.form['letters'],
                               req.remote_addr,
                               req.user_agent.browser,
                               res, ))
