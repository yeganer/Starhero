import random
import numpy as np

def RGBToHTMLColor(R, G, B):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % (R, G, B)
    # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor


def get_sphere_aframe(data):
    string = "<a-entity>\n"
    hexcolor = RGBToHTMLColor(data.R, data.G, data.B)
    string += "<a-sphere position=\"{} {} {}\" radius=\"{}\" opacity=\"0\" color=\"{}\">\n".format(
        data.x, data.y, data.z, data.radius, hexcolor)
    string += "<a-animation begin=\"{}\" dur=\"{}\" attribute=\"material.opacity\" fill=\"none\" from=\"0\" to=\"1\" repeat=\"1\" direction=\"alternate\"></a-animation>\n".format(
        data.start, data.duration)
    string += "<a-animation begin=\"{}\" dur=\"{}\" attribute=\"radius\" fill=\"both\" from=\"0.01\" to=\"{}\" repeat=\"1\" direction=\"alternate\"></a-animation>\n".format(
        data.start, data.duration, data.radius)
    string += "</a-sphere></a-entity>"
    print(string)
    return


class crap:
    def __init__(self):
        self.x = random.uniform(-100, 100)
        self.y = random.uniform(-100, 100)
        self.z = random.uniform(-100, 100)
        self.radius = 5
        self.R = 255
        self.G = 185
        self.B = 35
        self.start = random.uniform(1000, 10000)
        self.duration = random.uniform(1000, 10000)
        return

# A = crap()
# points = 500
# data = []
# for i in range(points):
#	A = crap()
#	data.append(A)
#	get_sphere_aframe(A)
# fileData = open("closest_stars.csv", "r")


class star:
    def __init__(self, line):
        d = line.split(',')
        self.name = d[1]
        self.RA = float(d[2])
        self.DEC = float(d[3])
        #self.vmag = float(d[4])
        
        try:
            self.dist = float(d[5])
        except ValueError:
            print('Skipped one star due to strange distance value')
            self.dist = -1

        self.radius = 1
        self.x = 1
        self.y = 1
        self.z = 1

        if self.dist == -1:
            return
        else:
            self.getCoordinates()
            return

    def printStuff(self):
        print(self.name, self.dist)
        return

    def getCoordinates(self):
        self.x = self.dist*np.sin(self.RA)*np.cos(self.DEC)
        self.y = self.dist*np.sin(self.RA)*np.sin(self.DEC)
        self.z = self.dist*np.cos(self.RA)
        return

    def printAframe(self, verbose=False):
        string = "<a-sphere position='{} {} {}' scale='{} {} {}'  src='https://cdn.glitch.com/0cd1fbdb-63f9-41ba-8fa9-a2fd321a956f%2Fmercury.jpg?1504965277967'></a-sphere>".format(self.x, self.y, self.z, self.radius, self.radius, self.radius)
        if verbose:
            print(string)
        return string


stars = []
i=0

# get all star data
with open('closest_stars.csv', 'r') as f:
    for line in f:
        if(i != 0):
            stars.append(star(line))
        i+=1

# put all star data into a file, in the correct html format
FILE = 'star_coords.html'
with open(FILE, 'w') as outfile:
    for I in stars:
        html_string = I.printAframe(verbose=False)
        outfile.write(html_string)
