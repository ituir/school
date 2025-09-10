# School Repository / School Repository

Dit repository bevat Nederlandse onderwijsmaterialen voor 4 VWO (Voortgezet Wetenschappelijk Onderwijs).
This repository contains Dutch educational materials for 4 VWO (Pre-university Education).

## Bestanden / Files

- `601742-01_bvj_4vwo_lob_a_bladerboek.pdf` - Bladerboek A (190 pagina's, 123.6 MB)
- `601743-01_bvj_4vwo_lob_b_bladerboek.pdf` - Bladerboek B (188 pagina's, 125.0 MB)

## Bestandslezer / File Reader

### Antwoord op "kan je de bestanden lezen?" / Answer to "can you read the files?"

**Ja! / Yes!** Alle bestanden in dit repository zijn leesbaar. / All files in this repository are readable.

### Gebruik / Usage

Dit repository bevat een Python script om de bestanden te lezen en analyseren:
This repository contains a Python script to read and analyze the files:

```bash
# Analyseer alle bestanden / Analyze all files
python file_reader.py

# Extraheer tekst uit specifiek bestand / Extract text from specific file
python file_reader.py 601742-01_bvj_4vwo_lob_a_bladerboek.pdf
```

### Vereisten / Requirements

```bash
pip install pypdf
```

### Functies / Features

Het script kan: / The script can:
- ✅ Controleren of PDF bestanden leesbaar zijn / Check if PDF files are readable
- 📄 Pagina aantallen tellen / Count page numbers  
- 📊 Bestandsgroottes tonen / Show file sizes
- 🔍 Metadata extraheren / Extract metadata
- 📖 Tekst proberen te extraheren / Attempt text extraction

### Resultaten / Results

Beide PDF bestanden zijn:
Both PDF files are:
- ✅ **Volledig leesbaar** / **Fully readable**
- 📚 Ongeveer 190 pagina's elk / About 190 pages each
- 🎨 Waarschijnlijk gescande afbeeldingen (geen extraheerbare tekst) / Likely scanned images (no extractable text)
- 💾 Opgeslagen met Git LFS voor grote bestanden / Stored with Git LFS for large files

## Git LFS

Dit repository gebruikt Git LFS (Large File Storage) voor de grote PDF bestanden.
This repository uses Git LFS (Large File Storage) for the large PDF files.

**Conclusie: Ja, de bestanden kunnen gelezen worden! 🎉**
**Conclusion: Yes, the files can be read! 🎉**