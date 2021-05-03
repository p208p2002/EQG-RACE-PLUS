import os
from pathlib import Path
import json
import re

_base_path = str(Path(__file__).absolute())
_base_path = re.sub(re.escape(__file__)+"$","",_base_path)
_split_set_path = {
    'train/high': os.path.join(_base_path,'datasets/EQG-RACE-PLUS/train/high.jsonl'),
    'train/middle': os.path.join(_base_path,'datasets/EQG-RACE-PLUS/train/middle.jsonl'),
    'dev/high': os.path.join(_base_path,'datasets/EQG-RACE-PLUS/dev/high.jsonl'),
    'dev/middle': os.path.join(_base_path,'datasets/EQG-RACE-PLUS/dev/middle.jsonl'),
    'test/high': os.path.join(_base_path,'datasets/EQG-RACE-PLUS/test/high.jsonl'),
    'test/middle': os.path.join(_base_path,'datasets/EQG-RACE-PLUS/test/middle.jsonl')
}

class EqgRacePlusDataset():
    def __init__(self,split_set_and_level):
        self.data = open(_split_set_path[split_set_and_level],'r',encoding='utf-8').readlines()
        
    def __getitem__(self,index):
        return json.loads(self.data[index])
            
    def __len__(self):
        return len(self.data)

# dataset = EqgRacePlusDataset('train/high')
# print(dataset[0])
