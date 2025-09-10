#!/usr/bin/env python3
"""
File Reader for School Repository
Bestandslezer voor School Repository

Dit script kan de bestanden in deze repository lezen en analyseren.
This script can read and analyze the files in this repository.
"""

import os
import sys
from pathlib import Path
from pypdf import PdfReader

def analyze_pdf(file_path):
    """Analyseer een PDF bestand / Analyze a PDF file"""
    try:
        reader = PdfReader(file_path)
        
        # Basis informatie / Basic information
        num_pages = len(reader.pages)
        
        # Metadata
        metadata = reader.metadata
        title = metadata.get('/Title', 'Geen titel / No title') if metadata else 'Geen metadata / No metadata'
        author = metadata.get('/Author', 'Onbekend / Unknown') if metadata else 'Onbekend / Unknown'
        
        # Eerste paar regels tekst van eerste pagina / First few lines of text from first page
        first_page_text = ""
        if num_pages > 0:
            try:
                first_page = reader.pages[0]
                text = first_page.extract_text()
                # Neem eerste 200 karakters / Take first 200 characters
                first_page_text = text[:200].strip() if text else "Geen tekst gevonden / No text found"
            except Exception as e:
                first_page_text = f"Fout bij tekst extractie / Error extracting text: {str(e)}"
        
        return {
            'readable': True,
            'pages': num_pages,
            'title': title,
            'author': author,
            'preview': first_page_text,
            'size_mb': round(os.path.getsize(file_path) / (1024 * 1024), 1)
        }
        
    except Exception as e:
        return {
            'readable': False,
            'error': str(e),
            'size_mb': round(os.path.getsize(file_path) / (1024 * 1024), 1)
        }

def list_and_analyze_files():
    """Lijst en analyseer alle bestanden / List and analyze all files"""
    current_dir = Path('.')
    
    print("=== School Repository Bestandsanalyse / File Analysis ===")
    print()
    
    # Zoek naar PDF bestanden / Look for PDF files
    pdf_files = list(current_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("Geen PDF bestanden gevonden / No PDF files found")
        return
    
    print(f"Gevonden {len(pdf_files)} PDF bestand(en) / Found {len(pdf_files)} PDF file(s):")
    print()
    
    for pdf_file in pdf_files:
        print(f"📚 Bestand / File: {pdf_file.name}")
        analysis = analyze_pdf(pdf_file)
        
        if analysis['readable']:
            print(f"   ✅ Leesbaar / Readable: Ja / Yes")
            print(f"   📄 Pagina's / Pages: {analysis['pages']}")
            print(f"   📊 Grootte / Size: {analysis['size_mb']} MB")
            print(f"   📝 Titel / Title: {analysis['title']}")
            print(f"   👤 Auteur / Author: {analysis['author']}")
            print(f"   🔍 Voorvertoning / Preview:")
            print(f"      {analysis['preview']}")
        else:
            print(f"   ❌ Leesbaar / Readable: Nee / No")
            print(f"   📊 Grootte / Size: {analysis['size_mb']} MB")
            print(f"   ⚠️  Fout / Error: {analysis['error']}")
        
        print("-" * 60)
    
    # Algemene samenvatting / General summary
    readable_count = sum(1 for pdf in pdf_files if analyze_pdf(pdf)['readable'])
    total_size = sum(os.path.getsize(pdf) for pdf in pdf_files) / (1024 * 1024)
    
    print()
    print("=== Samenvatting / Summary ===")
    print(f"Totaal bestanden / Total files: {len(pdf_files)}")
    print(f"Leesbare bestanden / Readable files: {readable_count}")
    print(f"Totale grootte / Total size: {total_size:.1f} MB")
    
    if readable_count == len(pdf_files):
        print("✅ Alle bestanden zijn leesbaar! / All files are readable!")
    elif readable_count > 0:
        print("⚠️  Sommige bestanden zijn leesbaar / Some files are readable")
    else:
        print("❌ Geen bestanden zijn leesbaar / No files are readable")

def extract_text_from_file(filename, max_pages=5):
    """Extraheer tekst uit specifiek bestand / Extract text from specific file"""
    file_path = Path(filename)
    
    if not file_path.exists():
        print(f"❌ Bestand niet gevonden / File not found: {filename}")
        return
    
    if not file_path.suffix.lower() == '.pdf':
        print(f"❌ Alleen PDF bestanden ondersteund / Only PDF files supported: {filename}")
        return
    
    print(f"📖 Tekst extractie uit / Text extraction from: {filename}")
    print("=" * 60)
    
    try:
        reader = PdfReader(file_path)
        num_pages = min(len(reader.pages), max_pages)
        
        for i in range(num_pages):
            print(f"\n--- Pagina / Page {i + 1} ---")
            try:
                page = reader.pages[i]
                text = page.extract_text()
                if text.strip():
                    print(text[:1000])  # Eerste 1000 karakters / First 1000 characters
                    if len(text) > 1000:
                        print("\n... (meer tekst beschikbaar / more text available) ...")
                else:
                    print("Geen tekst gevonden op deze pagina / No text found on this page")
            except Exception as e:
                print(f"Fout bij lezen pagina / Error reading page: {str(e)}")
        
        if len(reader.pages) > max_pages:
            print(f"\n📝 Nota / Note: Alleen eerste {max_pages} pagina's getoond van {len(reader.pages)} totaal")
            print(f"Only first {max_pages} pages shown of {len(reader.pages)} total")
            
    except Exception as e:
        print(f"❌ Fout bij lezen bestand / Error reading file: {str(e)}")

def main():
    """Hoofdfunctie / Main function"""
    if len(sys.argv) == 1:
        # Geen argumenten - analyseer alle bestanden / No arguments - analyze all files
        list_and_analyze_files()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ['--help', '-h', 'help']:
            print("File Reader for School Repository / Bestandslezer voor School Repository")
            print()
            print("Gebruik / Usage:")
            print("  python file_reader.py                    # Analyseer alle bestanden / Analyze all files")
            print("  python file_reader.py <bestandsnaam>     # Extraheer tekst / Extract text")
            print("  python file_reader.py --help             # Toon deze help / Show this help")
            print()
            print("Voorbeelden / Examples:")
            print("  python file_reader.py")
            print("  python file_reader.py 601742-01_bvj_4vwo_lob_a_bladerboek.pdf")
        else:
            # Een argument - extraheer tekst uit specifiek bestand / One argument - extract text from specific file
            extract_text_from_file(arg)
    else:
        print("Gebruik / Usage:")
        print("  python file_reader.py                    # Analyseer alle bestanden / Analyze all files")
        print("  python file_reader.py <bestandsnaam>     # Extraheer tekst / Extract text")
        print("  python file_reader.py --help             # Toon deze help / Show this help")
        print()
        print("Voorbeelden / Examples:")
        print("  python file_reader.py")
        print("  python file_reader.py 601742-01_bvj_4vwo_lob_a_bladerboek.pdf")

if __name__ == "__main__":
    main()