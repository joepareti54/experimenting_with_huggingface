from transformers import pipeline
#
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")
#
text = "my favorite signature is: only the paranoid survive"
tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
#https://kandi.openweaver.com/python/Helsinki-NLP/Opus-MT#Community-Discussions
# The model requires pytorch tensors and not a python list. Simply add return_tensors='pt' to prepare_seq2seq
#
translation = model.generate(**tokenized_text)
translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
# Print translated text
print(translated_text)
