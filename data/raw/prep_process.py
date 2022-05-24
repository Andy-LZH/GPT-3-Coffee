import csv


def clean_lines(arr):
    country = arr[6]
    origin = arr[5]
    description = arr[9]
    description = description[:len(description)-2]
    if description == "Notes:":
        return -1

    else:
        return [country, origin, description]


if __name__ == "__main__":
    file = open("coffees_with_regions.csv")
    output_file = open("../processed/test.csv", 'w')
    writer = csv.writer(output_file)

    lines = file.readlines()[1:]
    writer.writerow(["prompt", "completion"])
    for i in lines:
        line = str.split(i, "\"|\"")
        data = clean_lines(line)
        if data != -1:
            writer.writerow([data[0] + ', ' + data[1], data[2]])

    file.close()
