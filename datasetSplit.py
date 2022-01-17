from pathlib import Path
import splitfolders

print("Start datasetSplit")

inputPath = Path('../input/').absolute()
outputPath = Path('../output/').absolute()
splitfolders.ratio(inputPath, outputPath, seed=689, ratio=(.7, .2, .1))
