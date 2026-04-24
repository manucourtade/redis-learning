import redis

# Conectar nuestra bd
redis_cliente = redis.Redis(host="localhost", port=6379, db=0, password="password")

# Comprobar conexion
try:
    redis_cliente.ping()
    print("El servidor de redis esta disponible")
except redis.exceptions.ConnectionError:
    print("El servidor de redis NO esta disponible")

# Imprimir valores
redis_cliente.set("id_nombre", "manucourtade")
valor = redis_cliente.get("id_nombre")
print(valor.decode("utf-8"))

informacion = {
    "nombre": "Josema Traverso",
    "fecha_de_nacimiento": "12/11/1983",
    "nacionalidad": "Argentina",
}

# Recuperar diccionarios
redis_cliente.hset("clave_informacion", mapping=informacion)
data = redis_cliente.hgetall("clave_informacion")
for clave, valor in data.items():
    print(f"{clave.decode('utf-8')}: {valor.decode('utf-8')}")

# Vaciar Base de datos
redis_cliente.flushdb()
