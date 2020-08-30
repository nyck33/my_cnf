from flask import current_app as app, request, render_template, abort, url_for, session, redirect
from cnf.models import (
    CNFFoodName, CNFConversionFactor, CNFNutrientAmount,
    CNFYieldAmount, CNFRefuseAmount
)
#from cnf.login_form import LoginForm
from flask import current_app as app
from flask_user import login_required

db = app.db


@app.route('/', methods=['GET', 'POST'], endpoint='cnf.login')
def login():
    name = None
    password = None
    '''
    form = LoginForm()
    # form = request.form

    if form.validate_on_submit():
        session['name'] = request.form.get('name')  # form.name.data
        session['password'] = request.form.get('password')  # form.password.data
        session['logged_in'] = True
        return redirect(url_for('cnf.food_search'))
    '''
    # return render_template('login.html', form=form, name=session.get('name'), password=session.get('password'))
    if request.method == 'POST':
        request.session['logged_in'] = True
        return redirect(url_for('food_search'))
    # default
    return render_template('user_login.html')

@app.route('/user/<int:user_id>', methods=['GET'], endpoint='cnf.users')
def user_info():
    pass

@app.route('/food_search', methods=['GET'], endpoint='cnf.food_search')
@login_required  # User must be authenticated
def food_search():
    q = request.args.get('q')
    foods = CNFFoodName.objects.filter(description__icontains=q) if q else []
    #if session.get('logged_in'):
    return render_template('food_search.html', foods=foods, q=q)
    #else:
     #   return redirect(url_for('cnf.login'))
# app.add_url_rule('/', 'index', index)


@app.route('/<int:food_id>', methods=['GET'], endpoint='cnf.show')
def show(food_id):
    food = CNFFoodName.objects.get(id=str(food_id))
    conversions = CNFConversionFactor.objects.filter(food=food)
    nutrients = CNFNutrientAmount.objects.filter(food=food, nutrient_value__gt=0)
    yields = CNFYieldAmount.objects.filter(food=food)
    refuses = CNFRefuseAmount.objects.filter(food=food)
    return render_template(
        'show.html',
        food=food,
        conversions=conversions,
        nutrients=nutrients,
        yields=yields,
        refuses=refuses,
    )
# app.add_url_rule('/show', 'show', show)


