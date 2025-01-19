# pls test server on http://localhost:5000

# to update changes on web:
# - go to powershell[Shared] on bottom right side of screen
# - input ctrl + c
# - input "flask --app server run"

# instead of typing allat you can just press up arrow key to autofill the last typed command

from flask import Flask, render_template
from flask import flash, request, redirect, url_for, send_file
from flask import Response
from werkzeug.utils import secure_filename
import os
import platform

import pdftools
import img2table
import csv

WORKING_FOLDER = "/processing/"
PDF_FOLDER = "/static/outputpdfs/"
CSV_FOLDER = "/static/outputcsv"
TINGXIE_FOLDER = "/static/outputtingxie"

if "win" in platform.system().lower():
    WORKING_FOLDER = WORKING_FOLDER.replace('/', '\\')
    PDF_FOLDER = PDF_FOLDER.replace('/', '\\')
    CSV_FOLDER = CSV_FOLDER.replace('/', '\\')
    TINGXIE_FOLDER = TINGXIE_FOLDER.replace('/', '\\')

def get_file_extension(filename: str):

    i = filename.find(".")
    if i == -1: return None
    return filename[i:]

WORKING_FOLDER = os.getcwd() + WORKING_FOLDER
PDF_FOLDER = os.getcwd() + PDF_FOLDER
CSV_FOLDER = os.getcwd() + CSV_FOLDER
TINGXIE_FOLDER = os.getcwd() + TINGXIE_FOLDER

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/upload")
def upload():
    return render_template('check.html', titlename = "Upload file")

@app.route("/check")
def check():
    return render_template('check.html', titlename = "Grading")

@app.route("/exportpage")
def exportpage():
    pdf_link = request.args.get('file').strip()
    return render_template('exportpage.html', file=pdf_link)

@app.route("/markpage")
def markpage():
    return render_template('markpage.html')

@app.route("/convertedworksheet")
def convertedworksheet():
    return render_template('convertedworksheet.html')


@app.route("/upload_photo_scan", methods=["POST"])
def process_photo():
    if 'photo' not in request.files:
        print("no photo received. very sad.")
        flash('No file part')
        return redirect(request.url)


    photo = request.files["photo"]
    if photo.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    # use this path to process the image!
    # remember to delete after done
    photoname = pdftools._make_tempfilename(get_file_extension(photo.filename))
    photopath = os.path.join(WORKING_FOLDER + photoname)
    print(f"saved to {photopath}")

    photo.save(photopath)

    

    return {
        "url" : "/",
        "photoname" : photoname
    }

@app.route("/wait_for_pdf", methods=["POST"])
def get_pdf_link():
    data = request.get_json()

    if not data:
        return '''
<!DOCTYPE html>
<html>

<head>
    <title>ERROR</title>
</head>

<body>
    <h1>An error has occured</h1>
    <br>
    <br>
    <h4>our bad.</h4>
    <h3>Please navigate back to the main page.</h3>
</body>

</html>
        '''
    print("parsing photoname")
    #photoname = data.get("photo_name")
    print(data)
    photoname = data["photo_name"]
    print(photoname)
    photopath = os.path.join(WORKING_FOLDER + photoname)
    output = img2table.read_image(photopath)

    add1 = True
    add1i = 0
    for x in output[0]:
        if "中文" in x or "华语" in x:
            add1 = False
        add1i += 1

    if add1 == True:
        o = ["English", "English"]
        o[add1i] = "中文"
        output[0] = o


    

    for x in output:
        print(x)
    basename = photoname[:photoname.rfind(".")]

    pdfname = basename + ".pdf"
    csvname = basename + ".csv"


    print(os.path.join(PDF_FOLDER, pdfname))

    pdftools.create_pdf(output, os.path.join(PDF_FOLDER, pdfname))

    with open(os.path.join(CSV_FOLDER, csvname), 'w') as newfile:
        writer = csv.writer(newfile)
        writer.writerows(output)



    return {
        "redirect" : "/exportpage?file=/pdf/" + pdfname
    }

@app.route("/pdf/<pdfname>", methods=['GET'])
def access_pdf(pdfname):


    
    return send_file(os.path.join(PDF_FOLDER, pdfname), mimetype='application/pdf')

@app.route("/pdf/csv/<csvname>", methods=['GET'])
def access_csv(csvname):
    realcsvname = csvname[:csvname.rfind(".")] + '.csv'


    
    return send_file(os.path.join(CSV_FOLDER, realcsvname))







