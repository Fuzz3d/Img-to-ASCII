import ascii_magic 

image = input("Ruta de la imagen: ")
output = ascii_magic.from_image_file(image, columns=200,char="#")
ascii_magic.to_terminal(output)