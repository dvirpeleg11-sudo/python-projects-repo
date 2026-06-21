# from cyberEducationDigitalBooks.pythonBook.oppExcersises.plane import Plane
import plane


def main():
    plane_obj = plane.Plane("best plane")
    plane_obj.update_position()

    x_value, y_value = plane_obj.get_position()
    # there is no private in python. it only hides the data member.
    plane_obj._Plane__x = 2
    print("x value: {}.\ny value: {}.".format(plane_obj.get_position()[0], plane_obj.get_position()[1]))
    print(plane_obj.__str__())
    print("method of our {} object:\n {}.".format(plane_obj.__class__, dir(plane_obj)))


if __name__ == "__main__":
    main()
