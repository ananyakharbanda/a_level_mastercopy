
import flask

app = flask.Flask(__name__)

@app.route('/home/') # always safer to have trailing slashes
def home():
    return 'heya'

@app.route('/path_name/<int:i>/') # < int:i > whole thing in the angular bracket
def return_int(i):
    return 'this is the int ' + str(i)

@app.route('/path_str/<string:s>') # string:s or can just keep it as s 
def return_str(s):
    return 'this is the str ' + s

@app.route('/path_float/<float:f>')
def return_float(f):
    # return 'this is the float ' + str(f)
    headers = {"Content-Type": "text/plain"}
    return ('this is the float ' + str(f), 200, headers) #--> status codes in tuple

if __name__ == '__main__':

    app.run() # blocking call
    print('app ran')

    