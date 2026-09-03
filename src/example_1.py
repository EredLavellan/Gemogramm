class Gemogramm:
    def __init__(self,sex, gem, eri, ret, tromb):
        self.sex = sex
        self.gem = gem
        self.eri = eri
        self.ret = ret
        self.tromb = tromb
        self.anemia_status = self.anemia_check(self.sex, self.gem)
        self.color_grade_status = self.color_grade(self.gem, self.eri)
        self.regeneration = self.regeneration_check(self.ret)
        self.tromb_status = self.tromb_check(self.tromb)
        self.diagnose = self.diagnose_print(self.anemia_status,self.color_grade_status, self.regeneration, self.tromb_status)

    def anemia_check(self, sex, gem) -> str:
        if sex == 'М':
            if gem < 130:
                return 'анемия'
            elif gem > 160:
                return 'Уровень выше нормы'
            else:
                return 'Гемоглобин в норме'
        elif sex == 'Ж':
            if gem < 120:
                return 'анемия'
            elif gem > 140:
                return 'Уровень выше нормы'
            else:
                return 'Гемоглобин в норме'
        else:
            return 'Неправильно указан пол пациента'

    def color_grade(self, gem, eri) -> str:
        index = float(gem/eri * 0.03)
        if index < 0.85:
            return 'гипохромная'
        elif index > 1.05:
            return 'гиперхромная'
        else:
            return 'нормохромная'

    def diagnose_print(self, anemia_status, color_grade_status, regeneration, tromb_status) -> str:
        if anemia_status == 'анемия':
            return f'{regeneration} {color_grade_status} {anemia_status}\n{tromb_status}'
        elif anemia_status == 'Уровень выше нормы':
            return f'Высокий уровень гемоглобина\n{tromb_status}'
        elif anemia_status == 'Гемоглобин в норме':
            return f'Показатели в норме\n{tromb_status}'
        else:
            return f'{anemia_status}\n{tromb_status}'

    def regeneration_check(self, ret) -> str:
        if 1.5 < ret < 5.0:
            return 'Регенераторная'
        elif 5.0 < ret:
            return 'Гиперрегенераторная'
        elif 0.2 < ret < 1.5:
            return 'Гипорегенераторная'
        else:
            return 'Арегенераторная'

    def tromb_check(self, tromb) -> str:
        if tromb > 320:
            return 'Тромбоцитоз'
        elif tromb < 180:
            return 'Тромбоцитопения'
        else:
            return 'Тромбоциты в норме'