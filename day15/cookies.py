class Ingredient:
    def __init__(self, cap, dur, fla, tex, cal):
        self.cap = cap
        self.dur = dur
        self.fla = fla
        self.tex = tex
        self.cal = cal

    def __repr__(self):
        return(f"capacity: {self.cap}; durability: {self.dur}; \
flavor: {self.fla}; texture: {self.tex}; calories: {self.cal}"
        )
    
    def get_props(self):
        return [self.cap, self.dur, self.fla, self.tex, self.cal]

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    ingredients = []
    for l in lines:
        l = l.split()
        ingredients.append(
            Ingredient(
                cap = int(l[2][:-1]),
                dur = int(l[4][:-1]),
                fla = int(l[6][:-1]),
                tex = int(l[8][:-1]),
                cal = int(l[10])
            )
        )
    max_score = 0
    cal_score = 0
    i_ing, j_ing, k_ing, l_ing = ingredients
    i_cap, i_dur, i_fla, i_tex, i_cal = i_ing.get_props()
    j_cap, j_dur, j_fla, j_tex, j_cal = j_ing.get_props()
    k_cap, k_dur, k_fla, k_tex, k_cal = k_ing.get_props()
    l_cap, l_dur, l_fla, l_tex, l_cal = l_ing.get_props()
    for i in range(1,101):
        for j in range(1,101):
            for k in range(1,101):
                for l in range(1,101):
                    if i+j+k+l != 100:
                        continue
                    this_score = \
                    max([0,(i*i_cap + j*j_cap + k*k_cap + l*l_cap)]) * \
                    max([0,(i*i_dur + j*j_dur + k*k_dur + l*l_dur)]) * \
                    max([0,(i*i_fla + j*j_fla + k*k_fla + l*l_fla)]) * \
                    max([0,(i*i_tex + j*j_tex + k*k_tex + l*l_tex)])
                    calories = (i*i_cal + j*j_cal + k*k_cal + l*l_cal)
                    max_score = max([this_score, max_score])
                    if calories == 500:
                        cal_score = max([this_score, cal_score])

    print(max_score)
    print(cal_score)

