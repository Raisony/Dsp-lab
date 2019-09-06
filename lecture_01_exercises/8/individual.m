clear
[x,fs] = audioread('3channels.wav');

subplot(2,2,1)
plot(x(:,1))
xlim([0,100])
xlabel('Time (sample)')
title('channel 1')

subplot(2,2,2)
plot(x(:,2))
xlim([0,100])
xlabel('Time (sample)')
title('channel 2')

subplot(2,2,3)
plot(x(:,3))
xlim([0,100])
xlabel('Time (sample)')
title('channel 3')

print -dpdf plot_of_3_individual_channels1