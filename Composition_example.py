class house():
    def __init__(self, kitchen, bedroom, living_room):
        self.__kitchen = kitchen
        self.__bedroom = bedroom
        self.__living_room = living_room
    def get_kitchen(self):
        return self.__kitchen
    def get_bedroom(self):
        return self.__bedroom
    def get_living(self):
        return self.__living_room
    
class human():
    def __init__(self, location=""):
        self.__location = location
        self.house = house("kitchen", "bedroom", "living_room")
    def location(self):
        self.__location = self.house.get_kitchen()
        return self.__location
    
ralph = human()
print(ralph.location())