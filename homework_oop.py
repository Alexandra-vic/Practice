class Contact:
    def __init__(self, ID, first_name, last_name, day, month, year, profession):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.day = day
        self.month = month
        self.year = year
        self.profession = profession

    def get_information(self):
        return f'ID - {self.ID}, \nFull name - {self.first_name} {self.last_name}, \nBirth Date - {self.day}.{self.month}.{self.year} , \nProfession - {self.profession}\n '

c = Contact('1','John', 'Dow', '21', '04', '1996', 'python developer')
print(c.get_information())

new = Contact('2', 'Kate', 'Win', '07', '11', '2000', 'manager')
print(new.get_information())
