import cv2
from sklearn.cluster import KMeans

def importimage(filename):
    return cv2.imread(filename)

def processimage(image):
    ##Convert image into the RGB space
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ##Resize into x by 3
    img = img.reshape((img.shape[0] * img.shape[1],3)) 

    return img

def findcolour(image, clusters):
    ##Create KMeans model with desired clusters
    km = KMeans(n_clusters=clusters)
    model = km.fit(image)

    ##Return labels used to define clusters (RGB value)
    return model.cluster_centers_

def distance(c1, c2):

    distance = 0

    ##Standard Euclidean Distance
    for i in range(3):
        distance += ((c1[i] - c2[i])**2)

    return distance**(1/2)


def checkcolour(rgb, comparison=[]):
    
    if comparison == []:
    ##Define comparison base colours if none is passed.
    ##Expected benchmark RGB values should be passed for accuracy.
        comparison = {
            "blue": [0,0,225],
            "red": [255,0,0],
            "green" : [0,128,0],
            "yellow": [255,255,0],
            "purple": [128,0,128],
            "white": [255,255,255],
            "black": [0,0,0],
            "orange": [255,165,0]
            }

    ##Calculate distance between rgb value and baseline
    for c in comparison:
        comparison[c] = distance(rgb, comparison[c])

    return comparison