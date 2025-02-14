from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(String, primary_key=False)
    username = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    role = Column(String, primary_key=False)


class Leads(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    created_at = Column(String, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    address_city = Column(String, primary_key=False)
    address_state = Column(String, primary_key=False)
    message = Column(String, primary_key=False)
    attachments = Column(String, primary_key=False)
    source = Column(String, primary_key=False)
    status = Column(String, primary_key=False)


class Formsubmission(Base):
    __tablename__ = 'formsubmission'
    id = Column(Integer, primary_key=True)
    created_at = Column(String, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    message = Column(String, primary_key=False)
    attachment = Column(String, primary_key=False)


class AdminLogs(Base):
    __tablename__ = 'admin_logs'
    id = Column(Integer, primary_key=True)
    created_at = Column(String, primary_key=False)
    adminId = Column(String, primary_key=False)
    leadId = Column(String, primary_key=False)
    action = Column(String, primary_key=False)


