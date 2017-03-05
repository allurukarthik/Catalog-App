from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Fiction
category1 = Category(name="Fiction", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Harry Potter", user_id=1, description="Harry Potter is a series of magic and wizardry ", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Artemis Fowl", user_id=1,  description="Artemis Fowl is a young adult fantasy novel written by Irish author Eoin Colfer. ", category=category1)

session.add(item2)
session.commit()


# Items for Woodwinds
category2 = Category(name=" Social engineering", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="The Art of Intrusion", user_id=1, description="The Art of Intrusion: The Real Stories Behind the Exploits of Hackers.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Art of Deception", user_id=1,  description="The Art of Deception is a book by Kevin Mitnick  ", category=category2)

session.add(item2)
session.commit()



# Items for Percussion
category3 = Category(name="Self Help", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="The 7 Habits of Highly Effective People", user_id=1, description="The 7 Habits of Highly Effective people", category=category3)

session.add(item1)
session.commit()



# Items for Brass
category4 = Category(name="Non Fiction", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Quiet: The Power of Introverts in a World That Can't Stop Talking", user_id=1, description="Quiet: The Power of Introverts in a World That Can't Stop Talking  ", category=category4)

session.add(item1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
