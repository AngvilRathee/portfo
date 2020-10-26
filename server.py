from flask import Flask, render_template , url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)     # instead of making each separate link for each page, just make your func like this


@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

# @app.route('/index.html')
# def index():
#     return render_template('index.html')    

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["text_info"]
        file = database.write(f' \n\n\n email: {email},\n Subject: {subject},\n Message: {message}')
        
def write_to_csv(data):
    with open('data.csv', mode='a') as data2:
        email = data["email"]
        subject = data["subject"]
        message = data["text_info"]
        csv_writer = csv.writer(data2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank.html')
    else:
        return 'something went wrong'

















