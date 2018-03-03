import os
import json
from flask import Flask
from flask_ask import Ask, statement, question
from flask_ask import request as flask_ask_request
from flask import render_template, make_response, request, url_for, jsonify
import requests
import unidecode

#PRODUCTION_ENV = os.environ.get('PRODUCTION')
#CLUSTER_NAME = os.environ.get('CLUSTER_NAME')

"""if CLUSTER_NAME is None:
    print('defect94 not found. Please export environment variable CLUSTER_NAME=<name_of_your_hasura_cluster>')"""

app = Flask(__name__)
ask = Ask(app, '/movie')

# Store latest log data as dict. TODO: Update this
query_log = {
    'timestamp': None,
    'query_text': None,
    'answer': None,
    'response_time': None,
    'is_error_occured': None
}


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
	return (respObj["result"][1][0])

def getLatest():
        #This is the url to which the query is made
        url = "https://data.incipiently69.hasura-app.io/v1/query" 

        # This is the json payload for the query
        requestPayload = {
            "type": "run_sql",
            "args": {
                "sql": "select original_title from collect where release_date =(select max(release_date) from collect);"
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer a465dffb2aefe3d8cfd97a801ca6011d4de8a99764bc4cb7"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
        respObj = resp.json()
        return (respObj["result"][1][0])



#print (getLatest())

"""def get_:
    data_url = "https://data.geothermal68.hasura-app.io/v1/query"    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer c31a5972aa39f1352c6bd7c6c7c5a406000825248cb2d8db",
        "X-Hasura-User-Id": "1",
        "X-Hasura-Role": "admin"
    }
    body = {
        "type": "run_sql",
        "args": {
            "sql": "SELECT overview,tagline \
                    FROM collect \
                    WHERE original_title='{}';"
                    .format(name)
        }
    }
    response = requests.post(data_url, data=json.dumps(body), headers=headers)
    json_response = response.json()
    print(json_response) # for testing purpose
    
    is_error_occured = False
    if 'result' in json_response:
        if len(json_response['result']) > 1: # check if result is actually available
            movie = json_response['result'][1][0]
            movie = unidecode.unidecode(movie)
            answer = 'the details about movie {} is {}'.format(name,movie)
        else:
            answer = 'Sorry, I couldn\'t find any details of movie... {}'.format(name)
            is_error_occured = True
    else:
        answer = 'Sorry, I couldn\'t find any details of movie... {}'.format(name)
        is_error_occured = True
        log_payload = {
        'timestamp': str(flask_ask_request.timestamp),
        'query_text': 'Tell me about movie {}'.format(name), # Hardcoded value, TODO: update this
        'answer': answer,
        'response_time': response.elapsed.total_seconds(),
        'is_error_occured': is_error_occured
    }
    headers = {'Content-Type': 'application/json'}
    logs_url = 'https://bot.geothermal68.hasura-app.io/logs'
    requests.put(logs_url, data=json.dumps(log_payload), headers=headers) # make a PUT request to /logs to update new log value
    return statement(answer)"""





@app.route('/')
@app.route('/index')
def home():
    return 'Alexa Movie is running now.'


@ask.launch
def handle_launch():
    welcome_text = 'Welcome to movie data base... Ask me anything about movie...'
    return question(welcome_text)


@ask.intent('GetMovieIntent')
def get_movie(name):
    data_url = "https://data.incipiently69.hasura-app.io/v1/query"  
    headers = {
        "Content-Type": "application/json",
        "Authorization":  "Bearer c31a5972aa39f1352c6bd7c6c7c5a406000825248cb2d8db",
        "X-Hasura-User-Id": "1",
        "X-Hasura-Role": "admin"
    }
    body = {
        "type": "run_sql",
        "args": {
            "sql": "SELECT tagline,overview \
                    FROM collect \
                    WHERE original_name={};"
                    .format(name)
        }
    }
    response = requests.post(data_url, data=json.dumps(body), headers=headers)
    json_response = response.json()
    #print(json_response) # for testing purpose
    is_error_occured = False
    if 'result' in json_response:
        if len(json_response['result']) > 1: # check if result is actually available
            movie = json_response['result'][1][0]
            movie = unidecode.unidecode(movie)
            answer = 'the details about movie {} is {}'.format(name,movie)
        else:
            answer = 'Sorry, I couldn\'t find any details of movie... {}'.format(name)
            is_error_occured = True
    else:
        answer = 'Sorry, I couldn\'t find any details of movie... {}'.format(name)
        is_error_occured = True
        log_payload = {
        'timestamp': str(flask_ask_request.timestamp),
        'query_text': 'Tell me about movie {}'.format(name), # Hardcoded value, TODO: update this
        'answer': answer,
        'response_time': response.elapsed.total_seconds(),
        'is_error_occured': is_error_occured
    }
    headers = {'Content-Type': 'application/json'}
    logs_url = 'https://data.incipiently69.hasura-app.io/logs'
    requests.put(logs_url, data=json.dumps(log_payload), headers=headers) # make a PUT request to /logs to update new log value
    return statement(answer)


@ask.intent("GetLatestIntent")
def getLatestMovie():
    movie = getLatest()
    response = 'Latest Movie is '+movie + '...... mmmmmmm ......... Do you want more?'
    return question(response)


@ask.intent("YesIntent")
def getRandomMovie():
    movie = getRandom()
    response = movie + '...... mmmmmmm ......... Do you want more?'
    return question(response)

@ask.intent("NoIntent")
def noIntent():
    byeText = 'Lol... OK... Bye'
    return statement(byeText)


@app.route('/logs', methods=['GET', 'PUT'])
def send_log():
    '''Send logs to /logs endpoint'''
    if request.method == 'GET':
        return jsonify(query_log)
    elif request.method == 'PUT':
        for key, value in request.get_json().items():
            query_log[key] = value
        return 'Successfully updated log', 202



if __name__ == '__main__':
    app.run(debug=True)

