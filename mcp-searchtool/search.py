import zipfile
import os
from minsearch import Index

def load_documents(zip_path):
    documents = []
    with zipfile.ZipFile(zip_path, 'r') as z:
        for filename in z.namelist():
            if filename.endswith('.md') or filename.endswith('.mdx'):
                # Remove first directory component
                # e.g. "fastmcp-main/docs/welcome.mdx" -> "docs/welcome.mdx"
                parts = filename.split('/', 1)
                if len(parts) > 1:
                    clean_filename = parts[1]
                else:
                    clean_filename = filename

                # Skip if it was a root file (empty clean filename if it was just a dir name, though filtering by extension handles files)
                if not clean_filename: 
                    continue
                
                content = z.read(filename).decode('utf-8')
                documents.append({
                    'content': content,
                    'filename': clean_filename
                })
    return documents

def build_index(documents):
    index = Index(
        text_fields=["content"],
        keyword_fields=["filename"]
    )
    index.fit(documents)
    return index

def search(query, index, num_results=5):
    results = index.search(
        query,
        boost_dict={'content': 1},
        num_results=num_results
    )
    return results

def main():
    zip_path = "../fastmcp-main.zip"
    if not os.path.exists(zip_path):
        print(f"Error: {zip_path} not found.")
        return

    print("Loading documents...")
    documents = load_documents(zip_path)
    print(f"Loaded {len(documents)} documents.")

    print("Building index...")
    index = build_index(documents)
    
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "how to create a resource"
    print(f"\nSearching for: '{query}'")
    results = search(query, index)
    
    for i, result in enumerate(results):
        print(f"\nResult {i+1}:")
        print(f"Filename: {result['filename']}")
        # Print a snippet of content
        print(f"Content: {result['content'][:200]}...")

if __name__ == "__main__":
    main()
