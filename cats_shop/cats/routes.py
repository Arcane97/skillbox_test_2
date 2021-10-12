from flask import Blueprint, render_template, request

from cats_shop.cats.models import Cat
from cats_shop import db


cats = Blueprint('cats', __name__)


@cats.route('/', methods=['GET', 'POST'])
def index():
    search_req = request.args.get('search')
    # print(search_req)
    if search_req:
        cats_data = Cat.query.filter(Cat.name.contains(search_req) | Cat.breed.contains(search_req) |
                                     Cat.description.contains(search_req) | Cat.age.contains(search_req))

    else:
        cats_data = Cat.query.all()
    # print(cats_data)
    # db.session.commit()
    return render_template('index.html', title='Котики', cats_data=cats_data)


@cats.route('/cat/<int:cat_id>')
def cat_page(cat_id):
    cat_data = Cat.query.get(cat_id)
    return render_template('cat.html', cat_data=cat_data)
