import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from Bio import SeqIO


def count_and_plot(seq: str, xlab="", ylab="count", title=""):
    """Counts the unique characters in a string and plots a bargraph"""
    count = dict(Counter(seq))

    df = pd.DataFrame.from_dict(count, orient="index").reset_index()
    df.columns = [xlab, ylab]

    sns.set_style("whitegrid")
    sns.barplot(data=count, palette="viridis")
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()


# ? fetch the record / sequence
uniprot_id = "P69905"
url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
response = requests.get(url)
response.raise_for_status()
print(response.text)


# ? Accesing the saved data locally
# * saved it to this location for local access
path = "sequences/hemoglobin-alpha-subunit.fasta"

# * reading the fasta to get the seq
record = SeqIO.read(path, "fasta")
seq = record.seq

# * length of sequence
print(len(seq))

# * amino acid composotion
count_and_plot(seq, "amino acid", "count", "amino acid count")

# ? secondary structure was predicted using PSIPRED
# * open the file and read the data
with open("resources/secondry_structure.horiz") as file:
    align = file.read().split("\n")

aa = ""
pred = ""
for line in align[1:]:
    if "Pred:" in line:
        formated_line = line.split("Pred: ")[1]
        pred += formated_line
    elif "AA:" in line:
        formated_line = line.split("AA: ")[1]
        aa += formated_line

# * count the perdictions
count_and_plot(pred, xlab="Structure", ylab="count", title="Structure Count")

# ? aligning protein and prediction


def print_alignment():
    for n in range(0, len(pred), 50):
        print(f" AA    {n + 1}  {aa[n:n+50]} {n + len(aa[n:n+50])}")
        print(f" Pred  {n + 1}  {pred[n:n+50]} {n + len(pred[n:n+50])}\n")


print_alignment()


# ? "What domains or motifs does this protein contain, and what do they tell me about its structure and function?"
# * extracting the InterProScan data
df = pd.read_csv("resources/Domain Prediction.tsv", sep="\t", header=None,
                 names=[
                     "protein_id", "md5", "length",
                     "analysis", "signature_acc", "signature_desc",
                     "start", "end", "score",
                     "status", "date",
                     "interpro_id", "interpro_desc",
                     "GO", "pathways"
                 ])

# * data cleaning and reordering
df = df.sort_values("score")
df = df.drop_duplicates(subset="interpro_id", keep="first")

# * extracting only meaningful rows and columns
new_df = df[["interpro_id", "interpro_desc", "analysis", "start",
             "end", ]].reset_index(drop=True)
new_df = new_df.loc[[0, 5, 6]].reset_index(drop=True)

# * adding biological interpretation
new_df["significance"] = ["hamoglobin complex, oxygen transporter",
                          "heme binding",
                          "Iron ion biniding"]

print(new_df)

new_df.to_csv("Analysis/result.csv")
# ? which amino acid is most common in the iron ion binding motif i.e. IPR002339
count_and_plot(
    seq[5:31], title="Amino Acid count in the iron ion binding motif")
