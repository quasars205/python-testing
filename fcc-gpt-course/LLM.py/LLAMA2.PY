import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_for_int8_training
from transformers import AutoModelForCausalLM , AutoTokenizer,TrainingArguments
from trl import SFTTrainer


def train():
    train_dataset = load_dataset("tastsu-lab/alpaca", split= "train")
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/xgen-7b-8k-base", trust_remote_code = True)
    model = AutoModelForCausalLM.from_pretrained(
        "Salesforce/xgen-7b-8k-base", load_in_4bit = True, torch_dtype = torch.float16, device_map ="auto"
    )
    model.resize_token_embedding(len(tokenizer))
    model = prepare_for_int8_training(model)
    peft_config = LoraConfig(r=16, lora_alpha = 0.05 , bias ="none", task_type = "CAUSAL_LM")
    model = get_peft_model(model, peft_config)
    
    training_args = TrainingArguments(
        output_dir="xgen-7b-tuned-alpaca",
        per_device_train_batch_size= 4,
        optim="adamw_torch",
        logging_steps=100,
        learning_rate=2e-4,
        fp16=True,
        warmup_ratio=0.1,
        lr_scheduler_type="linear",
        num_train_epochs=1,
        save_strategy="epoch",
        push_to_hub=True
    )
    trainer = SFTTrainer(
        model = model,
        train_dataset = train_dataset,
        dataset_text_field ="text",
        max_seq_len = 1024,
        tokenizer = tokenizer,
        args = training_args,
        packing=True,
        
    )
    trainer.train()
    trainer.push_to_hub()










