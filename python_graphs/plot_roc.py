#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

def load_results(fname):
    fpr_list = [0.0]  # La curva ROC parte da (0,0)
    tpr_list = [0.0]
    
    with open(fname, 'r') as fh:
        for line in fh:
            if not line.strip():
                continue
            parts = line.split()
            
            try:
                # Il codice cerca la posizione di 'TP:', 'TN:', ecc. e prende il numero subito dopo
                tp = int(parts[parts.index('TP:') + 1])
                tn = int(parts[parts.index('TN:') + 1])
                fp = int(parts[parts.index('FP:') + 1])
                fn = int(parts[parts.index('FN:') + 1])
                
                # Formule matematiche di base per le coordinate del grafico
                tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                fpr = fp / (tn + fp) if (tn + fp) > 0 else 0.0
                
                tpr_list.append(tpr)
                fpr_list.append(fpr)
            except (ValueError, IndexError):
                # Se una riga è vuota o scritta male, la salta senza bloccarsi
                continue
                
    fpr_list.append(1.0)  # La curva ROC finisce a (1,1)
    tpr_list.append(1.0)
    
    # Ordina i punti in modo che il grafico venga disegnato da sinistra a destra
    points = sorted(zip(fpr_list, tpr_list))
    fpr_list, tpr_list = zip(*points)
    
    return fpr_list, tpr_list

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso nel terminale: python3 plot_roc.py <file_risultati.results>")
        sys.exit(1)
        
    results_file = sys.argv[1]
    fpr, tpr = load_results(results_file)
    
    # Setup del grafico grafico (dimensioni e stile simili a quello dell'MCC)
    plt.figure(figsize=(7, 5.5))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='HMM Kunitz Profile')
    plt.plot([0, 1], [0, 1], color='navy', lw=1.5, linestyle='--', label='Random Classifier')
    
    plt.xlim([-0.02, 1.02])
    plt.ylim([-0.02, 1.02])
    plt.xlabel('False Positive Rate (1 - Specificity)')
    plt.ylabel('True Positive Rate (Sensitivity)')
    plt.title(f'ROC Curve Analysis - {results_file}')
    plt.legend(loc="lower right")
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Salva il grafico direttamente come immagine PNG nella tua cartella
    output_image = results_file.replace('.results', '_roc.png')
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    print(f"Fatto! Grafico ROC salvato come: {output_image}")
