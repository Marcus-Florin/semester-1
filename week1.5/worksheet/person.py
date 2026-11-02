# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self,name,birth):
        """
        A Person, with a name and a date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("Name needs to be a string.")

        if name == "":
            raise ValueError("Name requires a value.")

        if not isinstance(birth, date):
            raise TypeError("Date of birth needs to be a date.")

        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns person's name's initials in upper case.
        """
        name_split = self.name.split()

        initials = ""

        for name in name_split:
            initials += name[0]

        return initials.upper()

    def is_birthday(self):
        """
        Checks if today is the person's birthday, returns true if yes.
        """
        x = date.today()

        if self.birth.day == x.day and self.birth.month == x.month:
            return True

        return False