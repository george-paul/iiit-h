function [handleLink] = drawLink(Yo,Zo,N,len,phi,X,radius)
%[handleLink] = drawLink(Xo,Yo,N,len,phi,Z,depth):
%Using the built in 'patch' command, the function draws a link of the
%Jansen Linkage model based on the given inputs.
%Input Yo,Zo = the coordinates of the lowest point of the link.
%Input N = number of crank angles
%Input len = length of the link
%Input phi = angle of the link raised above the positive y-axis
%Input X = the offset from the Y-Z axis, giving it depth
%Input radius = radius of the cylinders
%Output handleLink = handle to the link created

%Version 1: Created 07/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to draw the links of the Jansen
%Linkage model

%=========================================================================%
%Internal Parameters

%Creating N number of angles for the cylinder.
theta = [0:(2*pi)/N:(2*pi)-(2*pi)/N]';

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 7), error('Incorrect number of input arguments.'); end

%Storing the top vertices and the bottom vertices
v_bottom = [X+(radius*cos(theta)) zeros(N,1) radius*sin(theta)];
v_top = [X+(radius*cos(theta)) len*ones(N,1) radius*sin(theta)];

%Concatenating the top and bottom verices
vertex_matrix_link1 = [v_bottom;v_top];

%Creating the face matrix (Acknowledgement should be given to Prof. Paul
%Curran, it is his notes from which the following matrix was taken)
face_matrix_link1 = [[1:N];[1:N]' [[2:N] 1]' [(N+[2:N]) (N+1)]' ((N+[1:N])')*ones(1,(N-3));N+[1:N]];

%Store memory for the rotated link
v_rotated = zeros(2*N,3);

%Create rotation matrix to rotate link in the Y-Z plane (the -phi ensures
%that the shaft rotates counter clockwise)
Rtheta = [1 0 0; 0 cos(-phi) sin(-phi);0 -sin(-phi) cos(-phi)];

%Rotate every point of the vertices
for count = 1:2*N
    v_rotated(count,:) = (Rtheta*(vertex_matrix_link1(count,:)'))';
end

%Shift the link so that it is in the correct coordinate
v_rotated = [v_rotated(:,1) v_rotated(:,2)+Yo v_rotated(:,3)+Zo];

%Using the patch command to draw link
handleLink = patch('Vertices',v_rotated, 'Faces',face_matrix_link1, 'FaceColor',[128/255 0/255 128/255],'FaceLighting','gouraud','Linestyle','none');

end

