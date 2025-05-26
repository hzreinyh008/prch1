import cv2
def display_menu():
    print("\nВыбери действие: 1 - показать список молекул, 2 - удалить молукулу, 3 - показать молекулу трехмерной структуры, 4 - показать гибридизацию молекулы, 5 - геометрия молекулы, 6 - показать геометрию молекулы, 7 - показать число неподеленных электронных пар (НЕП), 0 - выход")

    choice = input("Введи номер действия: ")


    return choice

def show_molecules(molecule_list):
    if not molecule_list:
        print("Список молекул пуст")
    else:
        print("Список молекул:")
        for i, molecule in enumerate(molecule_list):
            print(f"{i}. {molecule}")

def get_molecule_title():
    return input("Введи название молекулы: ")

def get_molecule_index():
    return input("Введи индекс молекулы для удаления: ")

def show_molecule(molecule_name):

    molecule_name = molecule_name.lower() + ".jpg"

    img = cv2.imread("./mol_list/" + molecule_name)
    cv2.imshow("Molecule", img)
    key = cv2.waitKey(0)

    if key == ord("0"):
        cv2.destroyWindow("Molecule")

def show_gm_molecule(molecule_name):

    molecule_name = molecule_name.lower() + ".jpg"

    img = cv2.imread("./mol_gm/" + molecule_name)
    cv2.imshow("Molecule", img)
    key = cv2.waitKey(0)

    if key == ord("0"):
        cv2.destroyWindow("Molecule")



def show_message(message):
    print(message)
