"""
routes.py
Route controls for website
"""
from app import app
from app import etl
from app.resources import pledgeForm, requestForm
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    # Instantiate pledge and request forms
    pledgeform = pledgeForm()
    requestform = requestForm()
    errorModal = False
    # User is submitting form
    if request.method == 'POST':
        # Check if pledge or request
        if pledgeform.pledgeSubmit.data and pledgeform.validate_on_submit():
            # Process pledge data
            pledgeformDocument = etl.process(pledgeform)
            print('Pledge form: ')
            print(pledgeformDocument)
            # Write document to collection
            etl.writePledge(pledgeformDocument)
            return render_template('confirm.html', confirmType='pledge')
        elif requestform.requestSubmit.data and requestform.validate_on_submit():
            # Process request data
            requestformDocument = etl.process(requestform)
            print('Request form: ')            
            print(requestformDocument)
            etl.writeRequest(requestformDocument)
            return render_template('confirm.html', confirmType='request')
        else:
            errorModal=True
    return render_template('index.html', pledgeform=pledgeform, requestform=requestform, errorModal=errorModal)

@app.route('/view', methods=['GET', 'POST'])
def view():
    requests = etl.getRequests()
    return render_template('view.html', requests=requests, title="View Requests")

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
