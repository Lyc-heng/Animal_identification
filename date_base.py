from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    with app.app_context():
        from date import User
        db.create_all()

        db.session.merge(User(id=1, animals='有毛发、哺乳动物'))
        db.session.merge(User(id=2, animals='有奶、哺乳动物'))
        db.session.merge(User(id=3, animals='有羽毛、是鸟'))
        db.session.merge(User(id=4, animals='会飞、会下蛋、是鸟'))
        db.session.merge(User(id=5, animals='吃肉、肉食动物'))
        db.session.merge(User(id=6, animals='有犬齿、有爪、眼盯前方、肉食动物'))
        db.session.merge(User(id=7, animals='哺乳动物、有蹄、有蹄动物'))
        db.session.merge(User(id=8, animals='哺乳动物、嚼反刍动物、有蹄动物'))
        db.session.merge(User(id=9, animals='哺乳动物、肉食动物、黄褐色、身上有暗斑点、金钱豹'))
        db.session.merge(User(id=10, animals='哺乳动物、肉食动物、黄褐色、有黑色条纹、虎'))
        db.session.merge(User(id=11, animals='有蹄动物、有长脖子、有长腿、身上有暗斑点、长颈鹿'))
        db.session.merge(User(id=12, animals='有蹄动物、有黑色条纹、斑马'))
        db.session.merge(User(id=13, animals='是鸟、有长脖子、有长腿、不会飞、鸵鸟'))
        db.session.merge(User(id=14, animals='是鸟、会游泳、不会飞、有黑白两色、企鹅'))
        db.session.merge(User(id=15, animals='是鸟、善飞、信天翁'))

        db.session.commit()

    return app
