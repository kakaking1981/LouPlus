from flask import Flask
import os
import json
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    files = os.listdir("/home/shiyanlou/files")
    fileAndPath = ['/home/shiyanlou/files/'+files[0],'/home/shiyanlou/files/'+files[1]]
    title = []
    for testFile in fileAndPath:
        with open(testFile,'r') as f:
            data = json.load(f)
            title.append(data['title'])
    return render_template('index.html',title=title)

@app.route('/files/<filename>')
def file(filename):
    files = os.listdir("/home/shiyanlou/files")
    fileWithfix = filename+'.json'
    if fileWithfix not in files:
        return render_template('404.html')
    filePath = '/home/shiyanlou/files/'+filename+'.json'
    with open(filePath,'r') as f:
        data = json.load(f)
        return data['content']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
