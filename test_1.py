from test_class_1 import Gemogramm

def main():
    sex = input("Введите пол пациента: ")
    hemoglobin = input("Введите показатель гемоглобина: ")
    erythrocytes = input("Введите показатель эритроцитов: ")
    reticulocytes = input("Введите показатель ретикулоцитов: ")
    thrombocytes = input("Введите показатель тромбоцитов: ")
    leukocyte = input("Введите показатель лейкоцитов: ")

    result = Gemogramm(sex, hemoglobin, erythrocytes, reticulocytes, thrombocytes, leukocyte)
    result.diagnosis_print()

if __name__ == '__main__':
    main()