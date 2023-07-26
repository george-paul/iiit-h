# JansenMechanicalLinkage

The project aims at modelling the mechanism of the Jansen's Linkage given the distances of each of the joints, then simulating the mechanism for a particular number of angles that makes up a full revolution for the crank shaft and finally visualising the model by employing a number of MATLAB's functions. My visualistaion can be seen in the following link: (https://youtu.be/71Gi_qTGmU8).

## Table of Contents

Installation

Usage

Contributing

Credit

License

## Installation

To run my project you will need to download all the files and have MATLAB installed on your computer. The version of MATLAB I used was R2016b.

## Usage

The project was organised so that all functions are called from just running the interface (JansenInterface.m). Within this interface, you will be able to see a matrix L that is made up of all the lenghts of the joints. The variable N can be adjusted as you wish. I left it at 250 angles per revoultion which I felt gave a nice, smooth implementation. To reduce the length of time it takes to create the .avi video file, reduce the value of N to what suits you.

In terms of developing my project further, there is a lot of work that could be undertaken in draw files (drawAllLinks.m, drawJansen.m etc) to improve the visualisation. The functions that get the angles between all the joints can be left alone.

Running JansenInterface.m will begin calling all the functions, creating matrices to store all the angles and creating the visualisation.

## Contributing

If you want to contribute to this project, I would suggest beginning with the visualisation as the modelling and simulation are complete but improvement can be made with visualisation.

## Credit

Author: David Gormley

Credit is given to Ms. Anna McCann for her assistance with the visualisation.

## License

This project is licensed under the terms of MIT license.

