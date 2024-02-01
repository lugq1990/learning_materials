## LLM inference


### Frameworks to SERVE

- [vLLM](https://docs.vllm.ai/en/latest/)
  - easy to use LLM inference and servering
    - transformers supported
    - GPUs and distributed model serving
    - State-of-the-art serving throughput
    - query and value memory for PagedAttention
  - with pip to install `pip install vllm`



### Attention otpimization

#### PageAttention
Key insight:

How to better use of GPU memory for better inference.

- [PageAttention and vLLM comparation](https://zhuanlan.zhihu.com/p/638468472)
- [Transformers page attention](https://huggingface.co/docs/text-generation-inference/conceptual/paged_attention)