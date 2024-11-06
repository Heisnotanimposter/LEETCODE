# Drawing the Transformer Network from Scratch (Part 1)

## Overview

The Transformer Neural Networks, commonly referred to as "Transformers," were introduced by a Google-led team in 2017 in the paper titled **"Attention Is All You Need."** This architecture has since been refined and popularized in various applications, particularly in Natural Language Processing (NLP).

This document focuses on the **encoder** part of the Transformer, providing a step-by-step breakdown of its components to help readers develop a mental model of how Transformers operate.

## Key Components of the Transformer Encoder

### 1. Input Representation

A Transformer takes as input a sequence of words, which are represented as vectors. In NLP tasks, a vocabulary (or dictionary) is used, where each word is assigned a unique index. This index can be represented as a **one-hot vector**, predominantly made up of zeros, with a single "one" at the correct index.

- **One-Hot Encoding**: For a vocabulary of size 10, each word is represented as a vector of size 10, where only one position is set to 1.

### 2. Word Embeddings

To reduce the dimensionality of the one-hot encoded vectors, they are multiplied by an **embedding matrix**. The resulting vectors are called **word embeddings**. In the original paper, the size of the word embeddings is 512.

- **Benefit**: Words with similar meanings are positioned close to each other in the embedding space (e.g., "cat" and "kitty").

### 3. Positional Encoding

Since all words are presented to the Transformer simultaneously, the order of words in the input sequence is lost. To address this, the Transformer adds a positional encoding vector to each input embedding, injecting information about the relative or absolute position of each word.

### 4. Keys and Queries

The word embeddings are multiplied by matrices \( W_Q \) and \( W_K \) to obtain **query vectors** and **key vectors**, each of size 64.

### 5. Parallelization

One of the key advantages of the Transformer architecture is its ability to parallelize computations. All word embeddings, query vectors, and key vectors can be computed simultaneously, allowing for efficient processing.

### 6. Dot Products

The dot products of all possible combinations of query vectors and key vectors are calculated. The result is a single number that serves as a weight factor, indicating how much two words at different positions depend on each other. This mechanism is known as **self-attention**.

### 7. Scaling

To stabilize gradients during training, the weight factors are divided by the square root of the dimension of the key vectors (in this case, 8). This prevents the softmax function from entering regions with extremely small gradients.

### 8. Softmax

The scaled factors are passed through a **softmax function**, normalizing them so that they are all positive and sum to 1. This step ensures that the weight factors can be interpreted as probabilities.

### 9. Values

Similar to the computation of query and key vectors, **value vectors** are obtained by multiplying the word embeddings by a matrix \( W_V \). The size of the value vectors is also 64.

### 10. Weighting and Summation

Each value vector is multiplied by its corresponding weight factor. This process allows the model to focus on relevant words while suppressing irrelevant ones. The final output of the self-attention layer is obtained by summing all the weighted value vectors.

### 11. Masking

To handle shorter sequences, padding is used for words that do not contribute to the self-attention calculation. These padded words are masked (set to -inf) before the softmax step, ensuring they do not affect the attention weights.

### 12. Multi-Head Self-Attention

Instead of performing a single self-attention function, multiple self-attention heads are employed, each with different weight matrices. This allows the model to jointly attend to information from different representation subspaces at different positions.

### 13. Add & Normalize

The multi-head self-attention mechanism includes a residual connection and is followed by a layer normalization step, which standardizes the output.

### 14. Feed Forward Network

The output of the self-attention layer is fed into a fully connected feed-forward network, consisting of two linear transformations with a ReLU activation in between. The dimensionality of the input and output is 512, while the inner layer has a dimensionality of 2048.

### 15. Stack of Encoders

The entire encoding component consists of a stack of six identical encoders, each with its own set of weights.

## Conclusion

This document provides a foundational understanding of the encoder part of the Transformer architecture. In the next part, we will cover the decoder component, building upon the concepts introduced here.

## References

- Original Paper: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- The Illustrated Transformer
- Transformers Explained
- Get Busy with Word Embeddings

---