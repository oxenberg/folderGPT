import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from folderGPT.utils import ProjectLogger


class LLModel:

    def __init__(self, model_name: str):
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = self.create_model()

    def create_model(self):
        model = AutoModelForCausalLM.from_pretrained(self.model_name)
        ProjectLogger().info("Created model, starting to generate text")
        # model = model.half().cuda()
        return model

    def generate(self, input_text: str, max_length: int = 256):
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=max_length,
                                     do_sample=True,
                                     early_stopping=True,
                                     eos_token_id=self.model.config.eos_token_id,
                                     num_return_sequences=1)
        # output = output.cpu()
        output_text = self.tokenizer.decode(output[0], skip_special_tokens=False)
        return output_text
