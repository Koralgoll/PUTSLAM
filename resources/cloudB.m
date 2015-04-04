close all; clear all;
hold on;
plot3(-0.526662, -0.449252, 2.93561,'r.' );
C = [0.00544223, 0.00458931, -0.0300084; 0.00458931, 0.00392352, -0.0254985; -0.0300084, -0.0254985, 0.166729];
M = [-0.526662;-0.449252; 2.93561];
error_ellipse(C, M);
plot3(-0.589022, -0.535405, 3.44364,'r.' );
C = [0.00628577, 0.00562503, -0.0362871; 0.00562503, 0.00511251, -0.0327684; -0.0362871, -0.0327684, 0.211389];
M = [-0.589022;-0.535405; 3.44364];
error_ellipse(C, M);
plot3(-0.58826, -0.527352, 3.44432,'r.' );
C = [0.00628766, 0.00555119, -0.036298; 0.00555119, 0.00497856, -0.0323382; -0.036298, -0.0323382, 0.211452];
M = [-0.58826;-0.527352; 3.44432];
error_ellipse(C, M);
plot3(-0.589466, -0.510924, 3.34112,'r.' );
C = [0.00644672, 0.00542125, -0.0359373; 0.00542125, 0.00462797, -0.0304731; -0.0359373, -0.0304731, 0.202005];
M = [-0.589466;-0.510924; 3.34112];
error_ellipse(C, M);
plot3(0.938134, -1.86434, 5.11178,'r.' );
C = [0.0130633, -0.0258028, 0.0710649; -0.0258028, 0.0515307, -0.141724; 0.0710649, -0.141724, 0.390329];
M = [0.938134;-1.86434; 5.11178];
error_ellipse(C, M);
plot3(0.951814, -1.91715, 5.18124,'r.' );
C = [0.0133491, -0.0268191, 0.0726155; -0.0268191, 0.054479, -0.147306; 0.0726155, -0.147306, 0.398846];
M = [0.951814;-1.91715; 5.18124];
error_ellipse(C, M);
plot3(0.875934, -1.78553, 4.82422,'r.' );
C = [0.0116426, -0.0236626, 0.0640689; -0.0236626, 0.0486208, -0.131471; 0.0640689, -0.131471, 0.355971];
M = [0.875934;-1.78553; 4.82422];
error_ellipse(C, M);
plot3(0.831228, -1.71424, 4.68127,'r.' );
C = [0.0105978, -0.0217932, 0.0596798; -0.0217932, 0.0453236, -0.12395; 0.0596798, -0.12395, 0.339433];
M = [0.831228;-1.71424; 4.68127];
error_ellipse(C, M);
xlabel('x'); ylabel('y'); zlabel('z');