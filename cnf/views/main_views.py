from flask import (current_app as app, request, render_template, abort,
                   url_for, session, redirect, Blueprint)
from cnf.models import (
    CNFFoodName, CNFConversionFactor, CNFNutrientAmount,
    CNFYieldAmount, CNFRefuseAmount
)
#from cnf.login_form import LoginForm
from flask_user import login_required, current_user, roles_required
from cnf.models.user_models import UserProfileForm


main_blueprint = Blueprint('main', __name__, template_folder='templates')


#@app.route('/', methods=['GET', 'POST'], endpoint='cnf.login')
@main_blueprint.route('/')
def home_page():
    # default
    return render_template('main/home.html')

#@app.route('/user/<int:user_id>', methods=['GET'], endpoint='cnf.users')
@main_blueprint.route('/member')
@login_required
def member_page():
    """
    Display user account info
    :return:
    """
    return render_template('main/member_page.html')

@main_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    form = UserProfileForm(request.form, obj=current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)
        # Save user profile in mongo here

        # redirect to home page
        return redirect(url_for('main.home_page'))

    # Process GET or invalid POST
    return render_template('main/user_profile_page.html', form=form)


#@app.route('/food_search', methods=['GET'], endpoint='cnf.food_search')
@main_blueprint.route('/food_search', methods=['GET', 'POST'])
@login_required  # User must be authenticated
def food_search():
    q = request.args.get('q')
    foods = CNFFoodName.objects.filter(description__icontains=q) if q else []

    return render_template('main/food_search.html', foods=foods, q=q)


# app.add_url_rule('/', 'index', index)
@main_blueprint.route('/<int:food_id>', methods=['GET'])
@login_required  # User must be authenticated
def show(food_id):
    food = CNFFoodName.objects.get(id=str(food_id))
    conversions = CNFConversionFactor.objects.filter(food=food)
    nutrients = CNFNutrientAmount.objects.filter(food=food, nutrient_value__gt=0)
    yields = CNFYieldAmount.objects.filter(food=food)
    refuses = CNFRefuseAmount.objects.filter(food=food)
    return render_template(
        'main/show.html',
        food=food,
        conversions=conversions,
        nutrients=nutrients,
        yields=yields,
        refuses=refuses,
    )
# app.add_url_rule('/show', 'show', show)


