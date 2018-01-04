from flask_script import Server, Manager

from skeleton.application import app

manager = Manager(app)

manager.add_command("runserver", Server(host="0.0.0.0", port=9000))
	
@manager.command
def hello():
    print("hello")

if __name__ == "__main__":
    manager.run()
