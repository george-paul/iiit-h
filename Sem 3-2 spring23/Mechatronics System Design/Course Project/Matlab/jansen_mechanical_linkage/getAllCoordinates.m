function [Storage_Coordinates] = getAllCoordinates(N,S,L)
%[Storage_Coordinates] = getAllCoordinates(N, S):
%Calculates all the coordinates of each of the nodes of the Jansen Linkage
%model for each of the angles(which have already been calculated) and
%stores them in a matrix.
%Input N = the number of crank angles used(which will give the same number
%of coordinates for each node)
%Input S = matrix of all the angles
%Input L = matrix of all the lengths of the Jansen structure
%Output Storage_Coordinates = matrix of all the coordinates for each node

%Version 1: Created 06/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to calculate and store all of the
%coordinates Jansen Linkage Model

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 3), error('Incorrect number of input arguments.'); end

%Creating an empty matrix to store all of the coordinates in
S_Coordinates = zeros(N,16);

%Placing the fixed values in first (0,0) (-38,-7.8)
S_Coordinates(:,1) = 0;
S_Coordinates(:,2) = 0;
S_Coordinates(:,3) = -38;
S_Coordinates(:,4) = -7.8;

%Finding the coordinate i
[Y1,Z1] = getCoordinate(0, 0, L(1), S(:,1));
S_Coordinates(:,5) = Y1;
S_Coordinates(:,6) = Z1;

%Finding the coordinate j
[Y1,Z1] = getCoordinate(Y1, Z1, L(2), S(:,2));
S_Coordinates(:,7) = Y1;
S_Coordinates(:,8) = Z1;

%Finding the coordinate k
[Y1,Z1] = getCoordinate(S_Coordinates(:,3), S_Coordinates(:,4), L(4), S(:,4));
S_Coordinates(:,9) = Y1;
S_Coordinates(:,10) = Z1;

%Finding the coordinate l
[Y1,Z1] = getCoordinate(Y1, Z1, -L(8), S(:,8));
S_Coordinates(:,11) = Y1;
S_Coordinates(:,12) = Z1;

%Finding the coordinate m
[Y1,Z1] = getCoordinate(Y1, Z1, -L(9), S(:,9));
S_Coordinates(:,13) = Y1;
S_Coordinates(:,14) = Z1;

%Finding the coordinate n
[Y1,Z1] = getCoordinate(Y1, Z1, -L(11), S(:,11));
S_Coordinates(:,15) = Y1;
S_Coordinates(:,16) = Z1;

%Assigning the matrix S to output, Storage_Coordinates
Storage_Coordinates = S_Coordinates;

%Error Checking: To ensure corrent number of values being outputted
if (nargout ~= 1), error('An incorrect number of elements are being returned'); end

end

