function yy = Hvapor(x)

xx=[5:5:370];
xx(end+1)=373;
y=[2509.7 2518.9 2528.0 2537.2 2546.3 2555.3 2564.4 2573.4 2582.3 ...
    2591.2 2600 2608.8 2617.5 2626.1 2634.6 2643.1 2651.4 2659.6 ...
    2667.7 2675.7 2683.6 2691.3 2698.8 2706.2 2713.4 2720.4 2727.2 ...
    2733.8 2740.2 2746.4 2752.3 2758 2763.3 2768.5 2773.3 2777.8 2782 ...
    2785.8 2789.4 2792.5 2795.3 2797.7 2799.7 2801.3 2802.4 2803.1 ...
    2803.3 2803 2802 2800.7 2798.8 2796.2 2793 2789.1 2784.5 2779.2 ...
    2773 2765.9 2757.8 2748.7 2738.5 2727 2714.2 2699.7 2683.5 2665.3 ...
    2644.7 2621.3 2594.5 2563.5 2526.7 2482 2424.6 2340.2 2086];
yy= spline(xx,y,x);