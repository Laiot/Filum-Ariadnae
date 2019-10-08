from Randomness.MarkovChain import MarkovChain
import os
from pathlib import Path

path = Path(__file__)
dirname = path.parent.parent
print(dirname)
config = open(os.path.join(dirname, 'Configuration_Files/config.txt'), "r")
probs_file_path = config.readline().split()[1]
probs_file_path = os.path.join(dirname, probs_file_path)
print(probs_file_path)
first_page = config.readline().split()[1]
final_pages = [page for page in config.readline().split()[1:]]
ex = MarkovChain(probs_file_path, first_page, final_pages)
print(ex.next())
