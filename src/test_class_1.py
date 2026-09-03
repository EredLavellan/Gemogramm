from tabulate import tabulate

class Gemogramm:
    normal_indicators = {'hemoglobin':
                             {'male': '130-160',
                              'female': '120-140'
                              },
                         'erythrocytes':
                             {'male': '4-5.1',
                              'female': '4-5.2'
                              },
                         'color_indicator': '0,8-1.15',
                         'reticulocytes': '0.2-1.2',
                         'thrombocytes': '180-320',
                         'leukocyte': '4-9',
                         'neutrophils':
                             {'band neutrophils': '1-6',
                              'segmented neutrophils': '47-72'
                             },
                         'eosinophils': '0.5-5',
                         'basophils': '0-1',
                         'lymphocytes': '17-30',
                         'monocytes': '4-11'
                         }
    list_of_indicators = ['hemoglobin', 'erythrocytes', 'color_indicator', 'reticulocytes', 'thrombocytes', 'leukocyte']
    headers = ['Indicator', 'Value', 'Normal_value']

    def __init__(self, sex, hem, ery, ret, tro, leu):
        self.gender = sex
        self.hemoglobin = hem
        self.erythrocytes = ery
        self.reticulocytes = ret
        self.thrombocytes = tro
        self.leukocyte = leu
        self.anemia_exists = self.anemia_exists_check()
        self.anemia_chrom_definition = self.color_indicator_calculation()
        self.anemia_reg_definition = self.regeneration_check()
        self.anemia_text = self.anemia_definition()
        self.leukocyte_definition = self.leukocyte_check()

    def anemia_exists_check(self) -> bool:
        try:
            if self.gender == 'male' and int(self.hemoglobin) < 130:
                return True
            elif self.gender == 'female' and int(self.hemoglobin) < 120:
                return True
            else:
                return False
        except ValueError:
            return False

    def anemia_definition(self):
        list_anemia = []
        if self.anemia_exists:
            list_anemia.append('анемия')
            if self.reticulocytes != '':
                list_anemia.append(self.anemia_reg_definition)
            if self.erythrocytes != '':
                list_anemia.append(self.anemia_chrom_definition)
                return list_anemia
            return list_anemia
        else:
            return None

    def color_indicator_calculation(self):
        try:
            index = float(self.hemoglobin) / float(self.erythrocytes) * 0.03
            if index < 0.8:
                list_chrom = 'гипохромная'
                return list_chrom
            elif index > 1.05:
                list_chrom = 'гиперхромная'
                return list_chrom
            else:
                list_chrom = 'нормохромная'
                return list_chrom
        except ValueError:
            return None

    def regeneration_check(self):
        try:
            if 1.5 < float(self.reticulocytes) < 5.0:
                list_reg = 'Регенераторная'
                return list_reg
            elif 5.0 < float(self.reticulocytes):
                list_reg = 'Гиперрегенераторная'
                return list_reg
            elif 0.2 < float(self.reticulocytes) < 1.5:
                list_reg = 'Гипорегенераторная'
                return list_reg
            else:
                list_reg = 'Арегенераторная'
                return list_reg
        except ValueError:
            return None

    def thrombocytes_check(self):
        try:
            if int(self.thrombocytes) > 320:
                return 'Тромбоцитоз'
            elif int(self.thrombocytes) < 180:
                return 'Тромбоцитопения'
            else:
                return 'Тромбоциты в норме'
        except ValueError:
            return 'Нет данных'

    def diagnosis_print(self):
        print('Диагноз:')
        anemia_list = self.anemia_text
        try:
            if len(anemia_list) == 1:
                print(f'{anemia_list[0]}')
            elif len(anemia_list) == 2:
                print(f'{anemia_list[1].title()} {anemia_list[0]}')
            elif len(anemia_list) == 3:
                print(f'{anemia_list[1].title()} {anemia_list[2]} {anemia_list[0]}')
        except TypeError:
            print(f"Анемии нет")
        print(self.thrombocytes_check())
        print(self.leukocyte_definition)

    def get_diagnosis_string(self):
        result = ''
        anemia_list = self.anemia_text
        try:
            if len(anemia_list) == 1:
                result += f"{anemia_list[0]}\n"
            elif len(anemia_list) == 2:
                result += f"{anemia_list[1].title()} {anemia_list[0]}\n"
            elif len(anemia_list) == 3:
                result += f"{anemia_list[1].title()} {anemia_list[2]} {anemia_list[0]}\n"
        except TypeError:
            result += "Анемии нет\n"

        result += self.thrombocytes_check() + "\n"
        result += self.leukocyte_definition
        return result


    def leukocyte_check(self):
        try:
            if int(self.leukocyte) < 4:
                leukocyte_status = 'Лейкопения'
                return leukocyte_status
            elif int(self.leukocyte) > 9:
                leukocyte_status = 'Лейкоцитоз'
                return leukocyte_status
            else:
                leukocyte_status = 'Уровень лейкоцитов в норме'
                return leukocyte_status
        except ValueError:
            leukocyte_status = 'Нет данных'
            return leukocyte_status
