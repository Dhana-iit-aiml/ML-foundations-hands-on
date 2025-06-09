#

'''Closures - help stores the function context forever if inner function address is return outside the calling func

say below example : url, host, port are in scope of connection, however inner func - connect() reference/address returned
outside connection() func...
none of the variales - url,port,url dies until the address of inner fnc - connect() is explicitly destroyed like del connect()

'''


def connection(hostname, port, dbname):
    url_string = f'postgres://{hostname}:{port}/{dbname}'

    def connect():
        print(url_string)
    #returning just address
    return connect

db_connect = connection('localhost','5432', 'test')
db_connect()

db_connect1 = connection('localhost','5432', 'test')
db_connect1()
