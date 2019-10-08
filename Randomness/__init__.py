from Randomness.MarkovChain import MarkovChain
import os

dirname = os.path.dirname(__file__)
config = open(os.path.join(dirname, 'Configuration Files/config.txt'), "r")
probs_file_path = config.readline().split()[1]
first_page = config.readline().split()[1]
final_pages = [page for page in config.readline().split()[1:]]
ex = MarkovChain(probs_file_path, first_page, final_pages)
print(ex.next())
