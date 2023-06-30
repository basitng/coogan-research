FINE TUNE ID: ft-0ZOVrDQ2JL3mmcDQ587Lzpnu

### CLI data preparation tool

openai tools fine_tunes.prepare_data -f data.jsonl

### Create a fine-tuned model

openai api fine_tunes.create -t data_prepared.jsonl

### Resume training when failed

openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>

# List all created fine-tunes

openai api fine_tunes.list

# Retrieve the state of a fine-tune. The resulting object includes

# job status (which can be one of pending, running, succeeded, or failed)

# and other information

openai api fine_tunes.get -i <YOUR_FINE_TUNE_JOB_ID>

# Cancel a job

openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>
