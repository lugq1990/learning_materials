## accelerate


### hands on with accelerate

[how to use accelerate for distributed training](https://huggingface.co/docs/transformers/en/accelerate)

    In summary:

    ```python
    train_dataloader, eval_dataloader, model, optimizer = accelerator.prepare(
    train_dataloader, eval_dataloader, model, optimizer
    )
    ```

    Convert the data, model, optimizer with `accelerate`.