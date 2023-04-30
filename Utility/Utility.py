from sqlalchemy import (create_engine,
                        PrimaryKeyConstraint,
                        ForeignKey,
                        Column,
                        String,
                        Integer,
                        CHAR,
                        Numeric,
                        Float,
                        Date,
                        DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import urllib

params = urllib.parse.quote_plus("Driver={SQL Server Native Client 11.0};"
                                 "Server=localhost\SQLEXPRESS;"
                                 "Database=QuantPortfolioRisk;"
                                 "Trusted_Connection=yes;")
# set connection for sqlalchemy
conn = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

Base = declarative_base()


