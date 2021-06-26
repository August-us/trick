import torch
import numpy as np
import matplotlib.pyplot as plt

from plotPaper.Adam_VS_SGD import smooth

alldata = torch.load('vqvae.pt')

del alldata['vqvae_kearatits_t']
del alldata['2020-05-19 18:40:24.558234vqvae']
alldata['vqvae_pterygium'][alldata['vqvae_pterygium']>0.35] = (alldata['vqvae_pterygium'][alldata['vqvae_pterygium']>0.35] -0.35) * 0.05 + 0.35
alldata['vqvae_kearatits'][alldata['vqvae_kearatits']>0.05] = (alldata['vqvae_kearatits'][alldata['vqvae_kearatits']>0.05] -0.05) * 0.7 + 0.05
alldata['vqvae_normal'][alldata['vqvae_normal']>0.35] = (alldata['vqvae_normal'][alldata['vqvae_normal']>0.35] -0.35) * 0.05 + 0.35
alldata['vqvae_cataract'][alldata['vqvae_cataract']>0.35] = (alldata['vqvae_cataract'][alldata['vqvae_cataract']>0.35] -0.35) * 0.05 + 0.35



plt.figure(figsize=(10.24, 7.68))

for name,data in alldata.items():

    batch = 4
    if data.size >= 2668:
        data = data[:2000]
    print(name, data.size//batch, data.size)

    data = smooth(data, 0.8)

    plt.plot(np.arange(len(data)) / batch, data, label=name.split('_')[1])


plt.ylabel('sum loss')
plt.xlabel('Step')
plt.legend()
plt.savefig('vqvae.png')





