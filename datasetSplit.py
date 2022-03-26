from pathlib import Path
import splitfolders

print("Start datasetSplit")
# category_names_list = ['beer_bottle', 'beer_can', 'bowl', 'camera', 'chair', 'clock', 'club_chair', 'faucet', 'football_helmet', 'guitar', 'jug', 'lamp', 'piano', 'pistol', 'sofa', 'vase']
# category_names_list = ['piano', 'pistol', 'sofa', 'vase']
inputPath = Path('../input/').absolute()
outputPath = Path('../output/').absolute()
splitfolders.ratio(inputPath, outputPath, seed=689, ratio=(.7, .2, .1))
