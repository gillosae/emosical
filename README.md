# Emosical: An Emotion-Annotated Musical Theatre Dataset
Accepted to EMNLP Findings, 2024



### Info
This repository contains files and automatic scripts to produce the Emosical dataset.

Supported movies in current version (download links) : Aladdin (1992), Aladdin (2019), Beauty and the Beast (2017), Cats (1998), Chicago (2002), Frozen (2014), Frozen2 (2019), Frozen Fever (2015), JesusChristSuperstar (2012), Kinky Boots (2019), La la Land (2016), Moana (2016), Mulan (1998), Peter Pan (1953), Tangled (2011), Tick Tick Boom (2021), The Little Mermaid (1989), The Nightmare Before Christmas (1993), The Phantom of the Opera (2011), Trevor (2021)


### How to 
1. Download movie files from provided link above.
2. Place your movie file under ```data/raw/theatre/```.
The name of placed movie files should match the name of srt files in ```data/raw/srt/```.
3. Then run the following code to produce data automatically.
    
        ./run.sh




### Dataset Structure
Before:

    ├── data/
    │   └── raw/
    │       ├── theatre/
    │       │   ├── frozen.mov
    │       │   └── ...
    │       └── srt/
    │           ├── frozen.srt
    │           └── ...
    └── metadata/
        ├── number_info.csv
        └── global_persona/
        │       ├── frozen.yaml   
        │       └── ...
        └── scene_summarization/
                ├── frozen.yaml   
                └── ...

After:

    ├── data/
    │   ├── raw/
    │   │   ├── theatre/
    │   │   │   ├── frozen.mov
    │   │   │   └── ...
    │   │   └── srt/
    │   │       ├── frozen.srt
    │   │       └── ...
    │   ├── audio/ 
    │   │   ├── frozen/
    │   │   │   ├── 1.wav
    │   │   │   └── ...
    │   │   └── ...
    │   ├── video/
    │   └── text/
    └── metadata/
        ├── number_info.csv
        └── global_persona/
        │       ├── frozen.yaml   
        │       └── ...
        └── scene_summarization/
                ├── frozen.yaml   
                └── ...


### Dataset Split
