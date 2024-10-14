# Pre-Download requirements: Python + Git + CUDA installed + Ollama

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 \n
pip install datasets evaluate accelerate transformers \n
pip install llama-index-core llama-index-embeddings-huggingface \n

# Getting your API Key for LLamaParse
https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/

# Steps to run:
Add your own data to solar_data folder \n
ollama run llama3.1 \n
python .\Llama_Model.py \n 

# Future Project Goals
https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/ \n
https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/
