from sqlalchemy import create_engine, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,ForeignKey,String


db_connect_string='mysql://root:luo12138@127.0.0.1:3306/dbmysql?charset=utf8mb4'
# echo可以直接看到创建数据库的时候发送的代码
engine = create_engine(db_connect_string,echo=True)
Base = declarative_base(engine)

class Admin(Base):
    __tablename__='表名称'
    admin_id=Column(Integer,primary_key=True)
    name=Column(String(10))
    # 更改字符编码格式
    __table_args__ = {
        "mysql_charset": "utf8"
    }

class Electricity(Base):
    __tablename__ = 'sw_machine_electricity'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='电量id')
    number = Column(Integer, comment='电量')
    create_time = Column(DateTime, comment='创建时间')


# 位置
class Location(Base):
    __tablename__ = 'sw_machine_location'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='阻塞id')
    location = Column(String(64), comment='机器人位置')
    blocking = Column(String(64), comment='阻塞位置')
    create_time = Column(DateTime, comment='创建时间')


# 里程
class Mileage(Base):
    __tablename__ = 'sw_machine_mileage'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='里程id')
    mileage = Column(Float(4, 2), comment='里程')
    create_time = Column(DateTime, comment='创建时间')


# 操作
class Operation(Base):
    """
    1）RESTRICT：父表数据被删除，会阻止删除。默认就是这一项。
    2）NO ACTION：在MySQL中，同RESTRICT。
    3）CASCADE：级联删除。即父表数据被删除，子表也被删除。
    4）SET NULL：父表数据被删除，子表数据会设置为NULL。
    """
    __tablename__ = 'sw_machine_operation'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='操作id')
    operation = Column(String(64), comment='操作')
    state = Column(String(64), comment='状态')
    user_id = Column(Integer, ForeignKey('sw_user.id', ondelete="RESTRICT"), comment='用户id')
    create_time = Column(DateTime, comment='创建时间')


# 用户
class User(Base):
    __tablename__ = 'sw_user'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='用户id')
    username = Column(String(64), comment='用户名')
    password = Column(String(64), comment='密码')
    create_time = Column(DateTime, comment='创建时间')


# 机器操作
class MachineRecord(Base):
    __tablename__ = 'sw_machine_record'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='记录id')
    record_start = Column(DateTime, comment='开始时间')
    record_end = Column(DateTime, comment='结束时间')
    record_running = Column(DateTime, comment='运行时间')
    create_time = Column(DateTime, comment='创建时间')


# 放射物
class Rediation(Base):
    __tablename__ = 'sw_machine_rediation'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='放射物id')
    rediation_now = Column(Float(4, 2), comment='目前放射量')
    rediation_total = Column(Float(4, 2), comment='总放射量')
    create_time = Column(DateTime, comment='创建时间')


# 截图
class Screenshots(Base):
    __tablename__ = 'sw_machine_screenshots'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='截图id')
    create_time = Column(DateTime, comment='创建时间')


# 警告
class WarningRecord(Base):
    __tablename__ = 'sw_warning_record'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='警示id')
    warn_reason = Column(String(64), comment='警示原因')
    create_time = Column(DateTime, comment='创建时间')

Base.metadata.create_all()
