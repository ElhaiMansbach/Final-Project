from datetime import date

from gender import Gender


class User:
    """This class present regested user in the system"""

    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        birth_date: date,
        mail: str,
        password: str,
        gender: int,
        is_admin: bool,
    ):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = birth_date
        self._mail = mail
        self._password = password
        self._gender = Gender(gender) or Gender(1)
        self._is_admin = is_admin or False
        self._allowed_to_vote = True

    def get_id(self):
        """
        Returns the user id

        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_id()
        123456789
        """
        return self._id

    def set_id(self, id: int):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_id(987654321)
        >>> user.get_id()
        987654321
        """
        self._id = id

    def get_first_name(self):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_first_name()
        'Ofir'
        """
        return self._first_name

    def set_first_name(self, first_name: str):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_first_name('Ovadia')
        >>> user.get_first_name()
        'Ovadia'
        """
        self._first_name = first_name

    def get_last_name(self):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_last_name()
        'Ovadia'
        """
        return self._last_name

    def set_last_name(self, last_name: str):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_last_name('Ofir')
        >>> user.get_last_name()
        'Ofir'
        """
        self._last_name = last_name

    def get_date_of_birth(self):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_date_of_birth()
        datetime.date(2000, 1, 1)
        """
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth: date):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_date_of_birth(date(2001,1,1))
        >>> user.get_date_of_birth()
        datetime.date(2001, 1, 1)
        """
        self._date_of_birth = date_of_birth

    def get_mail(self):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_mail()
        'example@mail.com'
        """
        return self._mail

    def set_mail(self, mail: str):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_mail('new_example@mail.com')
        >>> user.get_mail()
        'new_example@mail.com'
        """
        self._mail = mail

    def get_password(self):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_password()
        '123123'
        """
        return self._password

    def set_password(self, password: str):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_password('12341234')
        >>> user.get_password()
        '12341234'
        """
        self._password = password

    def get_is_admin(self) -> bool:
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_is_admin()
        False
        """
        return self._is_admin

    def set_is_admin(self, is_admin: bool) -> None:
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_is_admin(True)
        >>> user.get_is_admin()
        True
        """
        self._is_admin = is_admin

    def get_gender_value(self) -> int:
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_gender().name
        MALE
        >>> user.get_gender().value
        1
        """
        return self._gender.value

    def get_gender_name(self) -> str:
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_gender_name()
        MALE
        >>> user.get_gender_value()
        1
        """
        return self._gender.name

    def set_gender(self, new_gender: int):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.set_gender()
        >>> user.get_gender().name
        FEMALE
        >>> user.get_gender().value
        2
        """
        self._gender = Gender(new_gender)

    def get_allowed_to_vote(self):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_allowed_to_vote()
        True
        """
        return self._allowed_to_vote

    def set_allowed_to_vote(self, _allowed_to_vote: bool):
        """
        >>> user = User(123456789,'Ofir','Ovadia',date(2000,1,1),'example@mail.com','123123',Gender.MALE,False)
        >>> user.get_allowed_to_vote()
        True
        >>> user.set_allowed_to_vote(False)
        >>> user.get_allowed_to_vote()
        False
        """
        self._allowed_to_vote = _allowed_to_vote
