from filesplit.split import Split
split = Split(inputfile="nutritionapp/static/models/dalai/alpaca/models/7B/ggml-model-q4_0.bin", outputdir="nutritionapp/static/models/dalai/alpaca/models/7B")
split.bysize(10_000_000)

# from filesplit.merge import Merge
# merge = Merge(inputdir=, outputdir: str, outputfilename: str)