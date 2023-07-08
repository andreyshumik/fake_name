from russian_names import RussianNames
import openpyxl


def generate_name():
    return RussianNames().get_person().split()
    
 
if __name__ == "__main__":
    number = int(input('Vvedite chislo imen: '))
    book = openpyxl.Workbook() #создание книги эксель
    sheet = book.active

    for i in range(number):
        sheet.append([i]+generate_name())
    
    book.save('555.xlsx')