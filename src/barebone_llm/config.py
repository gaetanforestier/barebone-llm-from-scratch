
GPT_CONFIG_124M = {
    "vocab_size": 50257,   # Taille du vocabulaire BPE
    "context_length": 1024, # Longueur maximale de la séquence
    "emb_dim": 768,        # Dimension des embeddings
    "n_heads": 12,         # Nombre de têtes d'attention
    "n_layers": 12,        # Nombre de blocs transformer
    "drop_rate": 0.1,      # Dropout pour éviter l'overfitting
    "qkv_bias": False      # Biais dans les couches linéaires QKV
}