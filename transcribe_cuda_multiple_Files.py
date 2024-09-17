import whisper 

import torch
# Cuda allows for the GPU to be used which is more optimized than the cpu
torch.cuda.init()



input = "./Input"

from os import listdir
from os.path import isfile, join
allfiles = [f for f in listdir(input) if isfile(join(input, f)) and not f.endswith(".gitkeep")]



#load whisper model
model_size = "base"                         #available options are: tiny, base, small, medium, large
model = whisper.load_model(model_size)
language = "en"

for input_file in allfiles:

    results = []

    # Transcribe audio
    result = model.transcribe("./Input/" + input_file, language=language, fp16=False, verbose=True)

    #save transcribed text to file
    f = open("./Output/" + input_file.replace("mp4","txt"), "w")
    f.write(result['text'])
    f.close()