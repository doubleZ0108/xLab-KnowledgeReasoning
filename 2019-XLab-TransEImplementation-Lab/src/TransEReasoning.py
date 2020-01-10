'''
@program: TransEReasoning.py

@description: 

@author: doubleZ

@create: 2019/12/06 
'''

from flask import Flask,jsonify
import src.TransE as TransE

app = Flask(__name__)  # 创建一个服务，赋值给APP

@app.route('/TransE_Reasoning',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post  #讲的是封装成一种静态的接口，无任何参数传入
def TransEReasoning():
    loss = TransE.main()
    return jsonify(loss)        #把字典转成json串返回


if __name__ == '__main__':
    app.run(host='localhost', port=8802, debug=True)
