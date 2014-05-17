'''
Created on Dec 29, 2013

@author: Mindaugas Greibus
'''
import sys, os

#sys.path.insert(0, '/home/mondhs/tmp/pocketsphinx-bin/usr/local/lib/python2.7/dist-packages/sphinxbase')
#sys.path.insert(0, '/home/mondhs/tmp/pocketsphinx-bin/usr/local/lib/python2.7/dist-packages/pocketsphinx')


from pocketsphinx import Decoder

MODELDIR = "../models"
#MODELDIR = "/home/as/src/speech/sphinx/lt-pocketsphinx-tutorial/impl/models"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(MODELDIR, 'hmm/lt.cd_cont_200/'))
config.set_string('-jsgf', os.path.join(MODELDIR, 'lm/robotas.gram'))
config.set_string('-dict', os.path.join(MODELDIR, 'dict/robotas.dict'))
decoder = Decoder(config)

decoder.decode_raw(open(os.path.join(MODELDIR, '../test/audio/varyk_pirmyn-16k.wav'), 'rb'))

# Retrieve hypothesis.
hypothesis = decoder.hyp()
print ('Best hypothesis: ', hypothesis.best_score, hypothesis.hypstr)
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])


