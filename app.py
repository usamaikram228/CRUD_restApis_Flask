from flask import Flask,jsonify,request,render_template
from flask_restful import Api,Resource
from db import db
import resources
import  routes

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/student'
}
api=Api(app)
db.init_app(app)
routes.initialize_routes(api)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/webpage')
def webPage():
    return render_template("webPage.html")  
@app.route('/update')
def update():
    return render_template("update.html")      
@app.route('/delete')
def delete():
    return render_template("delete.html")    
@app.route('/searchProduct')
def searchProduct():
    return render_template("searchProduct.html")
# @app.route('/addProduct')
# def add():
#     return render_template("addProduct.html")

# @app.route('/showProducts')
# def show():
#     return render_template("showProduct.html")
if __name__ == '__main__':
    app.run()
