# Imgs Concd Analyzer

The analyzing tool for imgs concordance rate

# Usage

## Clone the repository

```bash
git clone https://github.com/y-vectorfield/imgs_concd_analyzer.git
```

## Change directory

```bash
cd imgs_concd_analyzer
```

## Install requirements

```bash
pipenv sync
```

If you use this tool as developer, you should implement the following command.

```bash
pipenv sync --dev
```

## Implement the tool

```bash
mkdir data
```

Store the target images in the `data` directory and activate the venv.

```bash
pipenv shell
```

Implement the analyzing tool

```bash
python imgs_concd_analyzer.py --img1_path IMG1_PATH --img2_path IMG2_PATH
```
