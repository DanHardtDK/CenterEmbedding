# CenterEmbedding


## Data

The synthetic data can be found in /data/center_embed
ce1.json is level 1 question 0
ce22.json is level 2 question 1

## Results

Results of each run are stored in ./results
Folder names specify [model] [data] [number examples] [runtime].
For example
llama3-70b_ce-q0-l1-4_N200_Tn0_15-12-24-14-25
model: llama3-70b
data: ce-q0-l1-4
number examples: 200
run time: dec 12 2024, 14:25


## Paper

Hardt, D., (2025) “Sparks of Pure Competence in LLMs: the Case of Syntactic Center Embedding in English”, Society for Computation in Linguistics 8(1): 13. doi: https://doi.org/10.7275/scil.3149


## Producing Results

(need: conda activate ellipses-gpt)

python eli/center_embed.py --file_list data/lists/ce-lvl1 --model llama-7b-chat --sample_n 5 --iterations 1 --tuning_n 0 --prompt_strategy center_embed_tn1 --seed 42


## Get started
1. Create a conda env from the environment.yml file, and activate it

```bash
conda env create -f environment.yml
conda activate ./centerembed
```

2. Run `python eli/center_embed.py --help` to see the available options. Should show the following:

```bash
CenterEmbedding git:(debugging) ✗ python eli/center_embed.py --help
usage: center_embed.py [-h] [--file_list FILE_LIST] [--model MODEL]
                       [--prompt_strategy {default,center_embed,center_embed_tn1,center_embed_tn2,supervised_cot,unsupervised_cot}]
                       [--sample_n SAMPLE_N] [--iterations {1,2,3,5,10,50}]
                       [--tuning_n {0,1,2,3,5,10,20}] [--seed SEED]

options:
  -h, --help            show this help message and exit
  --file_list FILE_LIST
                        Path for txt containing list of files to test against
  --model MODEL         LLM to test
  --prompt_strategy {default,center_embed,center_embed_tn1,center_embed_tn2}
                        strategy to use for tuning
			center_embed = P0
			center_embed_tn1 = P1 (prompt with single level 1 example, with Q0 question)
			center_embed_tn1 = P1 (prompt with two examples, a level 1 example and a level 2 example, both with Q0 questions)
  --sample_n SAMPLE_N   number of ellipses examples to test
  --iterations {1,2,3,5,10,50}
                        number of iterations to run
  --tuning_n {0,1,2,3,5,10,20}
                        Number of in-prompt n-shot examples to use for tuning
  --seed SEED           random seed for reproducibility
(/Users/nicolai/Desktop/cbs/research/CenterEmbedding/centerembed) ➜  CenterEmbedding git:(debugging) ✗
```

3. Run the script with the desired options. For example:

```bash
python eli/center_embed.py --file_list data/lists/ce-lvl1 --model llama-7b-chat --sample_n 5 --iterations 1 --tuning_n 0 --prompt_strategy center_embed_tn1 --seed 42
```

## Adding models
Copy a model (e.g., from eli/models/llama/__init__.py) and paste it in a new file in the relevant folder under `eli/models/`. Make sure to keep the same model structure but update the model name, the API endpoint, and the prompt.

Make sure to add this model to the model registry in `eli/models/__init__.py`.

