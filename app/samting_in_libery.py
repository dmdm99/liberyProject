from abc import ABC, abstractmethod
from datetime import date

class samting_in_libery(ABC):
    @abstractmethod
    def __init__(self, id:int, title:str, author:str, datePublication:date, status:bool):
        self.id = id
        self.title = title
        self.author = author
        self.datePublication = datePublication
        self.status = status

    def get_samting_in_libery(self):
        return self.title, self.author, self.datePublication, self.status

    def get_samting_in_libery(self):
        return self.title, self.author, self.datePublication, self.status

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_date_publication(self):
        return self.datePublication

    def get_status(self):
        return self.status

    def set_samting_in_libery(self, samting_in_libery):
        self.title = samting_in_libery.get_title()

    def set_id(self, id:int):
        self.id = id

    def set_title(self, title:str):
        self.title = title

    def set_author(self, author:str):
        self.author = author

    def set_date_publication(self, datePublication:date):
        self.datePublication = datePublication

    def set_status(self, status:bool):
        self.status = status