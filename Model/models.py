#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Numeric, String, Table, text
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
metadata = Base.metadata

class HlhGiftcard(Base):
    __tablename__ = 'hlh_giftcard'

    ID = Column(Integer, primary_key=True)
    CardName = Column(String(20))
    SchemaID = Column(Integer)
    CardNO = Column(String(10), nullable=False, unique=True)
    ExchgCode = Column(String(10), unique=True)
    ExchgDate = Column(DateTime)
    SalePrice = Column(Numeric(8, 2))
    NeedExchgCde = Column(String(2), server_default=text("'Y'"))
    DispatchID = Column(Integer)
    IsActive = Column(String(2), nullable=False, index=True, server_default=text("'N'"))
    IsExchg = Column(String(2), nullable=False, index=True, server_default=text("'N'"))
    IsShipping = Column(String(2), nullable=False, index=True, server_default=text("'N'"))
    ActiveBy = Column(String(10))
    ActiveDate = Column(DateTime)
    CreateBy = Column(String(10))
    CreateDate = Column(DateTime)
    LastUpdBy = Column(String(10))
    LastUpdDt = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CustomerName = Column(String(20), index=True)
    cust_id = Column(Integer, index=True)


class HlhGiftcardexchg(Base):
    __tablename__ = 'hlh_giftcardexchg'

    ID = Column(Integer, primary_key=True)
    GiftCardID = Column(Integer, index=True)
    ShippingBy = Column(String(10))
    MobileNO = Column(String(20))
    ShippingAdress = Column(String(500))
    ShipOrderNo = Column(String(50))
    ExpressCompanyName = Column(String(200))
    ProductName = Column(String(50))
    ShippingDate = Column(DateTime)
    CreateBy = Column(String(10))
    CreateDate = Column(DateTime)
    LastUpdBy = Column(String(10))
    LastUpdDt = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    ShippingTo = Column(String(10))
    ProductImage = Column(String(120))
    Province = Column(String(20))
    City = Column(String(20))
    Area = Column(String(20))
    ExchgDate = Column(DateTime)
    ShippingRemark = Column(String(200))


class HlhMnssetting(Base):
    __tablename__ = 'hlh_mnssetting'

    ID = Column(Integer, primary_key=True)
    MNSCode = Column(String(20), unique=True)
    MNSName = Column(String(50))
    SITCode = Column(String(50))
    UATCode = Column(String(50))
    PRODCode = Column(String(50))
    TriggerConditon = Column(String(200))
    FormatType = Column(String(50))
    MNSContent = Column(String(50))
    CreateBy = Column(String(10))
    CreateDate = Column(DateTime)
    LastUpdBy = Column(String(10))
    LastUpdDt = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class HlhMnssublog(Base):
    __tablename__ = 'hlh_mnssublog'

    ID = Column(Integer, primary_key=True)
    MNSPubID = Column(Integer, index=True)
    MNSSubID = Column(Integer, index=True)
    SubDate = Column(DateTime)
    SubContent = Column(String(2000))
    SubStatus = Column(String(2))
    ErrContent = Column(String(500))


class HlhSchema(Base):
    __tablename__ = 'hlh_schema'

    ID = Column(Integer, primary_key=True)
    SchmNo = Column(String(10))
    SchemaType = Column(String(20))
    SchmName = Column(String(10), nullable=False)
    SchemaStatus = Column(String(20), server_default=text("'ONL'"))
    CustomerName = Column(String(20), index=True)
    H5Link = Column(String(200))
    ProdListLink = Column(String(255))
    Price = Column(Numeric(8, 2))
    From_Name = Column(String(50))
    Blessing = Column(String(400))
    To_Name = Column(String(50))
    CreateBy = Column(String(10))
    CreateDate = Column(DateTime)
    LastUpdBy = Column(String(10))
    LastUpdDt = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    Customer_id = Column(Integer)
    MareketPrice = Column(Numeric(8, 2))
    StckOnHand = Column(Integer, server_default=text("'0'"))
    SalesSum = Column(Integer)
    SchemaMusicId = Column(Integer)
    wxShareTitle = Column(String(50))
    wxShareDesc = Column(String(200))
    H5CardID = Column(Integer)
    Incolorcode = Column(String(10))
    outcolorcode = Column(String(10))
    VcardTxt = Column(String(400))
    cust_id = Column(Integer, index=True)


t_v_sxs_customer = Table(
    'v_sxs_customer', metadata,
    Column('id', Integer, server_default=text("'0'")),
    Column('customer_code', String(20)),
    Column('username', String(60)),
    Column('customer_name', String(333)),
    Column('phone', BigInteger),
    Column('crdt_points_limit', Float(10)),
    Column('crdt_points_total', Float(10)),
    Column('fid', Integer)
)
