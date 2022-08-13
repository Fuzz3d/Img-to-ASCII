# Img-to-ASCII
Este script es capaz de convertir cualquier imagen a formato ASCII, en muy pocas líneas de código. 

```python
import ascii_magic 
image = input("Ruta de la imagen: ")
output = ascii_magic.from_image_file(image, columns=200,char="#")
ascii_magic.to_terminal(output)
```
