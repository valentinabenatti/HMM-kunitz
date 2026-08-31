#!/usr/bin/env python
import sys
import numpy as np


def get_preds(fname):
    preds = []
    fh = open(fname)
    for line in fh:
        v = line.rstrip().split()
        #preds.append([v[0], float(v[2]), int(v[3])])
        preds.append([v[0], float(v[1]), int(v[2])])
    return preds
# Questa funzione estrae le informazioni dal prediction file, ovviamente bisogna aggiustarla in base al file che gli dai in input. in questo caso prende il file name e il treshold. 


def get_cm(preds, th=0.001):
    cm = np.zeros((2, 2))
    n = len(preds)
    for k in range(n):
        j = 0
        i = preds[k][2]
        if preds[k][1] <= th:
            j = 1
        cm[i, j] = cm[i, j] + 1
    return cm


def get_acc(cm):
    return (cm[0, 0] + cm[1, 1]) / np.sum(cm)


def get_mcc(cm):
    tp = cm[1, 1]
    tn = cm[0, 0]
    fn = cm[1, 0]
    fp = cm[0, 1]
    d = (tp + fp) * (tp + fn) * (tn + fn) * (tn + fp)
    if d == 0:  # Evita la divisione per zero
        return 0.0
    mcc = (tp * tn - fp * fn) / np.sqrt(d)
    return mcc


if __name__ == "__main__":
    fname = sys.argv[1]
    th = float(sys.argv[2])
    preds = get_preds(fname)
    cm = get_cm(preds, th)
    q2 = get_acc(cm)
    mcc = get_mcc(cm)

    # Estrazione dei valori dalla matrice di confusione per la stampa
    tp = int(cm[1, 1])
    tn = int(cm[0, 0])
    fn = int(cm[1, 0])
    fp = int(cm[0, 1])
    
    # Istruzioni di stampa modificate per includere la matrice di confusione
    print(f"TH: {th}\tQ2: {q2:.4f}\tMCC: {mcc:.4f}\tTP: {tp}\tTN: {tn}\tFP: {fp}\tFN: {fn}")
