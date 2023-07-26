%=========================================================================%
%Project: Simulation of Jansen Mechanical Linkage model.
%Author: David Gormley
%Date: 13/03/17
%Version 1 (13/03/17)
%=========================================================================%

clear all;
close all;

%=========================================================================%
%Internal Parameters

%Fixed lengths of each of the links of the Jansen model. Placing it in the
%interface so as not to have to rewrite the lengths in each function
L_0i = 15;
L_ij = 50;
L_1j = 41.5;
L_1k = 40.1;
L_kj = 55.8;
L_m1 = 39.3;
L_mi = 61.9;
L_lk = 39.4;
L_ml = 36.7;
L_nl = 65.7;
L_nm = 49;

%Creating a matrix to be passed into all of the functions
L = [L_0i L_ij L_1j L_1k L_kj L_m1 L_mi L_lk L_ml L_nl L_nm];

%The number of crank angles
N = 100;

%=========================================================================%
%Function call to find all the angles for all the associated crank angles
Storage_Angles = getAllAngles(N,L);

%Function call to get all coordinates for all the associated crank angles
Storage_Coordinates = getAllCoordinates(N,Storage_Angles,L);

%Function call to draw Jansen Linkage model and create video
drawJansen(Storage_Coordinates,Storage_Angles,N,L);