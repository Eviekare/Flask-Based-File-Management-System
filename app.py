from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated file storage (in-memory list)
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files, theme='girly')

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if filename and filename not in files:
        files.append(filename)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    old_filename = request.form.get('old_filename')
    new_filename = request.form.get('new_filename')
    if old_filename in files and new_filename:
        files[files.index(old_filename)] = new_filename
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    filename = request.form.get('filename')
    if filename in files:
        files.remove(filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)