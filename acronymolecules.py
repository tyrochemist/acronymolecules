import random


def create_acronym():
    """A function to create fun molecule names from an acronym"""

    acronym = input("Input upper case molecular acronym: ")
    acronym_letters = list(acronym)

    a_word = ['amine', 'acetate', 'alumnium']
    b_word = ['butyl', 'boron']
    c_word = ['cyclo', 'chloro', 'carbo']
    d_word = ['di', 'deoxy']
    e_word = ['ethyl', 'ethoxide', 'engegen']
    f_word = ['furan', 'formamide', 'fluoride']
    g_word = ['glycero', 'glycol', 'glycine']
    h_word = ['hexa', 'hydro', 'hydroxy']
    i_word = ['iso', 'imide']
    j_word = ['jodo', 'jolly']
    k_word = ['potassium', 'ketone']
    l_word = ['lithium', 'lead']
    m_word = ['methyl', 'methoxy', 'malono', 'meta']
    n_word = ['nitro', 'n-', 'nonane']
    o_word = ['oxy', 'oxide', 'oxirane']
    p_word = ['pyrdinium', 'pyrrolidone', 'phenyl', 'phosphoric']
    q_word = ['quino']
    r_word = ['ribo', 'ribulo']
    s_word = ['sulfide', 'silazide', 'silyl']
    t_word = ['thio', 'tri', 'toluene']
    u_word = ['urea', 'undec-7-ene']
    v_word = ['vinyl']
    w_word = ['tryptophan', 'tungsten']
    x_word = ['xylo', 'xylulo']
    y_word = ['yotta']
    z_word = ['z-', 'zusammen', 'zeta']

    print(*acronym_letters)

    letter_dict = {
        'A': a_word,
        'B': b_word,
        'C': c_word,
        'D': d_word,
        'E': e_word,
        'F': f_word,
        'G': g_word,
        'H': h_word,
        'I': i_word,
        'J': j_word,
        'K': k_word,
        'L': l_word,
        'M': m_word,
        'N': n_word,
        'O': o_word,
        'P': p_word,
        'Q': q_word,
        'R': r_word,
        'S': s_word,
        'T': t_word,
        'U': u_word,
        'V': v_word,
        'W': w_word,
        'X': x_word,
        'Y': y_word,
        'Z': z_word,
    }

    fullword = ''

    for i in acronym_letters:
        word_1 = random.choice(letter_dict[i])
        print(i+' word is: ' + word_1)
        fullword += word_1

    print("Your acronym stands for: "+fullword)
