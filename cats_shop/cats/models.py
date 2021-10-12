from cats_shop import db


class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,  nullable=False)
    breed = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String)

    def __init__(self, name, breed, age, description, image_url):
        self.name = name
        self.breed = breed
        self.age = age
        self.description = description
        self.image_url = image_url

    def __repr__(self):
        return f'{self.name}'

# db.session.add(Cat(name='Мурзик', breed='Метис', age=5, description='', image_url='/cats/1.jpg'))
# db.session.commit()
