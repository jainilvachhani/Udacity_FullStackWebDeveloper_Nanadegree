from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

users = [{'email' : 'jainilvachhani@gmail.com', 'name' : 'jainilvachhani'}]

for i in users:
	user = User(email = i['email'], name = i['name'])
	session.add(user)
	session.commit()
user_1 = user.id

category1 = Category(name = 'TV Series',user_id = user_1)
session.add(category1)
session.commit()

item1 = Item(
name = 'FRIENDS', 
user_id = user_1,
category_id = 1,
description = 'Follow the lives of six reckless adults living in Manhattan, as they indulge in adventures which make their lives both troublesome and happening'
)
session.add(item1)
session.commit()

item2 = Item(
name = 'HowIMetYourMother',
user_id = user_1, 
category_id = 1,
description = 'Ted Mosby, an architect, recounts to his children the events that led him to meet their mother. His journey is made more eventful by the presence of his friends Lily, Marshall, Robin and Barney.'
)
session.add(item2)
session.commit()


item3 = Item(
name = 'Sherlock', 
user_id = user_1, 
category_id = 1,
description = 'Dr. Watson, a former army doctor, finds himself sharing a flat with Sherlock Holmes, an eccentric individual with a knack for solving crimes. Together, they take on the most unusual cases.'
)
session.add(item3)
session.commit()

category2 = Category(name = 'Books',user_id = user_1)
session.add(category2)
session.commit()

item1 = Item(
name = 'TheKiteRunner', 
user_id = user_1, 
category_id = 2,
description = 'Amir lives in California with his wife Soraya. He receives a call from his uncle Rahim Khan who urges him to travel to Pakistan and rescue the son of Amir childhood servant and friend, Hassan.'
)
session.add(item1)
session.commit()

item2 = Item(
name = 'TheDaVinciCode', 
user_id = user_1, 
category_id = 2,
description = 'Symbologist Robert Langdon travels from Paris to London to discover the truth behind a mysterious and bizarre murder. Later, he learns about a religious mystery protected by a secret society.'
)
session.add(item2)
session.commit()

item3 = Item(
name = 'OctoberSky', 
user_id = user_1, 
category_id = 2,
description = 'The true story of one of America first rocket engineers and how he went against his father wishes to fulfil his great destiny.'
)
session.add(item3)
session.commit()
	
category3 = Category(name = 'Movies',user_id = user_1)
session.add(category3)
session.commit()

item1 = Item(
name = 'DeadPoetsSociety', 
user_id = user_1, 
category_id = 3,
description = 'John Keating, a progressive English teacher, encourages his students to break free from the norms, go against the status quo and live unapologetically.'
)
session.add(item1)
session.commit()

item2 = Item(
name = 'TheShawshankRedemption', 
user_id = user_1, 
category_id = 3,
description = 'Andy Dufresne, a successful banker, is arrested for the murders of his wife and her lover, and is sentenced to life imprisonment at the Shawshank prison. He becomes the most unconventional prisoner.'
)
session.add(item2)
session.commit()

item3 = Item(
name = 'ForrestGump', 
user_id = user_1, 
category_id = 3,
description = 'Forrest Gump, a man with a low I.Q., joins the army for service where he meets Dan and Bubba. However, he cannot stop thinking about his childhood sweetheart Jenny Curran, whose life is messed up.'
)
session.add(item3)
session.commit()	