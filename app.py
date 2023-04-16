from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/links', methods=['GET', 'POST'])
def get_links():
    if request.method == 'POST':
        url = request.form['url']
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all('a')
        urls = [link.get('href') for link in links]
        return render_template('links.html', urls=urls)
    else:
        return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
