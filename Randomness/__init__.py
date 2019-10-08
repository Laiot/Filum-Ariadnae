from Randomness.MarkovChain import MarkovChain

config = open("config.txt", "r")
probs_file_path = config.readline().split()[1]
first_page = config.readline().split()[1]
final_pages = [page for page in config.readline().split()[1:]]
ex = MarkovChain(probs_file_path, first_page, final_pages)
print(ex.next())
