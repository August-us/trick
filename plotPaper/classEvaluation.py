import numpy as np
import matplotlib.pyplot as plt


def plot_confusion_matrix(cm, savename=None, title='Confusion Matrix', classes=None, colorBar=True):
    if classes is None:
        classes = np.arange((len(cm)))+1
    plt.figure(figsize=(10.24, 7.56), dpi=100)
    np.set_printoptions(precision=2)

    # 在混淆矩阵中每格的概率值
    ind_array = np.arange(len(classes))
    x, y = np.meshgrid(ind_array, ind_array)
    for x_val, y_val in zip(x.flatten(), y.flatten()):
        c = cm[y_val][x_val]
        if c > 0.001:
            plt.text(x_val, y_val, "%0.2f" % (c,), color='red', fontsize=15, va='center', ha='center')

    plt.imshow(cm, interpolation='nearest', cmap='GnBu')
    # plt.title(title)
    if colorBar:
        plt.colorbar()
    xlocations = np.array(range(len(classes)))
    plt.xticks(xlocations, classes, rotation=90,fontsize=14)
    plt.yticks(xlocations, classes,fontsize=14)
    plt.ylabel('Actual label', fontdict={'size':14})
    plt.xlabel('Predict label', fontdict={'size':14})

    # offset the tick
    tick_marks = np.array(range(len(classes))) + 0.5
    plt.gca().set_xticks(tick_marks, minor=True)
    plt.gca().set_yticks(tick_marks, minor=True)
    plt.gca().xaxis.set_ticks_position('none')
    plt.gca().yaxis.set_ticks_position('none')
    plt.grid(True, which='minor', linestyle='-')
    plt.gcf().subplots_adjust(bottom=0.15)

    # show confusion matrix
    if savename is not None:
        plt.savefig(savename, format='png')
    else:
        plt.show()

def plot_generation():
    print(np.mean([0.96153846, 0.9591837, 0.9019608, 0.9375    ]))
    print(np.mean([1.  , 0.92, 0.94, 0.9 ]))
    cm = [[50,  0,  0,  0], [ 0, 47,  2,  1],[ 2,  0, 46,  2],[ 0,  2,  3, 45]]

    cls_list = ['cataract', 'keratitis', 'normal', 'pterygium']

    plot_confusion_matrix(cm, classes=cls_list, colorBar=False)

def plot_ture_all():
    print(np.mean([0.94339623, 0.96      , 0.90384615, 0.97777778]))
    print(np.mean([1.  , 0.96, 0.94, 0.88]))
    cm = [[50,  0,  0,  0],
       [ 1, 48,  1,  0],
       [ 2,  0, 47,  1],
       [ 0,  2,  4, 44]]

    cls_list = ['cataract', 'keratitis', 'normal', 'pterygium']

    plot_confusion_matrix(cm, classes=cls_list)

def plot_true_part():
    print(np.mean([0.96153846, 0.97727273, 0.89795918, 0.85454545]))
    print(np.mean([1.  , 0.86, 0.88, 0.94]))
    cm = [[50,  0,  0,  0],[ 0, 43,  3,  4],[ 2,  0, 44,  4],[ 0,  1,  2, 47]]

    cls_list = ['cataract', 'keratitis', 'normal', 'pterygium']

    plot_confusion_matrix(cm, classes=cls_list, colorBar=False)

# plot_true_part()
# plot_generation()
# plot_ture_all()




