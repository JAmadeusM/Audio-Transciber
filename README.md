# Simple Audio-Transcriber
 A simple implementation of the Whisper-AI from OpenAI

## Check for Cuda and PyTorch 
Simple run the file "test_for_cuda.py", if you want to check if PyTorch is setup correct.


## Install Cuda and PyTorch witch Cuda-Support:
1. Check what version of Cuda you need. For that look at and follow the accepted Answer in the [Stackoverflow-Thread](https://stackoverflow.com/questions/60987997/why-torch-cuda-is-available-returns-false-even-after-installing-pytorch-with)
2. After that, download the appropriate Cuda-Version from their [Archive](https://developer.nvidia.com/cuda-toolkit-archive)
3. Install PyTorch with Cuda-Support. You can generate an Installation-command via the official [PyTorch-Site](https://pytorch.org/get-started/locally/)  
Copy and run the command as it is. You shouldn't have to the the Cuda-Version in the command itself.
4. Run "test_for_cuda.py" to see if installation was successful.

## Transcribing X files
To transcribe an x amount of files simply insert them into the Input-folder and run "transcribe_cuda_multiple_files.py". After it ran through you can find the corresponding txt-files in the Output-Folder.
