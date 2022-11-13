## set up packages and working environment with `conda`

path to `conda` folder : ``` MYPATH="/goinfre/$USER/miniconda3" ```

## 1. Download & Install conda
``` bash
$> curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
$> sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH
```

## 2. Initial configuration of conda
``` bash
$> $MYPATH/bin/conda init bash
$> $MYPATH/bin/conda config --set auto_activate_base false
$> source ~/.bash_profile
```

## 3. Create an environment for 42AI !
``` bash
$> conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy
```

## 4. Check and Activate 42AI Python environment
``` bash
$> conda info --envs
$> conda activate 42AI-$USER
```

## Conda automated installation (run script.sh)
``` bash
    bash script.sh
```