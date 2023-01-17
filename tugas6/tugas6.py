from flask import Flask, render_template, url_for
application = Flask(__name__)
@application.route('/')
def index():
 return render_template('home.html')
@application.route('/kontak-saya')
def kontakSaya():
 return render_template('kontak-saya.html')
@application.route('/tentang-saya')
def tentangSaya():
 return render_template('tentang-saya.html')
if __name__ == '__main__':
 application.run(debug=True)