'''
closures - functional programming styple
Other than that, for a context, I would prefer a class itself.
from Prathik Pai to All Participants:
This has lot of bookkeeping like returning the intended functions etc

Inner functions while its reference/address are returned, it also returns context with entire scope

'''
def connection(hostname, port, db_name):
    url_string = f"postgres://{hostname}:{port}/{db_name}"
    connection_status = False
    def connect():
        nonlocal connection_status
        if connection_status:
            print("Connection already established")
        else:
            connection_status = True
            print(f"Connection established to {url_string}")
    def disconnect():
        nonlocal connection_status
        if connection_status:
            print(f"Disconnecting to {url_string}")
            connection_status = False
        else:
            print(f"No Connections Active")
    def status():
        if connection_status:
            print(f"Connected to {url_string}")
        else:
            print("No Connection Active")
    return connect, disconnect, status

db_connect, db_disconnect, db_status = connection("localhost", 5432, "test")
db_connect()
db_connect()
db_disconnect()
db_disconnect()
db_status()
db_connect()
db_status()
db_status()