from flask import Flask, redirect, url_for, request
import json
from paddlenlp import Taskflow
import threading
similarity = Taskflow("text_similarity")
lock = threading.Lock()

app = Flask(__name__)



@app.route('/getss',methods = ['POST'])
def getss():
  print(request.json)
  lock.acquire()
  result = similarity(request.json)
  lock.release()
  flag = -1
  score = 0.7
  for index,obj in enumerate(result):
    print(obj['similarity'])
    if(obj['similarity'] > score and obj['similarity'] <= 1):
      score = obj['similarity']
      flag = index
  if(flag != -1):
    print(result[flag])

  return json.dumps(flag)


if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5000, debug=True) 

