n=100;
v = [0];
for i = 1:n
v = v + (sin(i/n) * (1/n));
end
disp(v);


diceone = 0;
dicetwo = 0;
while diceone < 6 || dicetwo < 6
    diceone = randi(6);
    dicetwo = randi(6);
end
disp(diceone);
disp(dicetwo);