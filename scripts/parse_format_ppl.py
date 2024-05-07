import os
import re
import matplotlib.pyplot as plt


def extract(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    perplexity_scores = []
    for line in lines:
        if len(line) > 1:
            ppl = re.sub(
                r'ppl:\s+', '',
                re.search(r'ppl:\s+\d+\.\d+', line).group(0)
            )
            perplexity_scores.append(ppl)
    
    return perplexity_scores


def save_tsv(data: dict):
    header = 'validation ppl\t' + '\t'.join(data.keys()) + '\n'
    tsv_lines = [header]

    line_cnt = 0
    for i in range(len(data['baseline'])):
        line = f'{(i + 1) * 500}\t'
        line += f'{data["baseline"][i]}\t{data["post"][i]}\t{data["pre"][i]}'
        tsv_lines.append(line + '\n')
        line_cnt += 1
        
        # The last step (40600) does not generate a validation perplexity
    
    # Write to output tsv file
    with open('extracted_perplexities/ppl.tsv', 'w', encoding='utf-8') as output:
        for line in tsv_lines:
            output.write(line)


def plot_perplexities():
    with open('extracted_perplexities/ppl.tsv', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]  # Skip header
    
    validation_steps = []
    baseline_ppl = []
    post_ppl = []
    pre_ppl = []
    
    for line in lines:
        data = line.strip().split('\t')
        validation_steps.append(int(data[0]))
        baseline_ppl.append(float(data[1]))
        post_ppl.append(float(data[2]))
        pre_ppl.append(float(data[3]))
    
    plt.figure(figsize=(12, 8))
    plt.plot(validation_steps, baseline_ppl, label='Baseline', linewidth=2)
    plt.plot(validation_steps, post_ppl, label='Post-normalization', linewidth=2)
    plt.plot(validation_steps, pre_ppl, label='Pre-normalization', linewidth=2)
    plt.xlabel('Validation Step')
    plt.ylabel('Perplexity')
    plt.title('Perplexity Scores Over Validation Steps')
    plt.legend()
    plt.grid(True)
    plt.savefig('extracted_perplexities/perplexity_plot.png')  # Save the plot as a PNG file
    plt.close()  # Close the plot explicitly after saving


def main():
    raw_data_dir = 'extracted_perplexities/from_logs/'
    perplexities = {'baseline': 0, 'post': 0, 'pre': 0}

    for filename in os.listdir(raw_data_dir):
        if 'post' in filename:
            perplexities['post'] = extract(raw_data_dir+filename)
        elif 'pre' in filename:
            perplexities['pre'] = extract(raw_data_dir+filename)
        else:
            perplexities['baseline'] = extract(raw_data_dir+filename)
    
    save_tsv(perplexities)
    print("TSV created")
    plot_perplexities()
    print("Line plot created")
    


if __name__ == '__main__':
    main()