from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from telephone_network_db.alchemy.database import Base



class ClientsORM(Base):
    __tablename__ = 'Clients'

    ID: Mapped[int] = mapped_column(primary_key=True)
    NickName: Mapped[str] = mapped_column(nullable=False, unique=True)
    Password: Mapped[str] = mapped_column(nullable=False)


class ClientInfoORM(Base):
    __tablename__ = 'Client_Info'

    ClientID: Mapped[int] = mapped_column(ForeignKey("Clients.ID"), nullable=False, primary_key=True, unique=True)
    FirstName: Mapped[str] = mapped_column(nullable=False)
    SecondName: Mapped[str] = mapped_column(nullable=False)
    Patronymic: Mapped[str] = mapped_column(nullable=False)
    Address: Mapped[str] = mapped_column(nullable=False)
    Email: Mapped[str] = mapped_column(nullable=False, unique=True)


class ClientDevicesORM(Base):
    __tablename__ = 'Client_Devices'

    ID: Mapped[int] = mapped_column(primary_key=True)
    ClientID: Mapped[int] = mapped_column(ForeignKey("Clients.ID"), nullable=False)
    DeviceType: Mapped[str] = mapped_column(nullable=False)
    PhoneNumber: Mapped[str] = mapped_column(nullable=False, unique=True)
    SubscriptionPlan: Mapped[str] = mapped_column(nullable=False)
    Balance: Mapped[float] = mapped_column(nullable=True)


class NumberCallORM(Base):
    __tablename__ = 'Number_Call'

    ID: Mapped[int] = mapped_column(primary_key=True)
    DeviceID: Mapped[int] = mapped_column(ForeignKey("Client_Devices.ID"), nullable=False)
    Duration: Mapped[int] = mapped_column(nullable=False)
