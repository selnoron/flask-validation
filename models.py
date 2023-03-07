class User:
    """User for temp repository."""
    
    email: str
    old: int
    password: str
    password2: str

    @staticmethod
    def create(
        email: str,
        old: int,
        password: str,
        password2: str,
        address: str  # страна, город, район, улица, дом, квартира
    ) -> 'User':
        user: 'User' = User()
        user.email = email
        user.old = old
        user.password = password
        user.password2 = password2
        user.address = address
        user.validation()
        return user
    
    # 3 части - root@gmail.com
    def validation(self) -> bool:
        User.validation_email(self.email)
        User.validation_address(self.address)
        User.validation_age(self.old)
        User.validation_password(self.password)
        User.validation_password2(
            self.password, 
            self.password2
        )
        
    @staticmethod
    def validation_email(email: str):
        high_lvl_domain_pattern: tuple = (
            'net', 'com', 'kz', 'ru',
            'org', 'eu', 'cc', 'ua'
        )
        email_parts: list[str] = email.split('@')
        email_parts_by_point: list[str] = email.split('.')
        
        if (
            len(email_parts) != 2
        ) or (
            len(email_parts[0]) <= 2
        ) or (
            len(email_parts_by_point) != 2
        ) or (
            not email_parts_by_point[1] in high_lvl_domain_pattern
        ):
            raise ValueError(
                'Не верный email!'
            )
    
    @staticmethod
    def validation_address(address: str):
        try:
            address_parts: list[str] = address.split(', ')
            cities: list[str] = [
                "Актау",
                "Алматы",
                "Актобе",
                "Астана",
                "Атырау",
                "Караганда",
                "Костанай",
                "Павлодар",
                "Петропавловск",
                "Шымкент",
                "Уральск",
                "Усть-Каменогорск"
            ]

            if (
                len(address_parts) != 6
            ) or (
                address_parts[0] != "Kazakhstan"
            ) or (
                address_parts[1] not in cities
            ):
                raise ValueError(
                    'Не верный address!'
                )
        
            s_int1 = ''
            s_int2 = ''

            for i in address_parts[4]:
                if int(i) >= 0 and int(i) <= 9:
                    s_int1 += i

            for j in address_parts[5]:
                if int(j) >= 0 and int(j) <= 9:
                    s_int2 += i
            
            if s_int1 == '' or s_int2 == '':
                raise ValueError(
                    'Не верный address!'
                )
        except:
            raise ValueError(
                'Не верный address!'
            )
            
    
    @staticmethod
    def validation_age(age: int):
        if (
            type(age) == str
        ) or (
            age <= 14
        ) or (
            age >= 120
        ):
            raise ValueError(
                'Не верный age!'
            )

    @staticmethod
    def validation_password(pas: int):
        spec: str = "!@#$%^&*()_+=-"
        if len(pas) <= 4:
            raise ValueError(
                'Не верный password!'
            )

        for i in pas:
            if (i in spec):
                raise ValueError(
                'Не верный password!'
            )
    
    @staticmethod
    def validation_password2(pas: int, pas2: int):
        if (
            pas != pas2
        ):
            raise ValueError(
                'Не верный password2!'
            )
        

    
a = User.create(
    email="root@mail.ru",
    old=16,
    password="qwerty",
    password2="qwerty",
    address="Kazakhstan, Караганда, ajhif, djkdj, 2, 132"
)
print(a.email)