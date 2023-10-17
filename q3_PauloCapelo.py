from PIL import Image

input_image = Image.open('input.jpg') #EXEMPLO DE INPUT, VOCÊ PODERIA TROCAR E ADICIONAR O ARQUIVO CORRESPONDENTE

brightness = float(input("Enter the brightness adjustment value (between -1.0 and 1.0): "))

brightness = max(-1.0, min(1.0, brightness))

adjusted_image = Image.eval(input_image, lambda x: x + int(255 * brightness))

adjusted_image.save('output.jpg')

print("Image with brightness adjustment saved successfully!")
