# MolGAN
AI for a cure, a combination of Latent-GAN and VAE-JTNN to create 100% valid drug like molecules

Models, trainer and data_utils modified from original [LatentGan](https://github.com/Dierme/latent-gan)

Encoder and decoder for VAE-JTNN modified from [Mol-CycleGAN](https://github.com/ardigen/mol-cycle-gan)

Pretrained latent space also used from Mol-CycleGAN, and used pretrained decoder wieghts from [VAE-JTNN repository](https://github.com/wengong-jin/icml18-jtnn)

# I recommend using the models in a jupyter notebook and to get the required data set using:
```
!wget http://molcyclegan.ardigen.com/X_JTVAE_250k_rndm_zinc.csv
```

For training, you can directly run the notebook within the repository.
Although you can decode the sampled_epoch200.npy file (it contains 10 samples), I recommend training from scratch due to the lack of time to train the model enough prior to the deadline.

# Then due to environment constraints and requirements of the original VAE-JTNN repository, create the required environment using conda:
```
conda create env -f environment.py
```
# Be sure to git clone the original vae-jtnn repository into the folder:
```
git clone https://github.com/wengong-jin/icml18-jtnn.git
```
# Then just use:
```
python decode.py
```
Check at the bottom of the decode.py file for specifics on fields to set data path and file to decode path

The output will be a data files containing SMILES of the decoded molecules create by the MolGAN model

