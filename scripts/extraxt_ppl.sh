#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

logs=$base/logs
extracted=$base/extracted_perplexities/from_logs

mkdir -p "$extracted"

# Find all directories in the logs directory
for dir in "$logs"/*; do
    if [ -d "$dir" ]; then  # Check if it is a directory
        err_file="$dir/err"
        if [ -f "$err_file" ]; then  # Check if the "err" file exists
            echo "Extracting preplexity scores from $err_file"

            # Extract file basename to use as the output file name
            folder_name=$(basename "$dir")

            grep -Po 'loss:\s*\d+\.\d+,\s*ppl:\s*\d+\.\d+,\s*acc:\s*\d+\.\d+' "$err_file" > "$extracted/${folder_name}_ppl.txt"
        else
            echo "No err file in $dir"
        fi
    fi
done
