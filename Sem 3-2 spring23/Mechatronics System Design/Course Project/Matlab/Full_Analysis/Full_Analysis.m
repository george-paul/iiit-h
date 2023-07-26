%% Analysis for the jansen mechanism 
%wikipedia.org/wiki/Leg_mechanism#/media/File:Strandbeest-Walking-Animation.gif
%% KINEMATIC AND DYNAMIC ANALYSIS OF MECHANISM
% Winter 17. JAIME ROQUE 02/25/17

clear all; clc; close all;

%% ==============KNOWN ANGLES AND DISTANCES==================

L1=6;L2=1;L3=8;L33=8;L4=5;L44=5;L5=5;L6=5;L66=9;L7=5;L8=.5;
A1=0;A2=pi/2:0.3:6*pi+(pi/2);
 
A22=pi+A2;
A2=-A2;  A22=-A22;

%% ==================POSITION ANALYSIS=======================

% Point B.1
Bx=L2.*cos(A2);
By=L2.*sin(A2);
% Point B.2
B2x=L2.*cos(A22);
B2y=L2.*sin(A22);

% First Loop
[A3,A4]=Mechanism(L1,L2,L3,L4,A1,A2,'cross');  
A5=(pi-A4)+(pi/2);

[A32,A42]=Mechanism(L1,L2,L3,L4,A1,A22,'cross');  
A52=(pi-A42)+(pi/2);

% Point C
Cx=Bx+(L3.*cos(A3));  
Cy=L4.*sin(A4);

C2x=B2x+(L3.*cos(A32));  
C2y=L4.*sin(A42);

% Point E
Ex=L1;    Ey=-L8;

% Second Loop
j=2.*L4.*((L1.*cos(A1))-(L2.*cos(A2)));
k=2.*L4.*((L1.*sin(A1))-(L2.*sin(A2)));
m=(L1.^2)+(L2.^2)-(L33.^2)+(L44.^2)-(2.*L1.*L2.*cos(A1-A2));

A44=2.*atan((-k+sqrt((j.^2)+(k.^2)-(m.^2)))./(m-j));

n=2.*L3.*((L2.*cos(A2))-(L1.*cos(A1)));
p=2.*L3.*((L2.*sin(A2))-(L1.*sin(A1)));
q=(L1.^2)+(L2.^2)+(L33.^2)-(L44.^2)-(2.*L1.*L2.*cos(A2-A1));

A33=2.*atan((-p-sqrt((n.^2)+(p.^2)-(q.^2)))./(q-n));


j2=2.*L4.*((L1.*cos(A1))-(L2.*cos(A22)));
k2=2.*L4.*((L1.*sin(A1))-(L2.*sin(A22)));
m2=(L1.^2)+(L2.^2)-(L33.^2)+(L44.^2)-(2.*L1.*L2.*cos(A1-A22));

A442=2.*atan((-k2+sqrt((j2.^2)+(k2.^2)-(m2.^2)))./(m2-j2));

n2=2.*L3.*((L2.*cos(A22))-(L1.*cos(A1)));
p2=2.*L3.*((L2.*sin(A22))-(L1.*sin(A1)));
q2=(L1.^2)+(L2.^2)+(L33.^2)-(L44.^2)-(2.*L1.*L2.*cos(A22-A1));

A332=2.*atan((-p2-sqrt((n2.^2)+(p2.^2)-(q2.^2)))./(q2-n2));

% Point D
Dx=Ex+L5.*cos(pi-A5);
Dy=Ey+L5.*sin(pi-A5);

D2x=Ex+L5.*cos(pi-A52);
D2y=Ey+L5.*sin(pi-A52);

% Third Loop
A5=-A5;    A4=-A4;
[A6,A7]=Mechanism(L5,L4,L6,L7,A5,A4,'cross');

A52=-A52;    A42=-A42;
[A62,A72]=Mechanism(L5,L4,L6,L7,A52,A42,'cross');

% Point F
Fx=Bx+(L33.*cos(A33));
Fy=By+L33.*sin(A33);

F2x=B2x+(L33.*cos(A332));
F2y=B2y+L33.*sin(A332);

% Point G
Gx=Fx-L6.*cos(A6);
Gy=Fy-L6.*sin(A6);

G2x=F2x-L6.*cos(A62);
G2y=F2y-L6.*sin(A62);

% Point H
Hx=Fx+L66.*cos(A6+(pi/2));
Hy=Fy+L66.*sin(A6+(pi/2));

H2x=F2x+L66.*cos(A62+(pi/2));
H2y=F2y+L66.*sin(A62+(pi/2));

% Point BB.1
BBx=-L2.*cos(A2);
BBy=L2.*sin(A2);
% Point B.2
BB2x=-L2.*cos(A22);
BB2y=L2.*sin(A22);

% Point CC
CCx=BBx-(L3.*cos(A3));  
CCy=-L4.*sin(A4);

CC2x=B2x-(L3.*cos(A32));  
CC2y=-L4.*sin(A42);

% Point EE
EEx=-L1;    EEy=-L8;

% Point DD
DDx=EEx-L5.*cos(pi-A5);
DDy=EEy-L5.*sin(pi-A5);

DD2x=EEx-L5.*cos(pi-A52);
DD2y=EEy-L5.*sin(pi-A52);

% Point FF
FFx=BBx-(L33.*cos(A33));
FFy=BBy+L33.*sin(A33);

FF2x=BB2x-(L33.*cos(A332));
FF2y=BB2y+L33.*sin(A332);

% Point GG
GGx=FFx+L6.*cos(A6);
GGy=FFy-L6.*sin(A6);

GG2x=FF2x+L6.*cos(A62);
GG2y=FF2y-L6.*sin(A62);

% Point HH
HHx=FFx-L66.*cos(A6+(pi/2));
HHy=FFy+L66.*sin(A6+(pi/2));

HH2x=FF2x-L66.*cos(A62+(pi/2));
HH2y=FF2y+L66.*sin(A62+(pi/2));



%% ==================VELOCITIES ANALYSIS=======================

A4=-A4;  A5=-A5;

W2=2;  % Angular velocity of the crank

W3=-(L2.*W2.*sin(A2-A4))./(L3.*sin(A3-A4));
W4=(L2.*W2.*sin(A2-A3))./(L4.*sin(A4-A3));
W5=W4;

W33=-(L2.*W2.*sin(A2-A44))./(L33.*sin(A33-A44));
W44=(L2.*W2.*sin(A2-A33))./(L44.*sin(A44-A33));

A4=-A4;  A5=-A5;
W6=(L5.*W5.*sin(A5-A7)-L44.*W44.*sin(A44-A7))./(L6.*sin(A6-A7));
W7=(L44.*W44.*sin(A44)-L5.*W5.*sin(A5)+L6.*W6.*sin(A6))./(L7.*sin(A7));


%% ==================ACCELERATION ANALYSIS=======================

A4=-A4;  A5=-A5;

Alf2=0;    % Angular acceleration of the crank

Alf3=((L2.*(W2.^2).*cos(A2-A4))+(L3.*(W3.^2).*cos(A3-A4))-(L4.*(W4.^2))-(L2.*sin(A4-A2)))./(L3.*sin(A4-A3));
Alf4=((L2.*Alf2.*sin(A3-A2))-(L2.*(W2.^2).*cos(A2-A3))-(L3.*(W3.^2))+(L4.*(W4.^2).*cos(A4-A3)))./(L4.*sin(A3-A4));
Alf5=Alf4;

Alf33=((L2.*(W2.^2).*cos(A2-A44))+(L33.*(W33.^2).*cos(A33-A44))-(L44.*(W44.^2))-(L2.*sin(A44-A2)))./(L33.*sin(A44-A33));
Alf44=((L2.*Alf2.*sin(A33-A2))-(L2.*(W2.^2).*cos(A2-A33))-(L33.*(W33.^2))+(L44.*(W44.^2).*cos(A44-A33)))./(L44.*sin(A33-A44));

A4=-A4;  A5=-A5;
Alf7=((L44.*Alf44.*sin(A44-A6))+(L44.*(W44.^2).*cos(A44-A6))+(L6.*(W6.^2))-(L5.*Alf5.*sin(A5-A6))-(L5.*(W5.^2).*cos(A5-A6))-(L7.*(W7.^2).*cos(A7-A6)))./(L7.*sin(A7-A6));
Alf6=((L5.*Alf5.*sin(A5-A7))+(L5.*(W5.^2).*cos(A5-A7))+(L7.*(W7.*2))-(L44.*Alf44.*sin(A44-A7))-(L44.*(W44.^2).*cos(A44-A7))-(L6.*(W6.^2).*cos(A6-A7)))./(L6.*sin(A6-A7));

A4=-A4;  A5=-A5;


%% =======================SIMULATION=======================
figure('name','Movement Simulation','NumberTitle','off');
v = 2;
for i=1:length(A2)
    cla;
   %plot(Bx,By,'--k');    %  B path
   hold on
   % Dots representation   
   plot(0,0,'or'); 
   axis([-13 14 -14 6]); 
   plot(Bx(i),By(i),'or');   
   plot(Cx(i),Cy(i),'ok');    
   plot(Ex,Ey,'or'); 
   plot(Dx(i),Dy(i),'ok');
   plot(Fx(i),Fy(i),'ok');
   plot(Gx(i),Gy(i),'ok');
   plot(Hx(i),Hy(i),'ok');
   
   plot(B2x(i),B2y(i),'or');   
   plot(C2x(i),C2y(i),'ok');    
   plot(Ex,Ey,'or'); 
   plot(D2x(i),D2y(i),'ok');
   plot(F2x(i),F2y(i),'ok');
   plot(G2x(i),G2y(i),'ok');
   plot(H2x(i),H2y(i),'ok');

   % System 1
   plot([EEx Ex],[-0.5 -0.5],'-k','LineWidth',2); 
   plot([0 0],[0 -0.5],'-k','LineWidth',2); 
   plot([0 Bx(i)],[0 By(i)],'-k','LineWidth',1); 
   plot([Bx(i) Cx(i)],[By(i) Cy(i)],'-m','LineWidth',001);  
   plot([Ex Cx(i)],[Ey Cy(i)],'-m','LineWidth',001);
   plot([Ex Dx(i)],[Ey Dy(i)],'-m','LineWidth',001);
   plot([Cx(i) Dx(i)],[Cy(i) Dy(i)],'-m','LineWidth',001);
   plot([Bx(i) Fx(i)],[By(i) Fy(i)],'-m','LineWidth',001);
   plot([Ex Fx(i)],[Ey Fy(i)],'-m','LineWidth',1);
   plot([Dx(i) Gx(i)],[Dy(i) Gy(i)],'-m','LineWidth',001);
   plot([Fx(i) Gx(i)],[Fy(i) Gy(i)],'-m','LineWidth',001);
   
   % System 1 Interior  
   patch([Ex,Cx(i),Dx(i)],[Ey,Cy(i),Dy(i)],'g')
   patch([Fx(i),Hx(i),Gx(i)],[Fy(i),Hy(i),Gy(i)],'c')
   
   % System 2    
   plot([0 B2x(i)],[0 B2y(i)],'-k','LineWidth',1); 
   plot([B2x(i) C2x(i)],[B2y(i) C2y(i)],'-b','LineWidth',1);  
   plot([Ex C2x(i)],[Ey C2y(i)],'-b','LineWidth',001);
   plot([Ex D2x(i)],[Ey D2y(i)],'-b','LineWidth',001);
   plot([C2x(i) D2x(i)],[C2y(i) D2y(i)],'-b','LineWidth',001);
   plot([B2x(i) F2x(i)],[B2y(i) F2y(i)],'-b','LineWidth',001);
   plot([Ex F2x(i)],[Ey F2y(i)],'-b','LineWidth',001);
   plot([D2x(i) G2x(i)],[D2y(i) G2y(i)],'-b','LineWidth',001);
   plot([F2x(i) G2x(i)],[F2y(i) G2y(i)],'-b','LineWidth',001);
   
   % System 2 Interior   
   patch([Ex,C2x(i),D2x(i)],[Ey,C2y(i),D2y(i)],'c')
   patch([F2x(i),H2x(i),G2x(i)],[F2y(i),H2y(i),G2y(i)],'g')

   title('JANSEN MECHANISM - Jaime Roque');
  
   % Background
   set(gcf,'color','y')
   set(gca,'xcolor','y')
   set(gca,'ycolor','y')
   set(gca,'color','y')
    
   % Curves draw    
   plot(Hx(1:i),Hy(1:i),'-b');  
   plot(H2x(1:i),H2y(1:i),'-b'); 
   
   % Calling for Bearing doc
  % [Bearx,Beary]=Bearing(0,0,4);
   %plot(Bearx,Beary,'k')
   %[Bearx,Beary]=Bearing(Ex,Ey,4);
   %plot(Bearx,Beary,'k')  
  
   % Points legend 
   text(-1,-0.8,'A'); 
   text(Bx(i)+0.1*L2,By(i)+0.1*L2,'B'); 
   text(Cx(i)+0.1*(L3/2),Cy(i)+0.1*(L3/2),'C'); 
   text(5.8,-0.8,'E'); 
   text(Dx(i)+0.1*L5,Dy(i)+0.1*L5,'D'); 
   text(Fx(i)+0.1*(L3/2),Fy(i)+0.1*(L3/2),'F');
   text(Gx(i)+0.1*(L3/2),Gy(i)+0.1*(L3/2),'G');
   
   text(B2x(i)+0.1*L2,B2y(i)+0.1*L2,'B2'); 
   text(C2x(i)+0.1*(L3/2),C2y(i)+0.1*(L3/2),'C2'); 
   text(D2x(i)+0.1*L5,D2y(i)+0.1*L5,'D2'); 
   text(F2x(i)+0.1*(L3/2),F2y(i)+0.1*(L3/2),'F2');
   text(G2x(i)+0.1*(L3/2),G2y(i)+0.1*(L3/2),'G2');
   
   plot(BBx,BBy,'--k');    %  BB path
sh = 5;
   k= mod(i + sh, length(A2)) +1;
   %k =i;
   % Dots representation   
   plot(0,0,'or'); 
   axis([-13 14 -14 6]); 
   plot(BBx(k),BBy(k),'or');   
   plot(CCx(k),CCy(k),'ok');    
   plot(EEx,EEy,'or'); 
   plot(DDx(k),DDy(k),'ok');
   plot(FFx(k),FFy(k),'ok');
   plot(GGx(k),GGy(k),'ok');
   plot(HHx(k),HHy(k),'ok');
   
   plot(BB2x(k),BB2y(k),'or');   
   plot(CC2x(k),CC2y(k),'ok');    
   plot(EEx,EEy,'or'); 
   plot(DD2x(k),DD2y(k),'ok');
   plot(FF2x(k),FF2y(k),'ok');
   plot(GG2x(k),GG2y(k),'ok');
   plot(HH2x(k),HH2y(k),'ok');

   % System 1
   plot([0 BBx(k)],[0 BBy(k)],'-k','LineWidth',1); 
   plot([BBx(k) CCx(k)],[BBy(k) CCy(k)],'-m','LineWidth',001);  
   plot([EEx CCx(k)],[EEy CCy(k)],'-m','LineWidth',001);
   plot([EEx DDx(k)],[EEy DDy(k)],'-m','LineWidth',001);
   plot([CCx(k) DDx(k)],[CCy(k) DDy(k)],'-m','LineWidth',001);
   plot([BBx(k) FFx(k)],[BBy(k) FFy(k)],'-m','LineWidth',001);
   plot([EEx FFx(k)],[EEy FFy(k)],'-m','LineWidth',001);
   plot([DDx(k) GGx(k)],[DDy(k) GGy(k)],'-m','LineWidth',001);
   plot([FFx(k) GGx(k)],[FFy(k) GGy(k)],'-m','LineWidth',001);
   
   % System 1 Interior  
   patch([EEx,CCx(k),DDx(k)],[EEy,CCy(k),DDy(k)],'g')
   patch([FFx(k),HHx(k),GGx(k)],[FFy(k),HHy(k),GGy(k)],'c')
   
   % System 2    
   plot([0 BB2x(k)],[0 BB2y(k)],'-k','LineWidth',1); 
   plot([BB2x(k) CC2x(k)],[BB2y(k) CC2y(k)],'-b','LineWidth',001);  
   plot([EEx CC2x(k)],[EEy CC2y(k)],'-b','LineWidth',001);
   plot([EEx DD2x(k)],[EEy DD2y(k)],'-b','LineWidth',001);
   plot([CC2x(k) DD2x(k)],[CC2y(k) DD2y(k)],'-b','LineWidth',001);
   plot([BB2x(k) FF2x(k)],[BB2y(k) FF2y(k)],'-b','LineWidth',001);
   plot([EEx FF2x(k)],[EEy FF2y(k)],'-b','LineWidth',001);
   plot([DD2x(k) GG2x(k)],[DD2y(k) GG2y(k)],'-b','LineWidth',001);
   plot([FF2x(k) GG2x(k)],[FF2y(k) GG2y(k)],'-b','LineWidth',001);
   
   % System 2 Interior   
   patch([EEx,CC2x(k),DD2x(k)],[EEy,CC2y(k),DD2y(k)],'c')
   patch([FF2x(k),HH2x(k),GG2x(k)],[FF2y(k),HH2y(k),GG2y(k)],'g')
    
   % Curves draw    
   plot(HHx(1:k),HHy(1:k),'-b');  
   plot(HH2x(1:k),HH2y(1:k),'-b'); 
  
   % Points legend 
   text(-1,-0.8,'A'); 
   text(BBx(k)+0.1*L2,BBy(k)+0.1*L2,'B'); 
   text(CCx(k)+0.1*(L3/2),CCy(k)+0.1*(L3/2),'C'); 
   text(-4.8,-0.8,'E'); 
   text(DDx(k)+0.1*L5,DDy(k)+0.1*L5,'D'); 
   text(FFx(k)+0.1*(L3/2),FFy(k)+0.1*(L3/2),'F');
   text(GGx(k)+0.1*(L3/2),GGy(k)+0.1*(L3/2),'G');
   
   text(BB2x(k)+0.1*L2,BB2y(k)+0.1*L2,'B2'); 
   text(CC2x(k)+0.1*(L3/2),CC2y(k)+0.1*(L3/2),'C2'); 
   text(DD2x(k)+0.1*L5,DD2y(k)+0.1*L5,'D2'); 
   text(FF2x(k)+0.1*(L3/2),FF2y(k)+0.1*(L3/2),'F2');
   text(GG2x(k)+0.1*(L3/2),GG2y(k)+0.1*(L3/2),'G2');
   
   pause(.0001);   

   hold off;  
end

%% =======POSITION,VELOCITY AND ACCELERATION GRAPHICS ==========

figure('name','Joints Graphs','NumberTitle','off');
set(gcf,'color','W')
set(gca,'xcolor','W')
set(gca,'ycolor','W')
set(gca,'color','W')

subplot(2,2,1),plot(A2,A3,'k',A2,W3,'r',A2,Alf3,'b');
grid on;title('L2 Joint')
legend('Pos','Vel','Acce');axis([-12 -1 -3 3]);
subplot(2,2,2),plot(A2,A4,'k',A2,W4,'r',A2,Alf4,'b');
grid on;title('L3 Joint')
legend('Pos','Vel','Acce');axis([-12 -1 -8 8]);
subplot(2,2,3),plot(A2,A33,'k',A2,W33,'r',A2,Alf33,'b');
grid on;title('L22 Joint')
legend('Pos','Vel','Acce');axis([-12 -1 -3 3]);
subplot(2,2,4),plot(A2,A44,'k',A2,W44,'r',A2,Alf44,'b');
grid on;title('L33 Joint')
legend('Pos','Vel','Acce');axis([-12 -1 -4 3]);

figure('name','Joints Graphs (continuation)','NumberTitle','off');
set(gcf,'color','W')
set(gca,'xcolor','W')
set(gca,'ycolor','W')
set(gca,'color','W')

subplot(2,2,1),plot(A2,A6,'k',A2,W6,'b',A2,Alf6,'r');
grid on;title('L4 Joint')
legend('Pos','Vel','Acce');axis([-12 -1 -5 12]);
subplot(2,2,2),plot(A2,A7,'k',A2,W7,'b',A2,Alf7,'r');
grid on;title('L5 Joint')
legend('Pos','Vel','Acce');axis([-12 -1 -5 12]);

