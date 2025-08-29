# CenterEmbedding

## Paper

Hardt, D., (2025) “Sparks of Pure Competence in LLMs: the Case of Syntactic Center Embedding in English”, Society for Computation in Linguistics 8(1): 13. doi: https://doi.org/10.7275/scil.3149


## Data

The synthetic data can be found in data/center_embed

ce1.json is level 1 question 0 (as described in the paper)


ce[1-4].json designates a level 1-4, for question 0

ce22.json is level 2 question 1

ce[2-4]2.json is level 2-4, question 1

## Results

Results of each run are stored in results

Folder names specify [model] [data] [number examples] [runtime].

For example

llama3-70b_ce-q0-l1-4_N200_Tn0_15-12-24-14-25

model: llama3-70b

data: ce-q0-l1-4

number examples: 200

run time: dec 12 2024, 14:25

## Get started
1. Create a conda env from the environment.yml file, and activate it

```bash
conda env create -f environment.yml
conda activate ./centerembed
```

2. Run `python eli/center_embed.py --help` to see the available options. Should show the following:

Sample Run

python eli/center_embed.py --file_list data/lists/ce-q0-l1-4 --model gpt-4 --sample_n 200 --tuning_n 0 --seed 42



## Adding models
Copy a model (e.g., from eli/models/llama/__init__.py) and paste it in a new file in the relevant folder under `eli/models/`. Make sure to keep the same model structure but update the model name, the API endpoint, and the prompt.

Make sure to add this model to the model registry in `eli/models/__init__.py`.

