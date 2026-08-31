import json

json_file = open("rcsb_pdb_custom_report_20260423095304.json", "r")
json_file_list = json.load(json_file)
result_file = open("protein_file", "w")
count = 0

#qua spacchetto il file json per ottenre una sorta di formato fasta dove ho l'entry ID, la sequenza e la catena:
for protein in json_file_list:
    entry_ID = protein["identifier"]

    for entity in protein["data"]["polymer_entities"]:
        seq = entity["entity_poly"]["pdbx_seq_one_letter_code_can"]

        for instance in entity["polymer_entity_instances"]:
            chain = instance["rcsb_polymer_entity_instance_container_identifiers"]["auth_asym_id"]

            if entry_ID != "": #controllo se l'entry_ID è vuoto
                if 40 < len(seq) < 80: #controllo se la sequenza rispetta la lunghezza
                    result_file.write(f">{entry_ID}_{chain}_{seq}\n")
                    count += 1 


json_file.close()
result_file.close()

#per quando vuoi controllare il numero di proteine, la prima volta erano 134
print(f"saved proteins = {count}")
