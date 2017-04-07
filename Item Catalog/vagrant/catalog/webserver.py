from flask import Flask,render_template, request, redirect, url_for, flash, jsonify


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)

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
