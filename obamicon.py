from PIL import Image

darkBlue = (0, 51, 76)
rojo = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

from PIL import Image
im = Image.open ("capamerica.jpg")
data = im.getdata()
data_list = list(data)

def colorize(image_data):
	new_pic = []
	
	for pixel in image_data:
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		intensity = red + green + blue
		if intensity < 182:
			new_pic.append(darkBlue)
		elif intensity < 364:
			new_pic.append(rojo)
		elif intensity < 546:
			new_pic.append(lightBlue)
		else:
			new_pic.append(yellow)
	return new_pic
			
new_data = colorize(data_list)

new_image = Image.new(im.mode, im.size)
new_image.putdata(new_data)
new_image.show()
new_image.save("output.jpg", "jpeg")
