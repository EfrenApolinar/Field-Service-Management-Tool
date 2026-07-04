from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import datetime
import enum

class JobStatus(enum.Enum):
    estimate = "estimate"
    ongoing = "ongoing"
    approved="approved"
    invoiced = "invoiced"
    paid = "paid"

class Client(Base):
    __tablename__= "clients"
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    address = Column(String)
    created_at = Column(DateTime, default = datetime.datetime.now(datetime.timezone.utc))

    jobs = relationship("Job", back_populates="client")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key =True, index = True)
    title = Column(String, Nullable = False)
    description = Column(String)
    Status = Column(Enum(JobStatus), default = JobStatus.estimate)
    total = Column(Float, default = 0.0)
    created_at  = Column(DateTime, datetime.datetime.now(datetime.timezone.utc))
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", back_populates="jobs")