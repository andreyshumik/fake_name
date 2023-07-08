from russian_names import RussianNames
import openpyxl


def generate_name():
    a = RussianNames().get_person().split()
    return [a[1],a[0],a[2]]

def XLSX(number):
    book = openpyxl.Workbook() #создание книги эксель
    sheet = book.active
    sheet.append(['Номер','Фамилия','Имя','Отчество'])
    for i in range(number):
        sheet.append([i+1]+generate_name())
    
    book.save('555.xlsx')

    
 
if __name__ == "__main__":
    number = int(input('Vvedite chislo imen: '))
    XLSX(number)