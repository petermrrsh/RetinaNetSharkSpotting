
  
# Using readlines()
#files = ["9716", "9722", "9746"]
files = ["9676"]
csv_lines = []
PIXELS_X = 3840
PIXELS_Y = 2160
folder_name="validation_images"
output_name="validation.csv"
  
count = 0
for file in files:
    annotations = open("{}/{}.txt".format(folder_name, file), 'r')
    Lines = annotations.readlines()
    # Strips the newline character
    for line in Lines:
        words = line.split(" ")
        words[0] = "{}/{}.png".format(folder_name, file)

        x1 = float(words[1]) * PIXELS_X
        y1 = float(words[2]) * PIXELS_Y
        x2 = x1 + float(words[3]) * PIXELS_X
        y2 = y1 + float(words[4]) * PIXELS_Y

        words[1] = str(round(x1))
        words[2] = str(round(y1))
        words[3] = str(round(x2))
        words[4] = str(round(y2))

        words.append("shark")
        csv_lines.append(",".join(words))

print(csv_lines)
file1 = open(output_name, 'w')
file1.writelines("\n".join(csv_lines))
file1.close()


