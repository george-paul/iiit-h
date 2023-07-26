function [Storage_Angles] = getAllAngles(N,L)
%[Storage_Angles] = getAllAngles(N):
%Calculates and stores all 11 angles of the Jansen Linkage for N number of
%crank angles inputted.
%Input L = matrix of all the lenghts of Jansen Structure
%Input N = number of crank angles 
%Output Storage_Angles = matrix of all the angles for each crank angle.

%Version 1: Created 04/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to calculate amny systems of
%linear equations.

%-------------------------------------------------------------------------%
%Internal Parameters

%Initial guesses made from a static figure of the Jansen Linkage model
theta_ij = deg2rad(150);
theta_1j = deg2rad(80);
theta_1k = deg2rad(165);
theta_kj = deg2rad(35);
theta_m1 = deg2rad(115);
theta_mi = deg2rad(55);
theta_lk = deg2rad(120);
theta_ml = deg2rad(160);
theta_nl = deg2rad(112);
theta_nm = deg2rad(80);

%-------------------------------------------------------------------------%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 2), error('Incorrect number of input arguments.'); end

%An initial matrix is assigned memory to be able to hold all the expected
%angles
S = zeros(N,11);

%Creating all the values of the crank angles
phi = ([0:(2*pi)/N:((2*pi)-(2*pi)/N)])+deg2rad(35);

%Loop created to get all 11 angles for each of the crank angles, the
%previous angle is used as the initial guess to find the next angle
for count = 1:N
    %First set of equations
    c1 = (L(1)*cos(phi(count)))+38;
    c2 = (L(1)*sin(phi(count)))+7.8;
    [theta_ij,theta_1j] = getAngle(L(2), -(L(3)), theta_ij, theta_1j, c1, c2);
    
    %Second set of equations
    c1 = -(L(3)*cos(theta_1j));
    c2 = -(L(3)*sin(theta_1j));
    [theta_1k,theta_kj] = getAngle(L(4), L(5), theta_1k, theta_kj, c1, c2);
    
    %Third set of equations
    c1 = (L(1)*cos(phi(count)))+38;
    c2 = (L(1)*sin(phi(count)))+7.8;
    [theta_m1,theta_mi] = getAngle(L(6), -(L(7)), theta_m1, theta_mi, c1, c2);
    
    %Fourth set of equations
    c1 = (L(4)*cos(theta_1k))+(L(6)*cos(theta_m1));
    c2 = (L(4)*sin(theta_1k))+(L(6)*sin(theta_m1));
    [theta_lk,theta_ml] = getAngle(-(L(8)), -(L(9)), theta_lk, theta_ml, c1, c2);
    
    %Fifth set of equations
    c1 = L(9)*cos(theta_ml);
    c2 = L(9)*sin(theta_ml);
    [theta_nl,theta_nm] = getAngle(-L(10), L(11), theta_nl, theta_nm, c1, c2);
    
    S(count,:) = [phi(count) theta_ij theta_1j theta_1k theta_kj theta_m1 theta_mi theta_lk theta_ml theta_nl theta_nm];

end

Storage_Angles = S;

%Error Checking: To ensure corrent number of values being outputted
if (nargout ~= 1), error('An incorrect number of elements are being returned'); end

end

