from goglekaap import db
from sqlalchemy import func

class User( db.Model ):
    __tablename__ = 'USER'

    id = db.Column( db.Integer, primary_key = True )
    user_id = db.Column( db.String( 128 ), unique = True, nullable = False )
    user_name = db.Column( db.String( 20 ), nullable = False )
    password = db.Column( db.String( 256 ), nullable = False )
    # func.now() 지금 현재 시각을 디폴트로 하기 위해 필요한 함수
    # default와 server_default의 차이는 기존의 컬럼까지 전부 now()를 적용시켜주는 것이냐 아니냐인데
    # server_default가 기존의 모든 row에 적용을 시켜준다.
    created_at = db.Column(db.DateTime(), server_default = func.now())

    def __repr__( self ):
        return "<User('%s', '%s')>" % (self.email, self.nick_name)

    @classmethod
    def find_one_by_user_id( cls, user_id ):
        return User.query.filter_by( user_id = user_id ).first()
