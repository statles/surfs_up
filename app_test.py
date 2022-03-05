from flask import Flask

#create an app using magic methods
app = Flask(__name__)
#create a root
#create a function
@app.route('/')
def hello_world():
    return 'Hello world'
hello_world()

@app.route('/surf')
def moon(phase):
    print("The moon is " + phase)
moon("full")
