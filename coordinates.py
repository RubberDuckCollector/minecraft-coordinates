import json

def make_coords():
    with open("coords.txt", "a") as f:

        coords = {}

        x = int(input("Enter x coordinate: "))
        coords["X"] = x

        y = int(input("Enter y coordinate: "))
        coords["Y"] = y

        z = int(input("Enter z coordinate: "))
        coords["Z"] = z


        description = input("Enter description: ")
        coords["description"] = description

        coords = json.dumps(coords)
        
        f.write(f"{coords}\n")

def show_coords():

    with open("coords.txt", "r") as f:
                
        file_length = f.readlines()
        length = len(file_length)
        f.close()

    with open("coords.txt", "r") as f:

        for i in range(length):
            content = f.readline()
            data = json.loads(content)

            print()
            print(f"{json.dumps(data, indent=2)}")
            print()


def edit_mode():

    def read_coords():
        with open("coords.txt", "r") as f:
            coords = []
            for line in f:
                coords.append(json.loads(line.strip()))
            return coords

    def write_coords(coords):
        with open("coords.txt", "w") as f:
            for coord in coords:
                f.write(json.dumps(coord) + "\n")

    def edit_coords(coords):
        for i, coord in enumerate(coords):
            print(f"Coordinate {i + 1}:")
            print(f"X: {coord['X']}")
            print(f"Y: {coord['Y']}")
            print(f"Z: {coord['Z']}")
            print(f"Description: {coord['description']}")
            print("")

            choice = input("Enter 'e' to edit this coordinate, or enter any other key to continue: ")
            if choice == 'e':
                x = int(input("Enter x coordinate: "))
                coord["X"] = x

                y = int(input("Enter y coordinate: "))
                coord["Y"] = y

                z = int(input("Enter z coordinate: "))
                coord["Z"] = z

                description = input("Enter description: ")
                coord["description"] = description
    
    coords = read_coords()
    edit_coords(coords)
    write_coords(coords)

def main():
    
    while True:

        make_edit_show = input("Make, edit, or show coordinates? (m/e/s) > ").lower().replace(" ", "")
        
        if make_edit_show == "m":
            make_coords()
        elif make_edit_show == "e":
            edit_mode()
        elif make_edit_show == "s":
            show_coords()
        elif make_edit_show == "done":
            break



if __name__ == '__main__':
    main()
