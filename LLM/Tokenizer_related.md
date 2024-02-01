### Tokenizer


#### Types of Tokenizer
- [huggingface tokenizer explained](https://huggingface.co/docs/transformers/tokenizer_summary)
  - word level
  - character level
  - subword level
    - Byte-pair encoding: based on the character combined to get most frequent pairs
    - Wordpiece: similair to BPE, but not get most frequent but to maximizes the likelihood of data
    - Unigram:
    - SentencePiece: words order matters, and could be combined as the one, like chinese