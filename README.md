# Pre-Download requirements: Python + Git + CUDA installed + Ollama

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 <br />
pip install datasets evaluate accelerate transformers <br />
pip install llama-index-core llama-index-embeddings-huggingface <br />

# Getting your API Key for LLamaParse
https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/

# Steps to run:
Add your own data to solar_data folder <br />
ollama run llama3.1 <br />
python .\Llama_Model.py <br />

# Future Project Goals
https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/ <br />
https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/
