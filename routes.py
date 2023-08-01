from resources import ProductsApi ,ProductApi,ProductApiByName,ProductApiByDes

def initialize_routes(api):
    api.add_resource(ProductsApi, '/api/Products')
    api.add_resource(ProductApi, "/api/Productsid/<id>")
    api.add_resource(ProductApiByName, "/api/Productsname/<name>")
    api.add_resource(ProductApiByDes, "/api/Productsdes/<description>")
