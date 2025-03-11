# Emosical: An Emotion-Annotated Musical Theatre Dataset

(Pending)

Accepted to EMNLP Findings, 2024


### Info
This repository contains files and automatic scripts to produce the Emosical dataset.

Supported movies in current version (download links) : 
<a href="https://www.microsoft.com/en-us/p/aladdin/8d6kgwxn05ql?activetab=pivot%3Aoverviewtab">Aladdin (1992)</a>, 
<a href="https://www.microsoft.com/en-us/p/aladdin-2019-bonus/8d6kgwxn02mz">Aladdin (2019)</a>, 
<a href="https://www.microsoft.com/en-us/p/beauty-and-the-beast-2017/8d6kgwx29kg4">Beauty and the Beast (2017)</a>, 
<a href="https://www.microsoft.com/en-us/p/cats-2019/8d6kgwxn0z1v">Cats (1998)</a>, 
<a href="https://www.microsoft.com/en-us/p/chicago/8d6kgwzl5htw?activetab=pivot%3Aoverviewtab">Chicago (2002)</a>, 
<a href="https://www.microsoft.com/en-au/p/frozen-2013/8d6kgwzkhjg9?activetab=pivot%3Aoverviewtab">Frozen (2014)</a>, 
<a href="https://www.microsoft.com/en-us/p/frozen-ii/8d6kgwxn0hk0">Frozen2 (2019)</a>, 
<a href="https://www.microsoft.com/en-us/p/frozen-fever/8d6kgx02bg5t?activetab=pivot%3Aoverviewtab">Frozen Fever (2015)</a>, 
<a href="https://www.microsoft.com/nl-nl/p/jesus-christ-superstar/8d6kgwzl60ks">Jesus Christ Superstar (2012)</a>, 
<a href="https://www.microsoft.com/en-us/p/kinky-boots-the-musical/8d6kgwxn6zn4?activetab=pivot%3Aoverviewtab">Kinky Boots (2019)</a>, 
<a href="https://www.microsoft.com/en-us/p/la-la-land/8d6kgwx614c0?activetab=pivot%3Aoverviewtab">La la Land (2016)</a>, 
<a href="https://www.microsoft.com/en-us/p/moana/8d6kgx0m8tzw?activetab=pivot%3Aoverviewtab">Moana (2016)</a>, 
<a href="https://www.microsoft.com/en-us/p/mulan/8d6kgwzl4z7t?activetab=pivot%3Aoverviewtab">Mulan (1998)</a>, 
<a href="https://www.microsoft.com/en-us/p/peter-pan/8d6kgwxn1x51">Peter Pan (1953)</a>, 
<a href="https://www.microsoft.com/en-us/p/tangled/8d6kgwzl596v?activetab=pivot%3Aoverviewtab">Tangled (2011)</a>, 
<a href="https://www.microsoft.com/en-us/p/the-little-mermaid/8d6kgwxn3q1k">The Little Mermaid (1989)</a>, 
<a href="https://www.microsoft.com/en-us/p/nightmare-before-christmas-bonus/8d6kgwxn2q0x?activetab=pivot%3Aoverviewtab">The Nightmare Before Christmas (1993)</a>, 
<a href="https://www.microsoft.com/en-gb/p/phantom-of-the-opera-at-the-royal-albert-hall-25th-anniversary-celebration/8d6kgwzl5fz5?activetab=pivot%3Aoverviewtab">The Phantom of the Opera (2011)</a>, 
<a href="https://www.ebay.com/itm/335457354216?mkcid=16&mkevt=1&mkrid=711-127632-2357-0&ssspo=n41xXGNFTO2&sssrc=2047675&ssuid=&widget_ver=artemis&media=COPY">Tick Tick Boom (2021)</a>, 
<a href="">Trevor (2021)</a>


### How to 
1. Clone our repository recursively for <a href="https://github.com/facebookresearch/demucs">Demucs</a> and <a href="https://github.com/sp-uhh/sgmse">SGMSE</a> audio processing.

        git clone --recursive https://github.com/gillosae/emosical.git

2. Download movie files from provided link above.
3. Place your movie file under ```data/raw/theatre/```.
The name of placed movie files should match the name of srt files in ```data/raw/srt/```.
4. Then run the following code to produce data automatically.
    
        python run.py




### Dataset Structure
Before:

    ├── data/
    │   └── raw/
    │       ├── theatre/
    │       │   ├── aladdin.mov
    │       │   └── ...
    │       └── srt/
    │           ├── aladdin.srt
    │           └── ...
    └── metadata/
        ├── number_info.csv
        └── global_persona/
        │       ├── aladdin.yaml
        │       └── ...
        └── scene_summarization/
                ├── aladdin.yaml
                └── ...

After:

    ├── data/
    │   ├── raw/
    │   │   ├── theatre/
    │   │   │   ├── aladdin.mov
    │   │   │   └── ...
    │   │   └── srt/
    │   │       ├── aladdin.srt
    │   │       └── ...
    │   ├── audio/ 
    │   │   ├── aladdin/
    │   │   │   ├── 1.wav
    │   │   │   └── ...
    │   │   └── ...
    │   ├── video/
    │   └── text/
    └── metadata/
        ├── number_info.csv
        └── global_persona/
        │       ├── aladdin.yaml   
        │       └── ...
        └── scene_summarization/
                ├── aladdin.yaml   
                └── ...
