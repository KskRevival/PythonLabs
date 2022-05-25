import random as r
import algos
import benchmark
import plotbuilder
import textgen

if __name__ == '__main__':
    x = []  # Needle length
    standard = []
    rabin = []
    bauer = []
    kmp = []
    aho = []
    is_time = True

    for i in range(7, 20):
        (hay, needle) = textgen.get_fixed_text(r.randint(2 ** (i - 7), 2 ** (i - 3)), 10000)
        standard.append(benchmark.test(algos.standard_search, hay, needle, is_time))
        rabin.append(benchmark.test(algos.rabin_karp, hay, needle, is_time))
        bauer.append(benchmark.test(algos.bauer_moore, hay, needle, is_time))
        kmp.append(benchmark.test(algos.kmp, hay, needle, is_time))
        aho.append(benchmark.test(algos.aho, hay, needle, is_time))
        x.append(i)

    plotbuilder.draw(is_time, x,
                     [plotbuilder.PlotFunc("Standard", standard, 'b*'),
                      plotbuilder.PlotFunc("Rabin", rabin, 'g^'),
                      plotbuilder.PlotFunc("Bauer", bauer, 'm<'),
                      plotbuilder.PlotFunc("KMP", kmp, 'rs'),
                      plotbuilder.PlotFunc("Aho", aho, 'yP')])
