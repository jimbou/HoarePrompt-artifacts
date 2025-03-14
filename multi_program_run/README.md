
<table>
  <tr>
    <td style="width: 20%; text-align: center;">
      <img src="../assets/HoarePrompt_logo.png" alt="HoarePrompt Logo" width="100"/>
    </td>
    <td style="width: 80%; text-align: left;">
      <h1>HoarePrompt-expirement: Experiments guide for the HoarePrompt tool</h1>
    </td>
  </tr>
</table>

## Introduction

The **HoarePrompt-experiment** aims to determine whether large language models (LLMs) can accurately judge if a program correctly implements specifications without executing the tests. The experiment relies solely on natural language reasoning to make these determinations. This project assists users to run multiple experiments on larger datasets of programs using the HoarePrompt tool, the repository of which can be found [here](https://github.com/msv-lab/HoarePrompt).


## Preparation

Before running the project, make sure to set the necessary environment variables such as `GROQ_API_KEY` and `OPENAI_API_KEY`. These keys are essential for accessing the respective APIs, which power the LLM services used in this experiment.

### 1. Set up a Virtual Environment

It is recommended to create a virtual environment to ensure proper dependency isolation and avoid conflicts with other projects. Follow these steps to create and activate the virtual environment:

```bash
# Create a virtual environment
python3 -m venv hoareprompt-env

# Activate the virtual environment
source hoareprompt-env/bin/activate
```

### 2. Install Dependencies

Once your virtual environment is activated, install the necessary dependencies for the project:

```bash
pip install -r requirements.txt
```

Additionally, install the `hoareprompt` package locally using an editable install:

```bash
pip install -e /path/to/hoareprompt
```

> Replace `/path/to/hoareprompt` with the actual path to the `hoareprompt` directory from the git  [repo](https://github.com/msv-lab/HoarePrompt).
  
> The `-e` flag stands for **editable** mode, meaning that any changes you make to the `hoareprompt` package will immediately be reflected without needing to reinstall it.

### 3. Set API Keys

Depending on the LLM service you intend to use, set the appropriate environment variables for your API keys:

For **OpenAI** models:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

For **Groq** models:
```bash
export GROQ_API_KEY="your-groq-api-key"
```

You can add these `export` commands to your `.bashrc` or `.zshrc` files to avoid having to set them every time you start a new terminal session.

## Running the Project

This is used to run many problems in jsopn format together.
The configuartion options are the same and you can see them on the Readme on the main dir :../README.md, 
Execute the following command, specifying the data, log, and configuration file paths:
The data must be a json path with the following options per test case: "description", "correct", "unique_id", "task_id" ,"generated_code"
You can use our dataset in ../Results/Dataset

```bash
python3 -m src.main_verify --data /path/to/data/file --log /path/to/log/dir --config /path/to/config/file
```

- `--data` : Path to the data file.
- `--log` : Directory where logs will be stored.
- `--config` : Path to the configuration file.

Example:
```bash
python3 -m src.main_verify --data data/input.json --log logs/experiment1 --config configs/custom_config.json
```

If you do not provide the `--config` argument, the default configuration file (`default_config.json`) will be used.

The main_verify should be used if you want to test Hoareprompt or hoareprompt no unroll(depending on your config) for all available classifiers other than tester

If you want to use tester use the tester config and the main_tester script:



python3 -m src.main_tester --data /path/to/data/file --log /path/to/log/dir --config /path/to/config/file

