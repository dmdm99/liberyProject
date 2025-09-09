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

    def get_all_about_object_in_libery(self):
        return self.__dict__

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