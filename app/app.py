from flask import Flask
from redis import Redis
from controllers.aozora_controller import AozoraController


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return 'Hello My App'


@app.route('/redis_hits')
def redis_hits():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


@app.route('/aozora', methods=['GET'])
def search_music():
    return AozoraController.search()


@app.route('/elasticsearch')
def elasticsearch():
    return 'hoge'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
