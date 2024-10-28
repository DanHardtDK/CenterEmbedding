# CenterEmbedding

## Sample Cmd:

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
                       [--prompt_strategy {center_embed,center_embed_tn1,center_embed_tn2}]
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
			center_embed_tn2 = P2 (prompt with two examples, a level 1 example and a level 2 example, both with Q0 questions)
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

## Using Weave
Weave is on Weights & Biases new service for LLMs. We have a W&B organization named `cbs-nlp`. To use Weave, you need to have a W&B account and be added to the `cbs-nlp` organization. Check you email :)

Whenever you run the script, you will see something like this

```bash
(centerembed) ➜  CenterEmbedding git:(debugging) ✗ python eli/center_embed.py --file_list data/lists/ce-lvl1 --model llama-7b-chat --sample_n 5 --iterations 1 --tuning_n 0 --prompt_strategy center_embed_tn1 --seed 42

Logged in as Weights & Biases user: nthomsen.
View Weave data at https://wandb.ai/cbs-nlp/llama-7b-chat_center_embed_tn1_ce-lvl1_N5_Tn0_I1/weave
```
You can click on this link to see the Weave dashboard for this run.
