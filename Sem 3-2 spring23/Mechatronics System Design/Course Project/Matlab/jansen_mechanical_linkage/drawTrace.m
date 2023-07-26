function [handleLink] = drawTrace(Yo,Zo,radius,len,N,X)
%[handleLink] = drawTrace(Yo,Zo,depth,len,N):
%Using the built in 'patch' command, the function draws a very small
%cylinder at every point of the N node.
%Input Yo,Zo = the coordinates of the N node
%Input N = number of crank angles
%Input len = length of the cylinder
%Input X = the offset from the Y-Z axis, giving it depth
%Input radius = radius of the node
%Output handleLink = handle to the cylinder created

%Version 1: Created 09/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to draw the cylinder for the
%trace.

%=========================================================================%
%Internal Parameters

%Creating N number of angles for the cylinder.
theta = [0:(2*pi)/N:(2*pi)-((2*pi)/N)]';

%Offset to keep the trace behind the bottom node.
y_offset = 6;

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 6), error('Incorrect number of input arguments.'); end

%Storing the top vertices and the bottom vertices
v_bottom = [(radius*cos(theta))+X zeros(N,1)+(Yo-y_offset) (radius*sin(theta))+Zo];
v_top = [(radius*cos(theta))+X len*ones(N,1)+(Yo-y_offset) (radius*sin(theta))+Zo];

%Concatenating the top and bottom vertices
vertex_matrix_trace = [v_bottom;v_top];

%Creating the face matrix (Acknowledgement is given to Prof. Paul
%Curran, it is his notes from which the following matrix was taken)
face_matrix_trace = [[1:N];[1:N]' [[2:N] 1]' [(N+[2:N]) (N+1)]' ((N+[1:N])')*ones(1,(N-3));N+[1:N]];

%Using patch to draw the cylinder.
handleLink = patch('Vertices',vertex_matrix_trace, 'Faces',face_matrix_trace, 'FaceColor',[255/255 69/255 0/255],'FaceLighting','gouraud','Linestyle','none');

end