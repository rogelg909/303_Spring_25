import wikipedia
import time 
import os


## Sequentially download wikipedia content
start_time = time.perf_counter()

# Step 1
search_term = "generative artificial intelligence"
topics = wikipedia.search(search_term)

os.makedirs("wikipedia_references", exist_ok=True)

# Step 2
for topic in topics:
    try:
        # Step 2i
        page = wikipedia.page(topic, auto_suggest=False)
        
        #Step 2ii
        page_title = page.title
        
        # Step 2iii
        page_references = page.references
        
        references_text = '\n'.join(page_references)
        
        safe_title = ''.join(c for c in page_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        file_path = os.path.join("wikipedia_references", f"{safe_title}.txt")
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(references_text)
        
        print(f"Saved references for: {page_title}")
    
    except Exception as e:
        print(f"Skipping topic '{topic}' due to error: {e}")

# Step 3
end_time = time.perf_counter()
print(f"\nExecution completed in {end_time - start_time:.2f} seconds.")

## Concurrently download wikipedia content

import wikipedia
import time
import os
from concurrent.futures import ThreadPoolExecutor

os.makedirs("wikipedia_references", exist_ok=True)

# Step 2
def wiki_dl_and_save(topic):
    try:
        # Step 2i
        page = wikipedia.page(topic, auto_suggest=False)
        
        # Step 2ii
        title = page.title

        # Step 2iii
        references = page.references
        
        references_text = '\n'.join(references)
        # Step 2 iv
        safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        file_path = os.path.join("wikipedia_references", f"{safe_title}.txt")
        

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(references_text)

        print(f"Saved references for: {title}")
    
    except Exception as e:
        print(f"Failed to process topic '{topic}': {e}")

# Step 3 
if __name__ == "__main__":
    start_time = time.perf_counter()
    
    topics = wikipedia.search("generative artificial intelligence")

    with ThreadPoolExecutor() as executor:
        executor.map(wiki_dl_and_save, topics)
    # Step 4
    end_time = time.perf_counter()
    print(f"\nExecution completed in {end_time - start_time:.2f} seconds.")