# Shapesafari

## Introduction
Shapesafari is a didactic CAD application for children and young people, which is intended to help them gain access to digital manufacturing processes such as 3D printing, as well as digital design. It is intended as an educational software that provides an understanding of the design principles of CAD.

## The Goal
Growing environmental problems and scarcity of resources require a different approach to goods, consumption and production. Since this cannot be solved by sustainable materials alone, a new understanding of products and consumption is necessary. In today's society, consumers are becoming more and more prosumers. With a high demand for sustainability, they enable repairs, recycling processes and decentralized production from the middle of society. This ranges from reverse engineering of components and rapid prototyping of spare parts to small-scale production of new designs. CAD programs are an indispensable tool for this, and education and technical understanding are a prerequisite for participation in this process. Children and young people are shaping our world of tomorrow. If we introduce them to design tools at an early age, they will also perceive our world as something they can shape in the future. By providing didactic access to digital construction tools, Shapesafari not only enables them to participate technologically. It also changes their understanding of what we consider analog and digital, what we consider static and changeable, so that in the future more people can shape our world for the better.

## The Addon 
Children and young people can collaboratively create 3D models on the computer by drawing, tinkering and experimenting by hand in front of the computer. In the process, Shapesafari teaches the basic principles of established design programs and fosters a sense of proportion and practicality in designs. What is special about Shapesafari is its special analog/digital interface. With it, part of the work process is shifted in front of the screen. The virtual working environment of the program is projected onto a screen with the help of a projected onto a screen. As in shadow theaters, the children now cast shadows onto the screen and thus into the work environment. They can experiment with found objects, their hands or specially made stencils.
![Schema_small](https://github.com/lcsdmnn/Shapesafari/assets/103833835/615362c5-5d93-4da9-a22f-fc5e5b26bfb2)
CAD software can be classified according to their design principles. Shapesafari is based on the so-called solid modeling. Here geometric objects are described as solids and not just their shells as surfaces. When creating geometries with the help of solid modelers, a sketch is made at the beginning of the work process. This sketch must represent a surface and must therefore be closed. Through various transformations such as extrusion, rotation or lofting, the sketches/surfaces can be further developed into three-dimensional shapes. Shapesafari focuses on teaching this transformation process from two-dimensional to three-dimensional form.
![praesentation_neu_219](https://github.com/lcsdmnn/Shapesafari/assets/103833835/6fae06a0-3683-47ce-88c9-ab293ac1a5ad)


## How to use it

Shapesafari is a Blender addon. To use it, it requires Blender, a webcam and a projector. The camera must be aligned in such a way that it has the entire projection of the projector in its field of view. It must be positioned to pick up the shadows and the projection, but not the objects that serve the projection. 

### Calibrate
Every time you restart Shapesafari or move either the camera or the projector you have to calibrate the program. This is to compensate for the perspective distortion with which the camera captures the projection. Click on Calibrate. Make sure that the camera captures the projection entirely and as centered as possible.

### Image
The working process of Shapesafari starts with casting a shadow into the projection of the beamer. You can use your hands, your body, found objects or specially made stencils. Be creative! If you like the shadow you can bring it into the program with the "Image" button. Then it will be a two-dimensional mesh surface in the virtual space at the place you cast it.
![image](https://github.com/lcsdmnn/Shapesafari/assets/103833835/941139c5-3dbd-46f8-bba9-6b8b0750fbd4)


### Erase
If you want to remove something from the surface, for example because the camera has captured the shadow of your hand holding a stencil, you can do that with the Eraser function. Click on the button and draw a rectangle with the mouse where you want to remove something from the mesh.
![erase](https://github.com/lcsdmnn/Shapesafari/assets/103833835/51b71203-6a02-424e-b323-e350e1c3cfb9)


### Transform
Now you can make the surface a solid. You can extrude, rotate or loft it. Use the corresponding buttons to do this.
![transform](https://github.com/lcsdmnn/Shapesafari/assets/103833835/cf014956-f99d-4a0f-be33-545b3579af59)


### Bool
The resulting solids can be related to each other. They can be united, subtracted from each other, or the part can be maintained by intersecting.

![bool](https://github.com/lcsdmnn/Shapesafari/assets/103833835/aa22daa0-bfae-4442-9c0c-deec720a1844)



## Installation
In order to use Shapesafari, the OpenCV library must be installed before installing Shapesafari. This is a cross-platform program library that is used for image processing.

### Linux:
For manjaro with Blender installed from the package manager
* python3 -m ensurepip
* python3 -m pip install --upgrade pip --user
* python3 -m pip install opencv-contrib-python numpy --user

### MacOS:
* cd /Applications/Blender.app/Contents/Resources/2.81/python/bin
* ./python3.7m -m ensurepip
* ./python3.7m -m pip install --upgrade pip --user
* ./python3.7m -m pip install opencv-contrib-python numpy --user

### Windows:
Open Command Prompt as Administrator
* cd "C:\Program Files\Blender Foundation\Blender 2.81\2.81\python\bin"
* python -m pip install --upgrade pip
* python -m pip install opencv-contrib-python numpy

### Shapesafari:
Open Blender as Administrator
* Go to **Edit > Preferences > Add-ons > Install**.
* Search for the file Shapesafari.zip in the location where you saved it and install it.
* Search for Shapesafari at **Edit > Preferences > Add-ons > Searchbar**
* Click on the enable checkbox. 


## License
The Shapesafari source code is released under the GPL 3.0

## Special Thanks
Special thanks to the Prototype Fund and the entire Prototype Fund team. In addition, special thanks goes to the DLR and their team.

## Funding
The project was funded by the German Federal Ministry of Education and Research under grant number 01IS23S2 from March to August 2023. The author is responsible for the content of this publication.


![bmbf_eng](https://github.com/lcsdmnn/Shapesafari/assets/103833835/b3548c1d-4c04-440d-893e-6401de5d6112) ![PrototypeFund-P-Logo_small](https://github.com/lcsdmnn/Shapesafari/assets/103833835/6a73f85b-5b24-45ef-b8f3-e0b4232dd34c)



