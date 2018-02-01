#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:18:07 2017

@author: Andrea Argudo
"""

# Obtener el espectograma de un audio en wav de normoyentes e hipoacusicos (muestra)

import matplotlib.pyplot as plt
from scipy.io import wavfile

def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    nfft = 256  # Length of the windowing segments
    fs = 44100    # Sampling frequency
    pxx, freqs, bins, im = plt.specgram(data, nfft,fs)
    plt.axis('on')
        
    plt.savefig('/Users/Andrea/AnacondaProjects/Lab5/SpectrogramFrases.png',
                dpi=300, # Dots per inch
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0) # Spectrogram saved as a .png 
    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.title('Patient: prueba_658140, Sentence: 1' )
    plt.show()

# paciente aleatorio:/Users/Andrea/AnacondaProjects/Pacientes_audios_2017_2018/658140.wav
# frase sin ruido: la mujer limpiaba el suelo todos los días
    
    
    plt.savefig('/Users/Andrea/AnacondaProjects/Lab5/SpectrogramFrases.png.png',
                dpi=300, # Dots per inch
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0)
    plt.plot(data, 'y' , linestyle = '-',linewidth = 0.5 )
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.title('Patient:prueba_658140 , Sentence: 1')
    plt.show()
    

def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data
    
if __name__ == '__main__': # Main function
    wav_file = '/Users/Andrea/AnacondaProjects/Lab5/prueba_658140_procesada.wav' # Filename of the wav file
    graph_spectrogram(wav_file)
    
