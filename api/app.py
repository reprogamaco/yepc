from flask import Flask,render_template,redirect,request
from datetime import date
import random

app = Flask(__name__)

mode = 'development'
# mode = 'production'

# dealing with dates
today = date.today()
engDate = today.strftime("%B %d, %Y") # July 01,2023
year = today.strftime("%Y") # 2023

# website variables
website_full = 'Yusuph Events planning planning & Catering'
website_short = 'yepc'
slogan = 'Make Your Event Memorable with Us'
developer = 'masterplan'
logo = '/static/imgs/logos/logo-no-background.svg'
owner = 'Yusuph Event planning & Catering'
phoneNos = ['255769665666','255672665664']
phone = random.choice(phoneNos)



# mode of the website
if mode == 'production':
    home = 'https://yusuph-event-planners.vercel.app/'
elif mode == 'development':
    home = 'localhost:5000/'

# choose the random phoneNo
if phone == '255769665666':
    phoneNo = '(+255) 769 665 666'
    phoneWp = '255769665666'
elif phone == '255672665664':
    phoneNo = '(+255) 672 665 664'
    phoneWp = '255672665664'















# ------------ end of the variables of the website ---------- #







#################################################
## ******************************************* ##
# -------- starts of the functions ------------ #
## ***********codes*and*functions************** #
#################################################

'''
# The index page
@app.route('/')
def index():
    return redirect('/en/')
'''

# assumption made all the pages are english
# but make the reserve for easy intergration of the system,
# in the near future

# the home (english) page
@app.route('/')
def en_home():
    headers = {
        'title': website_full,
        'website_full': website_full,
        'description':'Welcome to our comprehensive event planning and catering services website. From weddings to corporate events, our team of experienced professionals is here to bring your vision to life. Discover our wide range of services, including venue selection, event coordination, and exquisite catering options. Whether you\'re hosting an intimate gathering or a grand celebration, trust us to handle every detail with meticulous care. Visit us now and let us turn your event into an unforgettable experience.',
        'backend': developer,
        'phoneNo': phoneNo,
        'logo':logo,
        'year': year,
        'owner': owner,
        'phoneWp': phoneWp,

    }
    return render_template('/en-home.html',**headers)



# the navigation pages
@app.route('/<name>')
def en_nav(name):
    if name == 'services':
        # the service page is rendered here
        headers = {
            'title': 'Explore Our Services We Provide',
            'website_full': website_full,
            'description': 'Discover our comprehensive range of professional event planning and catering services at Yusuph Event Planning and Catering. From corporate events to weddings and special occasions, our team of experienced professionals is dedicated to creating unforgettable experiences. We offer meticulous event coordination, personalized menu options, exquisite cuisine, and top-notch service. Contact us today to bring your vision to life and make your event a resounding success.',
            'backend': developer,
            'phoneNo' : phoneNo,
            'logo': logo,
            'year': year,
            'owner': owner,
            'phoneWp': phoneWp,
        }
        return render_template('/en-services.html',**headers)
    elif name == 'contact-us':
        # the contact-us page
        headers = {
            'title': 'Check how can you reach Us',
            'website_full': website_full,
            'description': 'Contact us with email, phone numbers, through whatsapp, telegram and etc',
            'backend': developer,
            'phoneNo': phoneNo,
            'logo': logo,
            'year': year,
            'owner': owner,
            'phoneWp': phoneWp,
        }
        return render_template('/en-contact-us.html',**headers)
    else:
        return redirect('/')



@app.route('/forms/<name>')
def forms(name):
    if name == 'en-form-contactus':
        headers = {
            'title': 'english form contact us',
            'website_full': website_full,
            'description': 'Contact us with email, phone numbers, through whatsapp, telegram and etc',
            'backend': developer,
            'phoneNo': phoneNo,
            'logo': logo,
            'year': year,
            'owner': owner,
            'phoneWp': phoneWp,
        }
        return render_template('/en-contact-form.html',**headers)
    else:
        return redirect('/')








#########################################
#########################################
##### server configurations stuffs ######
#########################################
#########################################





# handling the 404 error
@app.errorhandler(404)
def page_404(error):
    #lets redirect home
    return redirect('/')

# redirecting to https (443)
@app.before_request
def forwarding_https():
    if not request.is_secure:
        url = request.url.replace('http://','https://',1)
        code = 301 #redirect code
        return redirect(url,code=code)

if __name__ == '__main__':
    if mode == 'development':
        app.run(debug=True)
    elif mode == 'production':
        #never show the errors to the users!
        app.run()
    