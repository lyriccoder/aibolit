import pandas as pd
import os

current_location: str = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
target_folder = os.getenv('TARGET_FOLDER')
if target_folder:
    os.chdir(target_folder)

df_patterns = pd.read_csv('./target/04/04-find-patterns.csv', sep=';').set_index('filename')
df_patterns.to_csv('./target/dataset.csv')
