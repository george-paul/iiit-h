function [] = drawJansen(S,A,N,L)
%[] = drawJansen(S,A,N):
%Draws the entire Jansen Linkage model taking N number of Frames for the
%video that is created.
%Input S = matrix of all the coordinates
%Input A = matrix of all of the crank angles
%Input N = number of crank angles

%Version 1: Created 09/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to create a video of the Jansen
%Linkage model

%=========================================================================%
%Internal Parameters

%The number of frames in the video
FrameNumber = N;

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 4), error('Incorrect number of input arguments.'); end

    
% Use VideoWriter to create a suitable video object ready to receive data.
VideoObject = VideoWriter('Jansen.avi');
open(VideoObject);

%Setting up the axis and then removing it
handlefig = figure('Position',[100 100 850 600]);
axis([-110 110 -110 110 -110 110]);
axis off;
    
%Setting up the azmiuth and elevation to set up a particular viewpoint
az = 140;
el = 10;
view(az,el)
    
%Setting up light sources
light('Position',[200 200 0]);
light('Position',[100 -50 -50]);

%Loop that draws out the figure of each frame to create video    
for count = 1:FrameNumber   
    %Function call to draw all the frames and gets the output of a matrix
    %of all the links to be deleted.
    handleLinks = drawAllLinks(S,A,count,N,L);

    %Get the frame and add it into the video
    current_frame = getframe(handlefig);
    writeVideo(VideoObject,current_frame);
    
    %In this implementation the figure is kept open constantly in order for
    %the trace to be recorded. After every frame is captured all but the
    %trace is to be deleted from the matrix of handles
    delete(handleLinks);

%end
    
end
