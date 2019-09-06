function filter_gui_example_ver1

N = 50;
n = 1:N;
x = sin(5*pi*n/N) + randn(1, N);  % Input signal
imp = [1 zeros(1, N)];
a = [1 -1.9 0.998];
b = [1 0.998 0]
h = filter(b, a, imp);





figure(1)
clf

title('Impulse response');
xlabel('Time (sec)')
zoom xon



title('Noisy data', 'fontsize', 12 )
xlabel('Time')
box off
xlim([0, N]);
ylim([-3 3])

drawnow;

slider_handle = uicontrol('Style', 'slider', ...
    'Min', 0.005, 'Max', 0.4,...
    'Value', 0.2, ...
    'SliderStep', [0.02 0.05], ...
    'Position', [5 5 200 20], ...           % [left, bottom, width, height]
    'Callback',  {@fun1, line_handle, x}    );

end


function fun1(hObject, eventdata, line_handle, x)

fc = get(hObject, 'Value');  % fc : cut-off frequency

[b, a] = butter(2, fc);     % Order-2 Butterworth filter
y = filtfilt(b, a, x);

set(line_handle, 'ydata',  y);        % Update data in figure

title( sprintf('Output of LPF. Cut-off frequency = %.3f', fc), 'fontsize', 12 )

end

