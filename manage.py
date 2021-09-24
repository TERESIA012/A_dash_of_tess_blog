from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import create_app,db
from app.models import Upvote, User,Post,Comment,Subscriber,Category

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def add_shell_context():
    return dict(app = app,db = db,User = User,Post=Post,Comment=Comment,Subscriber=Subscriber,Upvote=Upvote,Category=Category)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()