function [handleLink] = drawStaticLink(Yo,Zo,len,radius,X,N,varargin)
%[handleLink] = drawStaticLink(Yo,Zo,len,radius,X,N):
%Using the built in 'patch' command, the function draws a node at the
%intersection of the Jansen Linkage model based on the given inputs.
%Input Yo,Zo = the coordinates of the intesection.
%Input N = number of crank angles
%Input len = length of the node
%Input X = the offset from the Y-Z axis, giving it depth
%Input radius = radius of the node
%Input varargin = maximum of three variable inputs that can specify the
%colour, their default values is set to give the colour green. The input
%should be based off MATLAB's schematic of [R G B] to define colour, where
%R,G or B must be less than or equal to 1.
%Output handleLink = handle to the node created

%Version 1: Created 08/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to draw the nodes at the
%intersection of the links.

%=========================================================================%
%Internal Parameters

%Creating N number of angles for the cylinder.
theta = [0:(2*pi)/N:(2*pi)-((2*pi)/N)]';

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin < 6), error('Incorrect number of input arguments.'); end

%Finding the number of inputs and checking to see if it is greater than 3
numvarargs = length(varargin);
if(numvarargs > 3)
    error('drawStaticLink: Requires at most 3 optional inputs');
end

%Setting the default value to equal green
optargs = {50/255 205/255 50/255};

%Replacing any of the optional inputs with the default value
[optargs{1:numvarargs}] = varargin{:};

%Giving meaningful names to the inputs, red(R), green(G) and blue(B)
[R,G,B] = optargs{:};

%Get the vertices of the top and bottom of the node
v_bottom = [zeros(N,1) radius*cos(theta)+Yo radius*sin(theta)+Zo];
v_top = [len*ones(N,1) radius*cos(theta)+Yo radius*sin(theta)+Zo];

%Concatenation of the upper vertices and lower vertices
v_matrix = [v_bottom; v_top];

%Shifting the vertex matrix in the x axis
v_matrix = [X+v_matrix(:,1) v_matrix(:,2) v_matrix(:,3)];

%Creating the face matrix (Acknowledgement should be given to Prof. Paul
%Curran, it is his notes from which the following matrix was taken)
face_matrix_link1 = [[1:N];[1:N]' [[2:N] 1]' [(N+[2:N]) (N+1)]' ((N+[1:N])')*ones(1,(N-3));N+[1:N]];

%Using the patch command to draw node
handleLink = patch('Vertices',v_matrix, 'Faces',face_matrix_link1, 'FaceColor',[R G B],'FaceLighting','gouraud','Linestyle','none');

end



