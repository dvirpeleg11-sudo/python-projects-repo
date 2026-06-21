from cyberEducationDigitalBooks.pythonBook.oppExcersises.student import Student


def main():
    student = Student("dvir", 17, True)
    student._age = 6  # Works, but breaks convention!
