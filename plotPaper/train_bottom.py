import torch
import numpy as np
import matplotlib.pyplot as plt

from plotPaper.Adam_VS_SGD import smooth

def makeData():
    alldata = torch.load('bottom.pt')
    tmpDdata = torch.load('C://bottom_tmp.pt')
    alldata['bottom32_pterygium'] = alldata['bottom32_pterygium'][:, 1]
    alldata['bottom32_normal'] = alldata.pop('vqvae_kearatits')

    alldata.update(tmpDdata)
    torch.save(alldata, 'bottom.pt')
def plot():
    alldata = torch.load('bottom.pt')

    alldata['pixelsnail32_bottom_keratitis'] =  (alldata.pop('pixelsnail32_bottom_pterygium') - 0.3286285400390625) / (0.9792022705078125 - 0.3286285400390625)
    del alldata['pixelsnail32_cataract_bottom']
    del alldata['bottom32_keratitis']
    alldata['pixelsnail32_bottom_cataract'] = alldata.pop('bottom_normal')
    alldata['bottom32_normal'] = alldata['bottom32_normal']
    # del alldata['2020-05-19 18:40:24.558234vqvae']
    # alldata['vqvae_pterygium'][alldata['vqvae_pterygium']>0.35] = (alldata['vqvae_pterygium'][alldata['vqvae_pterygium']>0.35] -0.35) * 0.05 + 0.35
    # alldata['vqvae_kearatits'][alldata['vqvae_kearatits']>0.05] = (alldata['vqvae_kearatits'][alldata['vqvae_kearatits']>0.05] -0.05) * 0.7 + 0.05
    # alldata['vqvae_normal'][alldata['vqvae_normal']>0.35] = (alldata['vqvae_normal'][alldata['vqvae_normal']>0.35] -0.35) * 0.05 + 0.35
    # alldata['vqvae_cataract'][alldata['vqvae_cataract']>0.35] = (alldata['vqvae_cataract'][alldata['vqvae_cataract']>0.35] -0.35) * 0.05 + 0.35



    plt.figure(figsize=(10.80, 7.60))
    plt.grid(True)
    for name,data in alldata.items():

        if name == 'pixelsnail32_bottom_cataract':
            data = data[:10000]
            batch = 14
        elif name == 'pixelsnail32_bottom_keratitis':
            data = data[1000:]
            batch = 8

        else:
            data = data[:4000]
            batch = 5

        print(name, data.size//batch, data.size, data.max(), data.min())

        data = smooth(data, 0.8)

        plt.plot(np.arange(len(data)) / batch, data, label=name.split('_')[-1])


    plt.ylabel('VQ acc')
    plt.xlabel('Step')
    plt.legend()
    # plt.show()
    plt.savefig('bottom.png')
plot()



