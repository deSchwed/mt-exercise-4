# MT Exercise 4: Layer Normalization for Transformer Models

## Changes made to the code
- Uncommented the code marked in the exercise sheet that caused issues when training with CPU.
- Changed `train.sh` to use a different model name and config file. Also adjusted CPU cores to 16.

## Added files
- In the `configs` folder, I added new config files for pre- and post-normalization. The config files are also set to use GPU for training.
- Added `scripts/parse_format_ppl.py` to get the perplexity from extracted values of the training logs. The script then formats the perplexity values into a tsv file and creates a line plot of the perplexity values.
- Added `scripts/extraxt_ppl.sh` to iterate over the training logs and extract loss, perplexity, and accuracy values. This script then calls `parse_format_ppl.py` to further process the extracted values as mentioned above.

## How to use
After running the setup explained in the exercise sheet and activating the virtual environment, you can run the training script. Make sure you choose the correct config file in the `train.sh` script.
Before extracting the perplexity values, make sure you have matplotlib installed. You can install it by running `pip install matplotlib`.
After training your model variations, you can run `extract_ppl.sh` to extract the perplexity values from the training logs and create a table and a line plot of the perplexity values.
