from enum import Enum

CREATE = 'create'
DELETE = 'delete'
DETAIL = 'detail'
LIST = 'list'
UPDATE = 'update'

READ = 'read'
WRITE = 'write'

FILE_KEY_NAME = 'file'

META_KEY_FORMAT = '_format'
META_KEY_LIMIT = '_limit'
META_KEY_OFFSET = '_offset'

COOKIE_PREFIX = '__COOKIE__'


class OperationType(str, Enum):
    CREATE = 'create'
    DELETE = 'delete'
    DETAIL = 'detail'
    LIST = 'list'
    UPDATE = 'update'
