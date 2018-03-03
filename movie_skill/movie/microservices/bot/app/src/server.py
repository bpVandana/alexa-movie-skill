import os
import json
from flask import Flask
from flask_ask import Ask, statement, question ,session
from flask_ask import request as flask_ask_request
from flask import render_template, make_response, request, url_for, jsonify
import requests
import unidecode


app = Flask(__name__)
ask = Ask(app, '/movie')
url = "https://data.incipiently69.hasura-app.io/v1/query" 



def getRandom():

	url = "https://data.incipiently69.hasura-app.io/v1/query" 
	headers = {
		"Content-Type": "application/json",
		"Authorization": "Bearer c31a5972aa39f1352c6bd7c6c7c5a406000825248cb2d8db",
        "X-Hasura-User-Id": "1",
        "X-Hasura-Role": "admin"
	}
	body = {
	    "type": "run_sql",
	    "args": {
	        "sql": "SELECT original_title FROM collect ORDER BY RANDOM() limit 1;"
	    }
	}
	response = requests.request("POST", url, data=json.dumps(body), headers=headers)
	respObj = response.json()
	ans = respObj["result"][1][0]
	
	query_payload = {
        'timestamp': str(flask_ask_request.timestamp),
        'query_text': respObj["result"][1][0] ,
        'answer':  ans ,
        'response_time': response.elapsed.total_seconds(),
        
    }
	headers = {
		"Content-Type": "application/json"
	}
	logs_url = "https://data.incipiently69.hasura-app.io/logs"
	requests.put(logs_url, data=json.dumps(query_payload), headers=headers) 
	#update_log()
    
	return (respObj["result"][1][0])


@app.route('/')
@app.route('/index')
def home():
    return 'Alexa Movie is running now.'


@ask.launch
def start():
    welcome = 'Welcome to movie data base... Ask me anything about movie...'
    return question(welcome)

@ask.intent("suggestMovie")
def getRandomMovie():
    movie = getRandom()
    response = movie + '......is a nice movie ......... '
    body = {
        'type': 'insert',
        'args': {
            'table': 'logs',
            'objects': [
                {
                    'answer':response,
                    'query_text':'suggestMovie'

                    
                    
                }
            ]
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer c31a5972aa39f1352c6bd7c6c7c5a406000825248cb2d8db"
    }
    requests.post(url, data=json.dumps(body), headers=headers)
	#session.attributes['response_time'] = response.elapsed.total_seconds()
	
    return statement(response)

@ask.intent("YesIntent")
def getRandomMovie():
    movie = getRandom()
    response = movie + '......is a nice movie '
    body = {
        'type': 'insert',
        'args': {
            'table': 'logs',
            'objects': [
                {
                    'answer':response,
                    'query_text':'suggestMovie'
                   
                    
                    
                }
            ]
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer c31a5972aa39f1352c6bd7c6c7c5a406000825248cb2d8db"
    }
    requests.post(url, data=json.dumps(body), headers=headers)
	
    
    return statement(response)

@ask.intent("NoIntent")
def noIntent():
    byeText = 'Lol... OK... Bye'
    body = {
        'type': 'insert',
        'args': {
            'table': 'logs',
            'objects': [
                {
                    'answer':byeText,
                    'query_text':'No more suggestions'
                   
                    
                    
                }
            ]
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer c31a5972aa39f1352c6bd7c6c7c5a406000825248cb2d8db"
    }
    requests.post(url, data=json.dumps(body), headers=headers)
	
    
    return statement(byeText)






