from main import _download_webpage_impl

def run_verification():
    url = "https://datatalks.club/"
    print(f"Downloading content from {url}...")
    try:
        content = _download_webpage_impl(url)
        print("Content downloaded successfully.")
        
        # Count "data" (case-insensitive usually good, but user said "data" specifically)
        # Let's count both "data" (exact) and case-insensitive just to be helpful.
        count_exact = content.count("data")
        count_case_insensitive = content.lower().count("data")
        
        print(f"Occurrences of 'data' (exact): {count_exact}")
        print(f"Occurrences of 'data' (case-insensitive): {count_case_insensitive}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_verification()
