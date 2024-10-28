import csv
import sys

def read_and_output_csv(input_csv):
    reader = csv.DictReader(input_csv, delimiter='|')

    output_csv = open('/tmp/output.csv', mode='w', newline='', encoding='utf-8')    
    writer = csv.writer(output_csv, delimiter='|')
    # Write the header
    writer.writerow(['target', 'output', 'correct'])

    negTot = posTot = negCorrect = posCorrect = 0
    # Write the selected columns
    for row in reader:
        writer.writerow([row['target'], row['correct']])
        writer.writerow([row['context']])
        if row['target'] == "No":
            negTot = negTot + 1
            if row['correct'] == "True":
                negCorrect = negCorrect + 1
        elif row['target'] == "Yes":
            posTot = posTot + 1
            if row['correct'] == "True":
                posCorrect = posCorrect + 1

    negScore = negCorrect / negTot
    posScore = posCorrect / posTot
    print(negScore, negCorrect, "out of ", negTot, "negative examples")

    posScore = posCorrect / posTot
    print(posScore, posCorrect, "out of ", posTot, "positive examples")

    return(negScore, posScore)

GPT4inpFiles = ['../results/gpt-4_center_embed_tn2_ce-q1-l2_N500_Tn0_I1_16-05-24-09-42/predictions.dat']

if __name__ == "__main__":
    negScore = posScore = n = 0

    for f in GPT4inpFiles:
        print(f)
        input_csv = open(f, mode='r', newline='', encoding='utf-8')    
        (neg, pos) = read_and_output_csv(input_csv)
        n = n + 1
        negScore += neg
        posScore += pos
    negAvg = negScore / n
    posAvg = posScore / n
    print("Averages:",negAvg, posAvg)
        
