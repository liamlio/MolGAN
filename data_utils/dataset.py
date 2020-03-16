from torch.utils import data
import numpy as np

#This dataset assumes it will be given an np.array containing the latent space vectors
class LatentMolsDataset(data.Dataset):
    def __init__(self, latent_space_mols):
        self.data = latent_space_mols

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]
