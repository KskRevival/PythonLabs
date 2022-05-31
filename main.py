import random as r
import algos
import benchmark
import plotbuilder
import textgen

if __name__ == '__main__':
    x = []  # Needle length
    is_time = True
    runners = {'Standard': plotbuilder.PlotFunc('Standard', 'b*'),
               'Rabin': plotbuilder.PlotFunc('Rabin', 'g^'),
               'Bauer': plotbuilder.PlotFunc('Bauer', 'm<'),
               'KMP': plotbuilder.PlotFunc("KMP", 'rs'),
               'Aho': plotbuilder.PlotFunc('Aho', 'yP')}

    for i in range(7, 20):
        (hay, needle) = textgen.get_fixed_text(r.randint(2 ** (i - 7),
                                                         2 ** (i - 3)), 10000)
        for (key, value) in runners.items():
            value.res.append(benchmark.test(algos.algos[key],
                                            hay, needle, is_time))
        x.append(i)

    plotbuilder.draw(is_time, x, runners.values())
