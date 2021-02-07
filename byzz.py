from flask import Flask, render_template
from flask import request

# Create a new web server Flask object
WebPage = Flask(__name__)

@WebPage.route('/')
def index():
    html_str = render_template('/index.html')
    return html_str

@WebPage.route('/answer.json', methods=['POST'])
def answer():
    content = request.json
    print(content)
    return "ok"

if __name__ == '__main__':
    # run server in debug mode
    WebPage.run(debug=True)
