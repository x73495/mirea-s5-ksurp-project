from app.misc.node import Node

_DEFAULT_NODE_PORT = 5000
LIST_OF_NODES = (
    Node('172.123.123.2', _DEFAULT_NODE_PORT),
    Node('172.123.123.3', _DEFAULT_NODE_PORT),
    Node('172.123.123.4', _DEFAULT_NODE_PORT),
    Node('172.123.123.5', _DEFAULT_NODE_PORT),
    Node('172.123.123.6', _DEFAULT_NODE_PORT)
)

_DEFAULT_DB_USER = 'root'
_DEFAULT_DB_PASSWORD = 'p'
_DEFAULT_DB_NAME = 'ksurp'
_DEFAULT_DB_PORT = 3306

DB_NODES_USER = _DEFAULT_DB_USER
DB_NODES_PASSWORD = _DEFAULT_DB_PASSWORD
DB_NODES_NAME = _DEFAULT_DB_NAME
DB_NODES_HOST = '172.222.222.2'
DB_NODES_PORT = _DEFAULT_DB_PORT

DB_SERVICES_USER = _DEFAULT_DB_USER
DB_SERVICES_PASSWORD = _DEFAULT_DB_PASSWORD
DB_SERVICES_NAME = _DEFAULT_DB_NAME
DB_SERVICES_HOST = '172.111.111.2'
DB_SERVICES_PORT = _DEFAULT_DB_PORT
