# Pre-Download requirements: Python + Git + CUDA installed + Ollama

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install datasets evaluate accelerate transformers
pip install llama-index-core llama-index-embeddings-huggingface

# Getting your API Key for LLamaParse
https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/

# Steps to run:
Add your own data to solar_data folder
ollama run llama3.1
python .\Llama_Model.py

# Future Project Goals
https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/
https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/
