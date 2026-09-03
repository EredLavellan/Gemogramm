from example_1 import Gemogramm

def main():
    border = '-' * 50
    while True:
        print(border)
        sex = input("Введите пол: ").title()
        gemoglobin = int(input("Введите показатель гемоглобина: "))
        eritrocit = float(input("Введите показатель эритроцитов: "))
        reticul = float(input("Введите показатель ретикулоцитов: "))
        tromb = int(input("Введите показатель тромбоцитов: "))

        result = Gemogramm(sex, gemoglobin, eritrocit, reticul, tromb)
        print(f"Диагноз:\n{result.diagnose}")

if __name__ == '__main__':
    main()