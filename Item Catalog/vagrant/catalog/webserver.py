from flask import Flask,render_template, request, redirect, url_for, flash, jsonify


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

from flask import session as login_session
import random,string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(open('clientsecrets.json','r').read())['web']['client_id']

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)

@app.route('/login')
def showLogin():
	state = ''.join(random.choice(string.ascii_uppercase + string.digits)for x in xrange(32))
	login_session['state'] = state
	return render_template('login.html',STATE = state)
	
@app.route('/gconnect',methods = ['POST'])
def gconnect():
    # Validate state token
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
    # Obtain authorization code
	code = request.data

	try:
        # Upgrade the authorization code into a credentials object
		oauth_flow = flow_from_clientsecrets('clientsecrets.json', scope='')
		oauth_flow.redirect_uri = 'postmessage'
		credentials = oauth_flow.step2_exchange(code)
	except FlowExchangeError:
		response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

    # Check that the access token is valid.
	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'% access_token)
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
	if result.get('error') is not None:
		response = make_response(json.dumps(result.get('error')), 500)
		response.headers['Content-Type'] = 'application/json'
		return response

    # Verify that the access token is used for the intended user.
	gplus_id = credentials.id_token['sub']
	if result['user_id'] != gplus_id:
		response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

    # Verify that the access token is valid for this app.
	if result['issued_to'] != CLIENT_ID:
		response = make_response(json.dumps("Token's client ID does not match app's."), 401)
		print "Token's client ID does not match app's."
		response.headers['Content-Type'] = 'application/json'
		return response

	stored_credentials = login_session.get('credentials')
	stored_gplus_id = login_session.get('gplus_id')
	if stored_credentials is not None and gplus_id == stored_gplus_id:
		response = make_response(json.dumps('Current user is already connected.'),200)
		response.headers['Content-Type'] = 'application/json'
		return response

    # Store the access token in the session for later use.
	login_session['credentials'] = credentials
	login_session['gplus_id'] = gplus_id

    # Get user info
	userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
	params = {'access_token': credentials.access_token, 'alt': 'json'}
	answer = requests.get(userinfo_url, params=params)

	data = answer.json()

	login_session['username'] = data['name']
	login_session['picture'] = data['picture']
	login_session['email'] = data['email']

	output = ''
	output += '<h1>Welcome, '
	output += login_session['username']
	output += '!</h1>'
	output += '<img src="'
	output += login_session['picture']
	output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
	flash("you are now logged in as %s" % login_session['username'])
	print "done!"
	return output

@app.route('/')
@app.route('/category/<int:category_id>/')
def showCategories(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	items = session.query(Item).filter_by(category_id = category_id).all()
	return render_template('categories.html',category = category, items = items)	
	
@app.route('/category/<int:category_id>/new/', methods = ['GET','POST'])
def newItem(category_id):
	if request.method == 'POST':
		addItem = Item(name = request.form['name'], category_id = category_id)
		session.add(addItem)
		session.commit()
		flash("New Item created")
		return redirect(url_for('showCategories', category_id=category_id))
	else:
		return render_template('newItem.html',category_id = category_id)
	
@app.route('/category/<int:category_id>/<int:item_id>/edit/', methods = ['GET','POST'])
def editItem(category_id, item_id):
	editedItem = session.query(Item).filter_by(id = item_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedItem.name = request.form['name']
		session.add(editedItem)
		session.commit()
		flash("Item edited")
		return redirect(url_for('showCategories',category_id = category_id))
	else:
		return render_template('editItem.html',category_id = category_id, item_id = item_id, item = editedItem)
	
@app.route('/category/<int:category_id>/<int:item_id>/delete/',methods = ['GET','POST'])
def deleteItem(category_id, item_id):
	itemDelete = session.query(Item).filter_by(id = item_id).one()
	if request.method == 'POST':
		session.delete(itemDelete)
		session.commit()
		flash("Item deleted")
		return redirect(url_for('showCategories',category_id = category_id))
	else:
		return render_template('deleteItem.html', category_id = category_id, item_id = item_id, item = itemDelete)
	
@app.route('/category/<int:category_id>/item/JSON')
def categoryItemJSON(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	items = session.query(Item).filter_by(category_id = category_id).all()
	return jsonify(Item = [i.serialize for i in items])



if __name__ == '__main__':
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)