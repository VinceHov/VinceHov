from flask import Flask
from flask import request
# from werkzeug import secure_filename
import re
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def mainResponse():
    if request.method == 'POST':
#        print(request.data, request.args, request.json)
        file = request.data
        name = re.findall("\d+\.\d+\.\d+\.\d+", file.decode('utf-8'))[0]
        something = open("/home/ubuntu/pyrest/%s.txt" % name, "wb")
        something.write(file)
        something.close()
        return "POST METHOD\n"
    elif request.method == 'GET':
        return "Нет, го лучше сервер делать по майнкрафту\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"))
