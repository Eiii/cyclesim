from matplotlib import pyplot as plt

def land_turns_dist(anal, output):
    fig, ax = plt.subplots(figsize=(8, 4), dpi=200)
    turns = {t for t, _ in anal.keys()}
    f = 0.8
    w = 1/len(turns)
    for idx, turn in enumerate(sorted(list(turns))):
        land_counts = [l for t, l in anal.keys() if t==turn]
        probs = [anal[(turn, x)] for x in land_counts]
        xs = [x+f*(w*idx-0.5) for x in land_counts]
        rects = ax.bar(xs, probs, w, label=f'Turn#{turn}')
        labels = [f'{100*p:.2f}' for p in probs]
        for rect, label in zip(rects, labels):
            ax.text(rect.get_x()+rect.get_width()/2, rect.get_height(),
                    label, ha='center', va='bottom', rotation=90, fontsize=8)
    ax.legend(loc='center left')
    ax.set_xlabel('# lands played')
    ax.set_ylim(0, 1.2)
    fig.savefig(output)

