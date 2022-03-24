from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file ('graficado_simple.html')
    fig =figure()

    total_vals = int(input('cuantos valores vas a graficar '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        valores = int(input(f'dame los valores de y para {x} '))
        y_vals.append(valores)
    
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)


    