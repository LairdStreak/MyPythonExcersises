""" https://www.codementor.io/kishanmehta/how-to-handle-switch-case-in-python-pj7q08bjj """

car_name_and_colors = {
  'ford': ['red', 'black', 'white', 'silver', 'gold'],
  	'audi': ['black', 'white'],
  	'volkswagon': ['purple', 'orange', 'green'],
  	'mercedes': ['black'],
}

def main():
    print(get_car_color('volvo'))

def get_car_color(car):
    return car_name_and_colors.get(car, 'red')



if __name__ == "__main__":
    main()