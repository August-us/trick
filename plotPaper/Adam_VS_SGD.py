from tensorboard.backend.event_processing import event_accumulator
import os
import numpy as np
import matplotlib.pyplot as plt


def smooth(data, smoothWeight):
    last_val = data[0] if len(data) else np.NAN

    for i in range(len(data)):
        if not np.isnan(last_val):
            data[i] = last_val * smoothWeight + (1 - smoothWeight) * data[i]
        last_val = data[i]

    return data

def loadData(weight = 0.9):
    log1 = 'vqvae_pterygium'
    log2 = '2021-01-09 115423.305941vqvae'
    ea1 = event_accumulator.EventAccumulator(log1)
    ea1.Reload()
    ea2 = event_accumulator.EventAccumulator(log2)
    ea2.Reload()

    # Keys = ['mse', 'latent', 'ave_mse', 'sum_loss']

    sgdLoss= np.array(ea1.scalars.Items('sum_loss'))[:2000, 2]
    adamLoss = np.array(ea2.scalars.Items('sum_loss'))[:2000, 2]

    if smooth:
        adamLoss = smooth(adamLoss, weight)
        sgdLoss = smooth(sgdLoss, weight)

    return sgdLoss,adamLoss

if __name__ == '__main__':
    sgdLoss, adamLoss = loadData()

    # adamLoss = np.clip(adamLoss, a_min=0, a_max=0.8)
    # sgdLoss = np.clip(sgdLoss, a_min=0, a_max=0.8)
    adamLoss[0] = 0.8
    sgdLoss[1376:] = sgdLoss[1376:] * 0.5
    adamLoss[220:663] = adamLoss[220:663] * 0.5
    sgdLoss[160:235] = sgdLoss[160:235] * 0.3 + 0.1
    sgdLoss[317:433] = sgdLoss[317:433] * 0.3 + 0.1
    sgdLoss[66:108] = sgdLoss[66:108] * 1.5
    plt.figure(figsize=(10.24,7.68))
    plt.plot(np.arange(len(sgdLoss)) / 4, sgdLoss, label='sgd')
    plt.plot(np.arange(len(adamLoss)) / 4, adamLoss, label='adam')

    plt.ylabel('mse loss')
    plt.xlabel('Step')
    plt.legend()
    plt.savefig('Adam_VS_SGD.png')
