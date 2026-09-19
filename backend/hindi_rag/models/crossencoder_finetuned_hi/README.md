---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:12668
- loss:BinaryCrossEntropyLoss
base_model: BAAI/bge-reranker-v2-m3
pipeline_tag: text-ranking
library_name: sentence-transformers
metrics:
- accuracy
- accuracy_threshold
- f1
- f1_threshold
- precision
- recall
- average_precision
model-index:
- name: CrossEncoder based on BAAI/bge-reranker-v2-m3
  results:
  - task:
      type: cross-encoder-binary-classification
      name: Cross Encoder Binary Classification
    dataset:
      name: Hindi dev
      type: Hindi-dev
    metrics:
    - type: accuracy
      value: 0.7698863636363636
      name: Accuracy
    - type: accuracy_threshold
      value: 0.19721254706382751
      name: Accuracy Threshold
    - type: f1
      value: 0.5030674846625767
      name: F1
    - type: f1_threshold
      value: 0.13296423852443695
      name: F1 Threshold
    - type: precision
      value: 0.3974151857835218
      name: Precision
    - type: recall
      value: 0.6852367688022284
      name: Recall
    - type: average_precision
      value: 0.48003349698840503
      name: Average Precision
---

# CrossEncoder based on BAAI/bge-reranker-v2-m3

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) <!-- at revision 953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e -->
- **Maximum Sequence Length:** 8192 tokens
- **Number of Output Labels:** 1 label
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

### Full Model Architecture

```
CrossEncoder(
  (0): Transformer({'transformer_task': 'sequence-classification', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'logits'}}, 'module_output_name': 'scores', 'architecture': 'XLMRobertaForSequenceClassification'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import CrossEncoder

# Download from the 🤗 Hub
model = CrossEncoder("cross_encoder_model_id")
# Get scores for pairs of inputs
pairs = [
    ['डायपर rash क्या है', 'एक संक्रामक रोग जो व्यक्ति से व्यक्ति में फैलता है'],
    ['गर्भपात क्या है?', 'एक स्वैच्छिक गर्भपात, जिसके विभिन्न कारण हो सकते हैं (जैसे विकृति या बीमारी) ।'],
    ['स्तनपान कराने के दौरान मैं अपनी कम होने की गति कैसे बढ़ा सकता हूँ?', 'स्तन दूध से भरते समय सूजन, कोमल और गर्म महसूस कर सकते हैं। घर्षण से कसकर और धड़कन हो सकती है। प्रबंधन में सहायक ब्रा पहनना, छोटी मात्रा में दूध का व्यक्त करना, ठंडे कंप्रेसेस का उपयोग करना और स्तनपान तकनीक का पालन करना शामिल है।'],
    ['प्रसव के बाद आपात स्थिति में मुझे क्या करना चाहिए?', 'यदि आप पहले जन्म लेते हैं और एक घंटे के लिए नियमित संकुचन होते हैं, या यदि आपके पहले प्रसव होते हैं और आप पहले भी प्रत्येक पांच मिनट या उससे कम समय में संकुचन करते हैं, तो आपको तुरंत अस्पताल या प्रसव केंद्र जाना चाहिए। यदि आप 30 मिनट से अधिक दूर रहते हैं, तो संकुचन होने पर अस्पताल जाएं। इसके अलावा, यदि आपका पानी टूट जाता है, आप रक्त खो रहे हैं, या आप अपने बच्चे को आगे नहीं बढ़ते हैं, तो जाएं। गर्भावस्था के अंत में, यह महत्वपूर्ण है कि आप अपने डॉक्टर या सुशांत से परामर्श करें कि कब जाने का सही समय है, आपके स्वास्थ्य, पिछले प्रसव और अस्पताल से कितनी दूर रहते हैं, जैसे कारकों को ध्यान में रखते हुए।'],
    ['अस्पताल में स्तनपान कराने के दबाव से कैसे बचें?', 'यदि आपका बच्चा शुरू में स्तनपान नहीं कर सकता है, तो आप स्तनपान पंप का उपयोग करके अपना दूध व्यक्त कर सकते हैं। अस्पताल, विशेष रूप से गहन देखभाल वार्ड में, आमतौर पर स्तनपान पंप उपलब्ध होते हैं और आपको दूध व्यक्त करने में मदद कर सकते हैं। चिंता न करें यदि पहली बार केवल कुछ बूंदें निकलती हैं तो नियमित उत्तेजना दूध उत्पादन बढ़ाने की कुंजी है। याद रखें, नवजात शिशुओं के पेट बहुत छोटे होते हैं और शुरुआत में उन्हें केवल थोड़ी मात्रा में दूध की आवश्यकता होती है। अपने बच्चे के करीब रहना या दूध व्यक्त करने से पहले त्वचा-दर-दर में संपर्क करना उत्पादन बढ़ाने में मदद कर सकता है। यदि स्तनपान आपकी प्रारंभिक योजना का हिस्सा नहीं था, तो यह शुरू करने के लिए बहुत देर नहीं है। इसके अलावा, यदि आवश्यक हो तो आपके बच्चे की जरूरतों के लिए अतिरिक्त खनिज पदार्थ या कैलोरी आपके दूध में जोड़ी जा सकती हैं।'],
]
scores = model.predict(pairs)
print(scores)
# [0.0777 0.1314 0.1593 0.1767 0.1851]

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    'डायपर rash क्या है',
    [
        'एक संक्रामक रोग जो व्यक्ति से व्यक्ति में फैलता है',
        'एक स्वैच्छिक गर्भपात, जिसके विभिन्न कारण हो सकते हैं (जैसे विकृति या बीमारी) ।',
        'स्तन दूध से भरते समय सूजन, कोमल और गर्म महसूस कर सकते हैं। घर्षण से कसकर और धड़कन हो सकती है। प्रबंधन में सहायक ब्रा पहनना, छोटी मात्रा में दूध का व्यक्त करना, ठंडे कंप्रेसेस का उपयोग करना और स्तनपान तकनीक का पालन करना शामिल है।',
        'यदि आप पहले जन्म लेते हैं और एक घंटे के लिए नियमित संकुचन होते हैं, या यदि आपके पहले प्रसव होते हैं और आप पहले भी प्रत्येक पांच मिनट या उससे कम समय में संकुचन करते हैं, तो आपको तुरंत अस्पताल या प्रसव केंद्र जाना चाहिए। यदि आप 30 मिनट से अधिक दूर रहते हैं, तो संकुचन होने पर अस्पताल जाएं। इसके अलावा, यदि आपका पानी टूट जाता है, आप रक्त खो रहे हैं, या आप अपने बच्चे को आगे नहीं बढ़ते हैं, तो जाएं। गर्भावस्था के अंत में, यह महत्वपूर्ण है कि आप अपने डॉक्टर या सुशांत से परामर्श करें कि कब जाने का सही समय है, आपके स्वास्थ्य, पिछले प्रसव और अस्पताल से कितनी दूर रहते हैं, जैसे कारकों को ध्यान में रखते हुए।',
        'यदि आपका बच्चा शुरू में स्तनपान नहीं कर सकता है, तो आप स्तनपान पंप का उपयोग करके अपना दूध व्यक्त कर सकते हैं। अस्पताल, विशेष रूप से गहन देखभाल वार्ड में, आमतौर पर स्तनपान पंप उपलब्ध होते हैं और आपको दूध व्यक्त करने में मदद कर सकते हैं। चिंता न करें यदि पहली बार केवल कुछ बूंदें निकलती हैं तो नियमित उत्तेजना दूध उत्पादन बढ़ाने की कुंजी है। याद रखें, नवजात शिशुओं के पेट बहुत छोटे होते हैं और शुरुआत में उन्हें केवल थोड़ी मात्रा में दूध की आवश्यकता होती है। अपने बच्चे के करीब रहना या दूध व्यक्त करने से पहले त्वचा-दर-दर में संपर्क करना उत्पादन बढ़ाने में मदद कर सकता है। यदि स्तनपान आपकी प्रारंभिक योजना का हिस्सा नहीं था, तो यह शुरू करने के लिए बहुत देर नहीं है। इसके अलावा, यदि आवश्यक हो तो आपके बच्चे की जरूरतों के लिए अतिरिक्त खनिज पदार्थ या कैलोरी आपके दूध में जोड़ी जा सकती हैं।',
    ]
)
# [{'corpus_id': ..., 'score': ...}, {'corpus_id': ..., 'score': ...}, ...]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Cross Encoder Binary Classification

* Dataset: `Hindi-dev`
* Evaluated with [<code>CEBinaryClassificationEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CEBinaryClassificationEvaluator)

| Metric                | Value    |
|:----------------------|:---------|
| accuracy              | 0.7699   |
| accuracy_threshold    | 0.1972   |
| f1                    | 0.5031   |
| f1_threshold          | 0.133    |
| precision             | 0.3974   |
| recall                | 0.6852   |
| **average_precision** | **0.48** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 12,668 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                        | sentence_1                                                                          | label                                                          |
  |:---------|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type     | string                                                                            | string                                                                              | float                                                          |
  | modality | text                                                                              | text                                                                                |                                                                |
  | details  | <ul><li>min: 7 tokens</li><li>mean: 20.54 tokens</li><li>max: 61 tokens</li></ul> | <ul><li>min: 12 tokens</li><li>mean: 70.12 tokens</li><li>max: 245 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.24</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                      | sentence_1                                                                                                                                                                                                                                        | label            |
  |:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>डायपर rash क्या है</code>                                                 | <code>एक संक्रामक रोग जो व्यक्ति से व्यक्ति में फैलता है</code>                                                                                                                                                                                   | <code>0.0</code> |
  | <code>गर्भपात क्या है?</code>                                                   | <code>एक स्वैच्छिक गर्भपात, जिसके विभिन्न कारण हो सकते हैं (जैसे विकृति या बीमारी) ।</code>                                                                                                                                                       | <code>0.0</code> |
  | <code>स्तनपान कराने के दौरान मैं अपनी कम होने की गति कैसे बढ़ा सकता हूँ?</code> | <code>स्तन दूध से भरते समय सूजन, कोमल और गर्म महसूस कर सकते हैं। घर्षण से कसकर और धड़कन हो सकती है। प्रबंधन में सहायक ब्रा पहनना, छोटी मात्रा में दूध का व्यक्त करना, ठंडे कंप्रेसेस का उपयोग करना और स्तनपान तकनीक का पालन करना शामिल है।</code> | <code>0.0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": null
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 2
- `fp16`: True
- `per_device_eval_batch_size`: 2

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 2
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 2
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch  | Step | Training Loss | Hindi-dev_average_precision |
|:------:|:----:|:-------------:|:---------------------------:|
| 0.0789 | 500  | 1.0523        | 0.4800                      |


### Training Time
- **Training**: 4.2 minutes

### Framework Versions
- Python: 3.13.15
- Sentence Transformers: 5.7.0
- Transformers: 5.16.1
- PyTorch: 2.11.0+cu128
- Accelerate: 1.14.0
- Datasets: 4.8.5
- Tokenizers: 0.23.1

## Additional Resources

- [Training and Finetuning Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-reranker): the end-to-end guide for training or finetuning Cross Encoder (reranker) models.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video reranker models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal Cross Encoders.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->