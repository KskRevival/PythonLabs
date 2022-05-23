import matplotlib.pyplot as plt


def draw(x, standard, rabin, bauer, res_kmp):
    ax1 = plt.figure(figsize=(12, 7)).add_subplot(111)

    plt.plot(x, standard, 'b*', alpha=0.7, label="Standard", mew=2, ms=10)
    plt.plot(x, rabin, 'g^', alpha=0.7, label="Rabin Karp", mew=2, ms=10)
    plt.plot(x, bauer, 'rs', alpha=0.7, label="Bauer Moore", mew=2, ms=10)
    plt.plot(x, res_kmp, 'cD', alpha=0.7, label="KMP", mew=2, ms=10)

    plt.legend()
    ax1.set_title(u'Time By Needle Length')
    plt.xlabel(u'Needle length [2^n]', fontsize=12)
    plt.ylabel(u'Time [ms]', fontsize=12)
    plt.grid(True)
    plt.show()
