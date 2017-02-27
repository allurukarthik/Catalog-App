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

item1 = CategoryItem(name="Harry Potter", user_id=1, description="Harry Potter is a series of fantasy novels written by British author J. K. Rowling. The novels chronicle the life of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic, and subjugate all wizards and Muggles, a reference term that means non magical people.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Artemis Fowl", user_id=1,  description="Artemis Fowl is a young adult fantasy novel written by Irish author Eoin Colfer. It is the first book in the Artemis Fowl series, followed by Artemis Fowl: The Arctic Incident. Described by its author as Die Hard with fairies it follows the adventures of Artemis Fowl, a twelve-year-old criminal mastermind, as he kidnaps a fairy for a large ransom of gold.", category=category1)

session.add(item2)
session.commit()


# Items for Woodwinds
category2 = Category(name=" Social engineering", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="The Art of Intrusion", user_id=1, description="The Art of Intrusion: The Real Stories Behind the Exploits of Hackers, Intruders, & Decievers is a book by Kevin Mitnick that is a collection of stories about social engineering as performed by other hackers. Each story ends by summarizing insight into the attack as well as measures to defend against it. The book was published after Mitnick's first book, The Art of Deception, and explores the same themes introduced in the first book.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Art of Deception", user_id=1,  description="The Art of Deception is a book by Kevin Mitnick that covers the art of social engineering. Part of the book is composed of real stories, and examples of how social engineering can be combined with hacking.", category=category2)

session.add(item2)
session.commit()



# Items for Percussion
category3 = Category(name="Self Help", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="The 7 Habits of Highly Effective People", user_id=1, description="The 7 Habits of Highly Effective People, first published in 1989, is a business and self-help book written by Stephen R. Covey.Covey presents an approach to being effective in attaining goals by aligning oneself to what he calls true north principles of a character ethic that he presents as universal and timeless.", category=category3)

session.add(item1)
session.commit()



# Items for Brass
category4 = Category(name="Non Fiction", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Quiet: The Power of Introverts in a World That Can't Stop Talking", user_id=1, description="Quiet: The Power of Introverts in a World That Can't Stop Talking is a 2012 non-fiction book written by Susan Cain. Cain argues that modern Western culture misunderstands and undervalues the traits and capabilities of introverted people, leading to a colossal waste of talent, energy, and happiness.", category=category4)

session.add(item1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
