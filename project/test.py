from main import download_webpage

# Test the download_webpage function
if __name__ == "__main__":
    # Test with a simple URL
    test_url = "https://github.com/alexeygrigorev/minsearch"
    print(f"Testing download_webpage with: {test_url}")
    print("-" * 50)
    
    try:
        content = download_webpage(test_url)
        print("Success! Downloaded content:")
        print("-" * 50)
        print(content[:500])  # Print first 500 characters
        print("-" * 50)
        print(f"Total length: {len(content)} characters")
    except Exception as e:
        print(f"Error: {e}")
