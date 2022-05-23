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
    
    for i in range(7, 20):
        (hay, needle) = textgen.get_fixed_text(r.randint(2 ** (i - 7), 2 ** (i - 3)), 100000)
        isTime = False
        standard.append(benchmark.test(algos.standard_search, hay, needle, isTime))
        rabin.append(benchmark.test(algos.rabin_karp, hay, needle, isTime))
        bauer.append(benchmark.test(algos.bauer_moore, hay, needle, isTime))
        kmp.append(benchmark.test(algos.kmp, hay, needle, isTime))
        x.append(i)
        
    plotbuilder.draw(x, standard, rabin, bauer, kmp)
