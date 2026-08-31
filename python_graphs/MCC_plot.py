import matplotlib.pyplot as plt
import re

def parse_results_file(filepath):
    th_values = [] # th = treshold di e-value
    mcc_values = []

    with open(filepath, "r") as file:
        for line in file:
            match = re.search(r'TH:\s*([\d.e-]+)\s+.*MCC:\s*([\d.]+)', line)
            if match:
                th_val = float(match.group(1))
                mcc_val = float(match.group(2))
                th_values.append(th_val)
                mcc_values.append(mcc_val)

    return th_values, mcc_values

set1_file = "kunitz_set_1.results" 
set2_file = "kunitz_set_2.results" 

th_set1, mcc_set1 = parse_results_file(set1_file)
th_set2, mcc_set2 = parse_results_file(set2_file)

plt.figure(figsize=(8, 5))
plt.plot(th_set1, mcc_set1, label="Set 1", color="purple", linewidth=1.5)
plt.plot(th_set2, mcc_set2, label="Set 2", color="orange", linewidth=1.5)

plt.xscale('log')

plt.gca().invert_xaxis()

plt.title("MCC vs E-value Threshold")
plt.xlabel("E-value")
plt.ylabel("MCC")

plt.grid(True, which="both", linestyle="--", alpha=0.7)

plt.legend(loc="lower left")
plt.ylim(-0.05, 1.05)

plt.tight_layout()
plt.savefig("mcc_vs_evalue_PLOT.png", dpi=300)
plt.show()

