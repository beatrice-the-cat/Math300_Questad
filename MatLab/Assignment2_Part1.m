A = [2 -1 4; 9 6 2; 1 3 8];
B = [1 1 1; 1 1 1; 1 1 1];
x = [3; 6; 8];
y = [5 10 15];
disp("A");
disp(A);
disp("B:");
disp(B);
disp("x:");
disp(x);
disp("y:");
disp(y);
%commented out lines break the rules for
%matrix and vector multiplication (m x n) * (n x p)
%where the number of columns of the first is equal to the number of rows of
%the 2nd, or number of dimensions in the case of a vector

disp("A*B:");
disp(A*B); %3x3 matrix multiplication
disp("A*x:");
disp(A*x); %3x3 matrix 3-dimensional vector multiplication
disp("x'*B:");
disp(x'*B); %1x3 transposed vector 3x3 matrix multiplication

% disp(B*y);

% disp(x*A);
disp("x*y:");
disp(x*y); %3-dimensional vector multiplied by three 1-dimensional points
disp("y*x:");
disp(y*x); %three 1-dimensional points multiplied by 3-dimensional vector

% disp(x*y');
disp("x.*y:");
disp(x.*y);
disp("A.*B:");
disp(A.*B);