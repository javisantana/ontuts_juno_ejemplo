from juno import *

init({'db_location': 'amigos.db'})

Amigos = model('Amigos', nombre='string')

@route('/:nombre/')
def hola(web, nombre):
  #salvamos el nuevo amigo
  Amigos(nombre=nombre).save() # similar a un insert ...
  amigos = find(Amigos).all() # similar a un select * from Amigos
  template('index.html', nombre=nombre, amigos=amigos)


run()

