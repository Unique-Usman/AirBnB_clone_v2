#!/usr/bin/python3
"""This module defines the DBStorage class for the HBNB project."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv


class DBStorage:
    """This class manages storage of the HBNB project in a MySQL database."""
    __engine = None
    __session = None
    user = ""
    pwd = ""
    host = ""
    db = ""

    def __init__(self):
        """Creates the engine and the session"""
        self.user = getenv('HBNB_MYSQL_USER')
        self.pwd = getenv('HBNB_MYSQL_PWD')
        self.host = getenv('HBNB_MYSQL_HOST', default='localhost')
        self.db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:\
                                      {}@{}:3306/{}'.
                                      format(self.user, self.pwd,
                                             self.host, self.db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Queries the current database session."""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        classes = [State, City, User, Place, Amenity, Review]

        if cls and cls not in classes:
            return {}

        if cls is not None:
            query_result = self.__session.query(cls).all()
        else:
            query_result = []
            for c in classes:
                query_result.extend(self.__session.query(c).all())

        print("Query Result:", query_result)

        objects = {}
        for obj in query_result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        and the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        call remove() method on the private
        session attribute (self.__session)
        """
        self.__session.remove()
