from getmethod import ClassGetMethod
from postmethod import ClassPostMethod
from putmethod import ClassPutMethod
from deletemethod import ClassDeleteMethod

def selection_method():
    var_input = input("Method please: ")
    if var_input == "GET":
        var_key = input("key please:")
        obj_get_method = ClassGetMethod(var_key)
        obj_get_method.get_method()
    elif var_input == "POST":
        var_route = input("route please:")
        var_origin = input("origin please:")
        var_mntby = input("mntby please:")
        var_source = input("source please:")
        var_descr = input("descr please:")
        obj_post_method = ClassPostMethod(var_route, var_origin, var_mntby, var_source, var_descr)
        obj_post_method.post_method()
    elif var_input == "PUT":
        var_route = input("route please:")
        var_origin = input("origin please:")
        var_mntby = input("mntby please:")
        var_source = input("source please:")
        var_descr = input("descr please:")
        var_key = input("key please:")
        obj_put_method = ClassPutMethod(var_route, var_origin, var_mntby, var_source, var_descr, var_key)
        obj_put_method.put_method()
    elif var_input == "DELETE":
        var_key = input("key please:")
        obj_delete_method = ClassDeleteMethod(var_key)
        obj_delete_method.delete_method()
selection_method()
