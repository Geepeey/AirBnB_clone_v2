from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.orm import Session
from models.base_model import BaseModel, Base
from os import getenv


class Amenity(BaseModel, Base):
    """Represents an Amenity for a HBNB project."""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")


class PlaceAmenity(Base):
    """Represents a relationship between a Place and an Amenity."""
    __tablename__ = "place_amenity"
    place_id = Column(String(60), ForeignKey("places.id"), primary_key=True, nullable=False)
    amenity_id = Column(String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)


class Place(BaseModel, Base):
    """Represents a Place for a HBNB project."""
    __tablename__ = "places"
    ...
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    ...
    

class DBStorage:
    """Represents a database storage engine for a HBNB project."""
    __engine = None
    __session = None
    
    def __init__(self):
        """Creates a new instance of the DBStorage class."""
        ...
        self.__create_tables()
        ...
    
    def __create_tables(self):
        """Creates the necessary tables in the database."""
        Base.metadata.create_all(self.__engine, extend_existing=True)
    
    def all(self, cls=None):
        """Query on the current database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        objs = {}
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
        else:
            classes = [cls]
        for c in classes:
            for obj in self.__session.query(c).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        return objs
    
    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database and initialize a new session."""
        session_factory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.remove()

