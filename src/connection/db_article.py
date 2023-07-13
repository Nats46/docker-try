from src.connection.article import article2
from src.connection.schema import articleBase
from sqlalchemy.orm.session import Session

def create_article(db:Session,request:articleBase):
    new_article=article(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db:Session,id:int):
    article=db.query(article2).filter(article2.id==id).first()
    return article