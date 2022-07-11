A = [1 1; 1 2; 1 3];
b = [1 5 10];

x = A\b;

disp(x);
disp(A*x);

%this doesn't work as the dimensions don't fit? A is a 3x2 matrix and we're
%trying to multiply it by a 3-dimensional vector