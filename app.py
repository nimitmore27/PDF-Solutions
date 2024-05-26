from flask import Flask, request, render_template, url_for, jsonify
from os import  path as osPath
from utils import *

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/convert', methods=['GET','POST'])
def convert_endpoint():
    if request.method == 'GET':
        return render_template('d2p.html')

    file = request.files['files']
    try:
        file_path = osPath.join(TEMP_FILES, file.filename)
        file.save(file_path)
        output = file.filename.split('.')[0] + '.pdf'
        output_path = osPath.join(TEMP_PDFS,output)
    except Exception as e:
        print("convert_endpoint() : ",e)
        res = {'success':False}
        return render_template('download.html', res = res)
    if file.filename.endswith('.docx') or file.filename.endswith('.doc'):
        d2p_cov(file_path, output_path)
    url = url_for('static', filename='_temp_pdfs/' + output)
    res = {'success':True,'url': url}
    return jsonify(res)

@app.route('/merge', methods=['GET','POST'])
def merge_endpoint():
    if request.method == 'GET':
        return render_template('merge.html')
    
    files = request.files.getlist('files')
    try:
        file_paths = []
        for file in files:
            file_path = osPath.join(TEMP_FILES, file.filename)
            file.save(file_path)
            file_paths.append(file_path)
        output = files[0].filename.split('.')[0] + '_merged.pdf'
        output_path = osPath.join(TEMP_PDFS,output)
    except Exception as e:
        print("merge_endpoint() : ",e)
        res = {'success':False}
        return jsonify(res)
    if merge_pdfs(file_paths, output_path):
        url = url_for('static', filename='_temp_pdfs/' + output)
        res = {'success':True,'url': url}
    else:
        res = {'success':False}
    return jsonify(res)

@app.route('/clear_memory', methods=['GET','POST'])
def clear_memory():
    if request.method == 'GET':
        return render_template('clear_memory.html')
    try:
        delete_old_files()
    except Exception as e:
        print("clear_memory() : ",e)
        return jsonify({'success':False})
    return jsonify({'success':True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)