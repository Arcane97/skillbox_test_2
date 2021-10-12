from cats_shop import create_app, db
from cats_shop.cats.models import Cat
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # db.session.add(Cat(name='Мурзик', breed='Кёрл', age=5, description='Серый полосатый', image_url='/img/cats/1.jpg'))
        # db.session.add(Cat(name='Колобок', breed='Ванская', age=4, description='Белый', image_url='/img/cats/2.jpg'))
        # db.session.add(Cat(name='Рыжик', breed='Метис', age=4, description='Рыжий полосатый', image_url='/img/cats/3.jpg'))
        # db.session.add(Cat(name='Соня', breed='Шартрез', age=1, description='Серая пушыстая', image_url='/img/cats/4.jpg'))
        # db.session.add(Cat(name='Гар', breed='Персидская', age=8, description='Рыжий пушистый', image_url='/img/cats/5.jpg'))
        # db.session.add(Cat(name='Вова', breed='Сфинкс', age=2, description='Голый серый', image_url='/img/cats/6.jpg'))
        # db.session.commit()
        app.run(debug=True, port=8080)
