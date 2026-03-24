class EventManager:
    def __init__(self):
        print("Event Manager:: Let me talk to the folks \n")
        
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()
        
        self.florist = Florist()
        self.florist.set_flower_requirements()
        
        self.caterer = Caterer()
        self.caterer.set_cuisine()
        
        self.musican = Musican()
        self.musican.set_music_type()
        

class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for marriage? --")
        
    def __is_avaliable(self):
        print("is the Hotel free for the event given day?")
        
    def book_hotel(self):
        if self.__is_avaliable():
            print("Registered the booking\n\n")
            

class Florist(object):
    def __init__(self):
        print("Flower decorations for the event? --")
        
    def set_flower_requirements(self):
        print("Carnations, roses and lilies would be used for decorations\n\n")
        

class Caterer(object):
    def __init__(self):
        print("Food arrangements for the event --")
        
    def set_cuisine(self):
        print("Chinese & continental cuisine to be served\n\n")
        
        
class Musican(object):
    def __init__(self):
        print("Musical arragements for the marriage --")
        
    def set_music_type(self):
        print("Jazz and classical will be playlist\n\n")
        
        
class You(object):
    def __init__(self):
        print("\nYou:: Whoa! Marriage arragements???!!!")
        
    def ask_event_manager(self):
        print("You:: Lets contact the event manager\n\n")
        em = EventManager()
        em.arrange()
        
    def __del__(self):
        print("You:: Thanks to the event manager, all preparations done! Phew!")
        
you = You()
you.ask_event_manager()
        
    