# pytorch-pqrnn
refactoring to pytorch from https://github.com/tensorflow/models/tree/master/research/sequence_projection

To-dos:
1. 13/10/20 - WIP on Prado tf/C/cpp code to pytorch implementation
   1. But first, from tf_ops, gotta change:
      - [ ] projection_normalizer_util
      - [ ] projection_tokenizer_util
      - [ ] projection_util
      - [ ] sequence_string_projection
      - [ ] text_distorter
      - [ ] expected_value
      - [ ] quantization_util
2. Bidirectional QRNN

pQRNN building blocks:
1. projection operator layer (prado)
    - From the PRADO paper, section 3.1:
      - words is mapped to embedding matrix modeled with dirac delta function 
2. dense bottleneck layer
3. stack of bidirectional QRNN encoders

Notes:
- train and test data is from https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data?select=all_data.csv 
- qrnn is not in the sequence_projection repo, will be taken from https://github.com/salesforce/pytorch-qrnn (not bidirectional)
- direct usage of torch.quantization (pytorch 1.6.0), subject to change
- feel free to contribute

Disclaimer:
- this implementation can be totally wrong, still waiting for TF2/Keras implementation from original paper/author.

