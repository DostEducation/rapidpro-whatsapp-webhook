from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .webhook_transaction_log import *
