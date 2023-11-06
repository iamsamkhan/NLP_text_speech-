# NLP_text_speech-


![High Level Overview](documentation/images/ds-toolkit-banner.png)

# Speech-to-Text Transcription and Classification Solution Accelerator
This repository contains the base repository for developing an end-to-end speech transcription and message classification solution for any type of business problem requiring an advanced method for classifying audio messages into actionable meaning. The types of business problem benefitting from this solution include:
- General audio message classification within a noisy environment 
- Monitoring communications for safety and regulatory purposes, eg: Mining industry - positive communications
- Complex audio message and communication classification scenarios, eg: Message understanding   

Note that to illustrate the specific use case of positive communication in mining industry, some customized samples files [sample_files_mining](./sample_files_mining) are aslo provided in this repo. This use case will be elabrated in [An example use case in Mining Industry](#an-example-use-case-in-mining-industry).

## Prerequisites

The diagram below presents the main data flow overview:

![High Level Overview](documentation/images/solution-overview.png)

# Main features

Provided audio files and their supporting attributes, this repository include three main features: 
- `Audio Signal Processing`
- `Speech to text transcription Machine Learning Modelling` 
- `Natural Language Processing (NLP) Machine Learning Modelling` 
- `Advanced sequential and classification modelling`
- `Speech to text transcription performance claculation methodology`

These features enable you to have extract major insights.

## Audio Signal Processing 
The audio signal processing and filtering techniques is developed to maximise the signal-to-noise ratio (SNR) of the audio signals for optimised speech-to-text processing. The key steps in the audio signal processing includes:
1. Audio data processing and mono channel averaging
2. Frequency domain and spectral analysis
3. Signal (S) and noise (N) power analysis
4. SNR optimisation
5. Fast-Fourier-Transform (FFT) and Butterworth filter application


![High Level Overview](documentation/images/audio-signal-processing-overview.png)

The digarm below shows a sample audio signal processing using the above mensioned key stapes, where the raw audio file (left) and optmised and filtered to produce the filtered (maximised SNR) audio file (right).

![High Level Overview](documentation/images/sample-audio-filtering.png)


## Speech to text transcription Machine Learning Modelling
The first stage of the solution is to apply a combination of Azure Cognitive services for Speech and customised scripts to convert the array of the audio files into lexical text




## Natural Language Processing (NLP) Machine Learning Modelling
The next stage uses NLP and related algorithms is the tokenisation of the lexical text and extraction of the key phrases. 
The output format for the NLP JSON (saved as **NLP_dict.json**) is presented below.
(NB: Major attributes in 

## Speech to text transcription performance claculation methodology
The transcripted voide data into text will be evlauted against the actual text using industry standard [Word Error Rate](https://en.wikipedia.org/wiki/Word_error_rate). For reporting we will use the accuarcy rate as shown below

<font size=5> $WER(transcript_{n}) = \frac{I + D + S}{N}$ * 100%

$WA_{cc}(transcript_{n}) = 1 - WER(transcript_{n})$

</font>

*where*
* `Insertion (*I*)`: Transcribed Words that are incorrectly added in the hypothesis transcript
* `Deletion (*D*)`: Transcribed Words that are undetected in the hypothesis transcript
* `Substitution (*S*)`: Trabscribed Words that were substituted between reference and hypothesis


# Getting Started

## Contents of Notebooks

We have two notebooks([00. provisioning](./src/engine/00.%20provisioning.ipynb), [10. training](.//src/engine/10.%20training.ipynb)) to understand the entire features.

- Provisioning
    - We set up Azure resouces and environment variables with the Notebook.
- Training
    - After completing provisioning, we find the following features:
        - Extract text from provided audio files with speech-to-text features
        - Extract some features from NLP techniques.
        - With extracted features, you can generate advanced Machine Learning classifier.

## Provisioning

At first, set up your Azure resource with [the instruction](./src/engine/00.%20provisioning.ipynb), which contains Azure resouce generation, setting python environment, and configuration some datastore to be used in experiencing training notebook.

## Preparing some constants and files

In order to analyze audio files, you need to prepare the following files:

- Audio files with `.wav` format
    - Prepare audio files, which you want to analyze. Then, please upload all of them into `recordings` directory in  `raw` container. This container should be already generated in [here](./src/engine/00.%20provisioning.ipynb).

- Transcription for each audio file
    - It defines true transcription for audio file, which will be used in measuring the accuracy of Speech-to-Text 

- Ground truth for each audio file, which will be used in Machine Learning classifier:

- Aggregated csv file `transcription-truth.csv`, which include the following columns:
    - `audio file name`: Names of sample audio files
        - This repository was verified with some `.wav` files.
    - `true transcription`: True transcription for each audio file
    - `Labels for each sample audio file`: Ground-truth of the classifier
        - Set your labels in `MESSAGE_CLASSIFICATION_GROUP` in `./src/common/constants.py`.
            - Ex.) If you define labels with `UPPER`, `LOWER` and `OTHERS`, please indicate them as "list" object in python like `MESSAGE_CLASSIFICATION_GROUP = ['OTHERS', 'UPPER', 'LOWER']` as well.

        ![Image](./documentation/images/transcripts-truth.png)

    NB: You don't need to add column names in header of csv file, and just put actual values there

- Vocabulary definition files
    - `general-ontology.json`
        - It defines the frequently used vocabularies in a particular use case, which are used to boost the performance of speech to text transcribing.

    - `homophone-list.txt`
        - It defines pairs of homophone vocabularies, which are used to correct the results of the original transcriptions in general to be more frequent vocabularies in the specific use case.  

    - `key-phrases-to-search.json`
        - It defines the key phrases in a specific use case, which will be used for NLP text mining. 

Once you prepare those files, please follow the instruction in `0.6 Upload those files` in [here](./src/engine/00.%20provisioning.ipynb)

## Training

Now, we're ready to enjoy the experiments

- [Training Notebook](./src/engine/10.%20training.ipynb): Demonstrate a series of processes like loading audio files, extract texts with speech-to-text technology, extract insights with NLP-techniques, generate classifier given ground-truth labels.

# An example use case in Mining Industry

This part will elaborate the specific use case of positive communication in mining industry. 

## Positive communication

In mining industry, there are a variety of vehicles involved in the normal operations a mining site, ranging from light vehicles to various type of heavy mobile platforms like dump trucks, excavators and loaders. The complicated interactions between the diverse types of vehiles in the complicated mining scenario are potential risk for the safe operation of a mining site. As such, multiple control measures are demanded to mitigate such risk.

One of these measures is called positive communications, which means clear and proactive communication with repeated confirmation. The radio communications between vehicle drivers are required to following this positive communication protocol. 

For example, a 50m safety distance around a heavy vehicle is assumed to ensure safety. When another vehicle approaches the 50m safety distance of the heavy vehicle, it needs to initiate a positive communication such as "40 loader, this is 539 dump truck. Permission to pass your left." and wait for the response for the heavy vehicle. After receiving the request, the heavy vehicle is expected to reply in a clear and repeated way such as "539 dump truck. You are clear to pass 40 loader on the left."    

![Positive communication illustration](./documentation/images/positive_communication.PNG)

## Automated transcribing and compliance classification

The mining companies have the demands to ensure the compliance of the radio communication to this positive communication protocol. Traditionally, there is a human supervisor responsible for monitoring the radio communication and evaluate the trend of compliance manually, which is inefficient and subjective.

As such, automated monitoring the radio communication and classifying if they are compliant to positive communication or not is highly demanded. 

## Sample files for mining use case

some customized samples files [sample_files_mining](./sample_files_mining) are provided to illustrate the use case of the accelerator. The sample files in it are explained as follows.

### Audio files with `.wav` format
- Prepared audio files, which you want to analyze. Then, please upload all of them into `recordings` directory in  `raw` container. This container should be already generated in [here](./src/engine/00.%20provisioning.ipynb). In this sample, the audio files are just an illustration of positive communication in mining which is not real recording from radio communication in production mining scenario. 

### Aggregated csv file `transcription-truth.csv`
    It includes the following columns:

- `audio file name`: Names of sample audio files. In this example, the audio file is named by the following format: <No. of conversation>-<start_date: YYMMDD>-<start_time: HHMMSS>-<end_date: YYMMDD>-<end_time: HHMMSS>. 
- `true transcription`: True transcription for each audio file, which will be used in measuring the accuracy of Speech-to-Text.
- `Labels for each sample audio file`: Ground-truth of the classifier
    - Y: It is a positive communication and it IS compliant.
    - N: If is a positive communication but it is NOT compliant. 
    - X: OTHERS, which is not a positive communication.
    Note that you don't need to add column names in header of csv file, and just put actual values there

### Vocabulary definition files
- `general-ontology.json`
    - It defines the frequently used vocabularies in a particular use case, which are used to boost the performance of speech to text transcribing. This file should be organized as following JSON format.
    
    Some words with frequently occurences in positive communications of mining can be selected to use as the general_ontology.


    The vocabularies are uttered and transcribed but should be replaced with other words in positive communication use case. These vocabulary pairs should be listed here. This file should be organized as the following format.

- `key-phrases-to-search.json`
   
    The keywords which are beneficial for classifying whether is a positive communication and/or compliant should be provided here for the NLP feature extraction. 

If you would like to try this use case, please follow the instruction in `0.6 Upload those files` in [here](./src/engine/00.%20provisioning.ipynb) to put the sample files in the right locations.

# Project Folder Structure

    ├── Speech2Text_NLP             # The main package, including the experiemntation and Azure ML pipelines
    │   ├── documentation           # Additional documentation descrining the system and any images used
    |   |── sample_files_mining     # Sample files for mining use case
    |   |      |── Audio_files      # The common folder containing any constants decleration
    |   |      |── ontoloy_files    # The main training and inference scripts
    |   |      |── transcripts-truth# The data ingestion, orchestration and Azure ML training & inference pipelines      
    │   |── src                     # Main scripts to perform the experimentation and the required inferences
    |   |      |── common           # The common folder containing any constants decleration
    |   |      |── engine           # The main training and inference scripts
    |   |      |── pipeline         # The data ingestion, orchestration and Azure ML training & inference pipelines
    │   |── CODE_OF_CONDUCT.md
    │   |── CONTRIBUTING.md  
    │   |── LICENSE
    │   |── README.md
    │   |── SECURITY.md
    │   |── SUPPORT.md    

# Contact

For more details or help deploying, contact the following:



# Acknowledgements

This repository is build in part using the following frameworks:



# Backlogs

- Add more detailed NLP techniques in [Training notebook](./src/engine/10.%20training.ipynb).
- Inferencing notebook.
- CI/CD pipeline with training/inferencing.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.



## Trademarks

This project may contain trademarks or logos for projects, products, or services.
