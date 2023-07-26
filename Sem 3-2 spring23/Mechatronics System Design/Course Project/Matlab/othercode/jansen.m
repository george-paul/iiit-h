close all               
clear all               
clc                     

% constants

crank_r = 150;
link_1 = 500;
link_2 = 558;
link_3 = 394;
link_4 = 657;
link_5 = 490;
link_6 = 619;
link_7 = 367;
link_8 = 393;
link_9 = 415;
link_10 = 401;
link_11 = 412;

crank_x = 0;
crank_y = 0;

pin_x = crank_x - 380;
pin_y = crank_y - 78;

node_1_x = pin_x;
node_1_y = 5;

link_9_t = 0;

link_10_t = pi;
link_11_t = pi;

node_2_x = pin_x - link_9;
node_2_y = pin_y;

link_8_t = 3/4*pi;

node_3_x = pin_x;
node_3_y = pin_y - link_8;

link_7_t = pi;

node_4_x = pin_x - link_7;
node_4_y = pin_y - link_3;

link_5_t = 3/4*pi;

node_5_y = pin_y - link_8 - link_5;
node_5_x = pin_x;

node_6_y = node_5_y;
node_6_x = node_5_x;

% plotting
figure(3)

i=0;

x = [];
y = [];

for t=0:0.1:8*pi+pi/2+pi

    i = i + 1;

    node_0_x = crank_x + crank_r*cos(t);
    node_0_y = crank_y + crank_r*sin(t);

    
    % node 1

    dist = 10000000;
    
    for link_9_t=0:0.02:pi
        node_1_x = pin_x + link_9*cos(link_9_t);
        node_1_y = pin_y + link_9*sin(link_9_t);

        dist_tmp = sqrt((node_0_x-node_1_x)^2+(node_0_y-node_1_y)^2);

        diff = abs(dist_tmp - link_1);

        if (diff < dist)
            dist = diff;
            theta = link_9_t;
        end
    end
    
    link_9_t = theta;
    
    node_1_x = pin_x + link_9*cos(link_9_t);
    node_1_y = pin_y + link_9*sin(link_9_t);
    
    
    % node 2
    
    dist = 10000000;
    
    for link_10_t=.75*pi:0.02:1.5*pi
        node_2_x = pin_x + link_10*cos(link_10_t);
        node_2_y = pin_y + link_10*sin(link_10_t);
    
        dist_tmp = sqrt((node_2_x-node_1_x)^2+(node_2_y-node_1_y)^2);
        
        diff = abs(dist_tmp - link_2);
        
        if (diff < dist)
            dist = diff;
            theta = link_10_t;
        end
    end
    
    link_10_t = theta;
    
    node_2_x = pin_x + link_10*cos(link_10_t);
    node_2_y = pin_y + link_10*sin(link_10_t);
    
    % node 3
    
     dist = 10000000;
    
    for link_8_t=pi:0.02:2*pi
        node_3_x = pin_x + link_8*cos(link_8_t);
        node_3_y = pin_y + link_8*sin(link_8_t);
    
        dist_tmp = sqrt((node_0_x-node_3_x)^2+(node_0_y-node_3_y)^2);
        
        diff = abs(dist_tmp - link_6);
        
        if (diff < dist)
            dist = diff;
            theta = link_8_t;
        end
    end
    
    link_8_t = theta;
    
    node_3_x = pin_x + link_8*cos(link_8_t);
    node_3_y = pin_y + link_8*sin(link_8_t);
    
    % node 4
    
    dist = 10000000;
    
    for link_7_t=.75*pi:0.02:1.5*pi
        node_4_x = node_3_x + link_7*cos(link_7_t);
        node_4_y = node_3_y + link_7*sin(link_7_t);
    
        dist_tmp = sqrt((node_4_x-node_2_x)^2+(node_4_y-node_2_y)^2);
        
        diff = abs(dist_tmp - link_3);
        
        if (diff < dist)
            dist = diff;
            theta = link_7_t;
        end
    end
    
    link_7_t = theta;
    
    node_4_x = node_3_x + link_7*cos(link_7_t);
    node_4_y = node_3_y + link_7*sin(link_7_t);
    
    
    % node 5
    
    dist = 10000000;
    
    for link_5_t=pi:0.02:2*pi
        node_5_x = node_3_x + link_5*cos(link_5_t);
        node_5_y = node_3_y + link_5*sin(link_5_t);
    
        dist_tmp = sqrt((node_4_x-node_5_x)^2+(node_4_y-node_5_y)^2);
       
        diff = abs(dist_tmp - link_4);
      
        if (diff < dist)
            dist = diff;
            theta = link_5_t;
        end
    end

    link_5_t = theta;

    node_5_x = node_3_x + link_5*cos(link_5_t);
    node_5_y = node_3_y + link_5*sin(link_5_t);

    node_6_x = node_3_x + link_11*cos(link_5_t);
    node_6_y = node_3_y + link_11*sin(link_5_t);

    x(end+1) = node_6_x;
    y(end+1) = node_6_y;

    % draw plot

    plot([crank_x pin_x], [crank_y pin_y],'black','linewidth',4); hold on       % crank to pin
    plot([crank_x node_0_x], [crank_y node_0_y],'r','linewidth',4); hold on     % crank

    plot([node_0_x node_1_x], [node_0_y node_1_y],'b','linewidth',4);           % link_1
    plot([pin_x node_1_x], [pin_y node_1_y],'g','linewidth',4);                 % link_9

    plot([pin_x node_2_x], [pin_y node_2_y],'g','linewidth', 4);                % link_10
    plot([node_1_x node_2_x], [node_1_y node_2_y],'g','linewidth', 4);          % link_2

    plot([node_0_x node_3_x], [node_0_y node_3_y],'g','linewidth',4);           % link_6
    plot([pin_x node_3_x], [pin_y node_3_y],'r','linewidth',4);                 % link_8

    plot([node_3_x node_4_x], [node_3_y node_4_y],'b','linewidth', 4);          % link_7
    plot([node_2_x node_4_x], [node_2_y node_4_y],'r','linewidth', 4);          % link_3

    plot([node_3_x node_6_x], [node_3_y node_6_y],'r','linewidth', 4);          % link_5
    plot([node_4_x node_6_x], [node_4_y node_6_y],'b','linewidth', 4);          % link_4

    plot([node_3_x node_6_x], [node_3_y node_6_y],'b','linewidth', 4);          % link_5

    plot(x,y);

    hold off
    axis([-1300 200 -900 600]);
    exportgraphics(gcf,'testAnimated.gif','Append',true);
    % pause(0.01)
    avi(i) = getframe(gca);
end
