from PIL import Image
from sentence_transformers import SentenceTransformer, util

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open("29-08-23-GNX.png")

myconfig = r"--psm 3 --oem 3"
text = pytesseract.image_to_string(image, config='myconfig')

print('\nTexto capturado de la imagen: \n')
print(text)

lines_array = text.splitlines()
print('\nTexto ordenado en una lista: \n')
print(lines_array)

# Lista de usuarios GNX actual
array_users = ['alvaro.ruiz', 'aaron.ramos', 'augusto.munoz', 'axel.carhuatocto', 'christopher.carrillo', 'edwin.romero', 'eloy.damian', 'francisco.leiva', 'hans.arancibia', 'jesus.franco', 'johnny,arango', 'john.candia', 'jose.tacuri', 'juan.montalvo', 'larry.quiroz', 'norma.vega', 'pedro.pena', 'ronald.yanqui', 'ruben.ursua', 'santos.taica', 'sinthia.venialgo', 'waldo.huertas', 'ytalo.cortez', 'edward.ruiz']

# model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
# model = SentenceTransformer('all-mpnet-base-v2')
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

print('\nResultado de la comparación entre los arrays que han cumplido con el mínimo porcentaje de similitud (36%): \n')

for valueImg in lines_array:
    e1 = model.encode('agfsd', convert_to_tensor=True)
    e2 = model.encode('mnb', convert_to_tensor=True)
    maxcosine = util.pytorch_cos_sim(e1, e2)
    maxValueImg = ''
    maxValueGNX = ''
    validateEntrance = False

    for valueGNX in array_users:
        embedding1 = model.encode(valueImg, convert_to_tensor=True)
        embedding2 = model.encode(valueGNX, convert_to_tensor=True)

        cosine_sim = util.pytorch_cos_sim(embedding1, embedding2)

        if (cosine_sim >= 0.36):  #0.37 funca con la foto del 28
            validateEntrance = True
            if (cosine_sim >= maxcosine):
                maxcosine = cosine_sim
                maxValueImg = valueImg
                maxValueGNX = valueGNX
    if (validateEntrance == True):
        print(maxValueImg)
        print(maxValueGNX)
        print("BERT Cosine Similarity:", maxcosine.item())
        print("\n")