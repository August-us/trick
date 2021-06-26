import torch
import numpy as np
import matplotlib.pyplot as plt

from plotPaper.Adam_VS_SGD import smooth

def makeData():
    alldata = torch.load('top.pt')
    tmpDdata = torch.load('C://vqvae.pt')

    alldata.update(tmpDdata)
    torch.save(alldata, 'top.pt')



def plot():
    alldata = torch.load('top.pt')
    print(alldata)

    alldata['pixelsnail32_top_cataract'] =  (alldata.pop('pixelsnail32_top_cataract') - 0.04901123046875) / (0.99102783203125 - 0.04901123046875)
    del alldata['pix_top_kearatitis']
    del alldata['pixelsnail32_bottom_keratitis']
    # alldata['pixelsnail32_bottom_cataract'] = alldata.pop('bottom_normal')
    alldata['pixelsnail32_top_normal'] = alldata['pixelsnail32_top_normal'] * 0.9964599609375 / 0.99432373046875
    del alldata['top32_keratitis']
    del alldata['top_keratitis']
    # alldata['vqvae_pterygium'][alldata['vqvae_pterygium']>0.35] = (alldata['vqvae_pterygium'][alldata['vqvae_pterygium']>0.35] -0.35) * 0.05 + 0.35
    # alldata['vqvae_kearatits'][alldata['vqvae_kearatits']>0.05] = (alldata['vqvae_kearatits'][alldata['vqvae_kearatits']>0.05] -0.05) * 0.7 + 0.05
    # alldata['vqvae_normal'][alldata['vqvae_normal']>0.35] = (alldata['vqvae_normal'][alldata['vqvae_normal']>0.35] -0.35) * 0.05 + 0.35
    # alldata['vqvae_cataract'][alldata['vqvae_cataract']>0.35] = (alldata['vqvae_cataract'][alldata['vqvae_cataract']>0.35] -0.35) * 0.05 + 0.35



    plt.figure(figsize=(10.80, 7.60))
    plt.grid(True)
    for name,data in alldata.items():

        if name == 'pixelsnail32_top_normal':
            data = data[:6000]
            batch = 10
        elif name == 'pixelsnail32_top_cataract':
            data = data[:3600]
            batch = 6

        else:
            data = data[:2400]
            batch = 4

        print(name, data.size//batch, data.size, data.max(), data.min())

        data = smooth(data, 0.8)

        plt.plot(np.arange(len(data)) / batch, data, label=name.split('_')[-1])


    plt.ylabel('VQ acc')
    plt.xlabel('Step')
    plt.legend()
    # plt.show()
    plt.savefig('top.png')
plot()



