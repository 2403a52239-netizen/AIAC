from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from models import init_db, add_item, get_items, delete_item

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report_lost', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        name = request.form.get('name', '')
        desc = request.form.get('description', '')
        location = request.form.get('location', '')
        image = request.files.get('image')
        
        if not name or not desc or not location:
            return render_template('report_lost.html', error='Please fill in all fields')
        
        if not image or image.filename == '':
            return render_template('report_lost.html', error='Please select an image')
        
        filename = secure_filename(image.filename)
        if filename:
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            add_item(name, desc, location, filename, 'lost')
            return redirect(url_for('items'))
        else:
            return render_template('report_lost.html', error='Invalid filename')
    return render_template('report_lost.html')

@app.route('/report_found', methods=['GET', 'POST'])
def report_found():
    if request.method == 'POST':
        name = request.form.get('name', '')
        desc = request.form.get('description', '')
        location = request.form.get('location', '')
        image = request.files.get('image')
        
        if not name or not desc or not location:
            return render_template('report_found.html', error='Please fill in all fields')
        
        if not image or image.filename == '':
            return render_template('report_found.html', error='Please select an image')
        
        filename = secure_filename(image.filename)
        if filename:
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            add_item(name, desc, location, filename, 'found')
            return redirect(url_for('items'))
        else:
            return render_template('report_found.html', error='Invalid filename')
    return render_template('report_found.html')

@app.route('/items')
def items():
    all_items = get_items()
    return render_template('items.html', items=all_items)

@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item_route(item_id):
    delete_item(item_id)
    return redirect(url_for('items'))

if __name__ == '__main__':
    app.run(debug=True)