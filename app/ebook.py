from app.samting_in_libery import samting_in_libery
from datetime import date

class ebook(samting_in_libery):

#create a new object
    def __init__(self, time_taken:date, id, title, author, datePublication, status):
        self.time_taken = time_taken
        super().__init__(id, title, author, datePublication, status)

# get when is taken
    def get_time_taken_ebook(self):
        return self.time_taken


    def get_all_about_ebook(self):
       data = super().get_all_about_object_in_libery().copy()
       data.update(self.__dict__)
       return data

    def set_time_taken_ebook(self, time_taken):
        self.time_taken = time_taken

#time to over from take this
    def time_to_left_ebook(self, rule):
        left = date.today() - self.time_taken
        if left < rule.get_Ebook_time:
            return (rule.get_Magazine_time - left, 'okey')
        else:
            return (left, 'penalty')


