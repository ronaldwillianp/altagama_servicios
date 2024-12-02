# @service.jsonrpc
# def getTasks():
#     todos = db(db.todo).select()
#     return [(todo.task, todo.id) for todo in todos]

@request.restful()
def v1():
    def GET(*args,**vars):
        import gluon.contrib.simplejson as gsj
        response.view = 'generic.json'
        servicios = db(db.contrato_cliente.id>0).select(
            db.contrato_cliente.id,
            db.contrato_cliente.numero,
            db.contrato_cliente.anho,
            db.contrato_cliente.empresa,
        ).as_list()
        return gsj.dumps(servicios, ensure_ascii=False)
    return locals()