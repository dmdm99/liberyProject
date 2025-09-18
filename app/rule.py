class rule(object):
    book_time = 21
    Ebook_time = 14
    Magazine_time = 7

    def __init__(self):
        self.book_time = self.Ebook_time
        self.Ebook_time = self.Magazine_time
        self.Magazine_time = self.book_time

    def get_book_time(self):
        return int(self.book_time)

    def get_Ebook_time(self):
        return int(self.Ebook_time)

    def get_Magazine_time(self):
        return int(self.Magazine_time)

    def set_book_time(self, book_time):
        self.book_time = book_time

    def set_Ebook_time(self, Ebook_time):
        self.Ebook_time = Ebook_time

    def set_Magazine_time(self, Magazine_time):
        self.Magazine_time = Magazine_time