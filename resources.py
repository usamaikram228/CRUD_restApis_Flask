from flask import request, Response, jsonify
from flask_restful import Resource
from model import Product

class ProductsApi(Resource):
    def get(self):
        #print("**************")
        data = Product.objects().to_json()
        #print(data)
        return Response(data, mimetype="application/json", status=200)
    def post(self):
        data = request.get_json()
        #pro = Product(**data).save()
        pro = Product(name=data["name"],description=data["description"],price=data["price"]).save()
        id=Product.id
        return {'id':str(id)},200

class ProductApi(Resource):
    def get(self,id):
        veh=Product.objects.get(id=id).to_json()
        return Response(veh,mimetype="application/json",status=200)
    def put(self,id):
        body=request.get_json()
        Product.objects.get(id=id).update(**body)
        return {'id':str(id)},200
    def delete(self,id):
        Product.objects.get(id=id).delete()
        #return {'id':str(pro.id)},200 
class ProductApiByName(Resource):
    def get(self,name):
        veh=Product.objects.get(name=name).to_json()
        return Response(veh,mimetype="application/json",status=200)
    def put(self,name):
        body=request.get_json()
        Product.objects.get(name=name).update(**body)
        return {'id':str(id)},200
    def delete(self,name):
        Product.objects.get(name=name).delete()        

class ProductApiByDes(Resource):
    def get(self,description):
        veh=Product.objects.get(description= description).to_json()
        return Response(veh,mimetype="application/json",status=200)
    def put(self,description):
        body=request.get_json()
        Product.objects.get(description= description).update(**body)
        return {'id':str(id)},200
    def delete(self,description):
        Product.objects.get(description= description).delete()         