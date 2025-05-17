
from kaggle.api.kaggle_api_extended import KaggleApi  # Luego el import

# Autenticación y descarga del dataset
api = KaggleApi()
api.authenticate()

dataset = 'hubertsidorowicz/football-players-stats-2024-2025'
print(f"Descargando dataset: {dataset}")

api.dataset_download_files(
    dataset,
    path='data',
    unzip=True
)

print("✅ Dataset descargado y descomprimido correctamente.")

