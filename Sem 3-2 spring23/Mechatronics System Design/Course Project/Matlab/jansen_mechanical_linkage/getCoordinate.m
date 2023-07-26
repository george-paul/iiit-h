function [Y1,Z1] = getCoordinate(Yo,Zo,len,theta)
%[X1, Y1] = getCoordinate(Xo,Yo,len,theta):
%Calculates the coordinates based on starting point(Yo,Zo), the length from
%that point to a coordinate raised by an angle of theta above the positive
%y axis.
%Input Yo,Zo = coordinates of starting point on the y-z axis
%Input len = length
%Input theta = angle above the positive y-axis
%Output Y1,Z1 = outputs the actual coordinates of the desired point

%Version 1: Created 05/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to calculate the coordinates.

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 4), error('Incorrect number of input arguments.'); end

Y1 = Yo + len*cos(theta);
Z1 = Zo + len*sin(theta);

%Error Checking: To ensure corrent number of values being outputted
if (nargout ~= 2), error('An incorrect number of elements are being returned'); end

end

