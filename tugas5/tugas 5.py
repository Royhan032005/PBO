from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hobiku/<string:nama>')
def getnama(nama):
 nama = "Nama saya {}" .format(nama)
 hobi = ['membaca' , 'gaming' , 'menggambar ']
 return render_template('hobiku.html', nama = nama , hobi = hobi)
if __name__ == '__main__':
 app.run(debug=True)