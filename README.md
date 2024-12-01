## **Get-the-cap**

**A Python script to download and clean YouTube video captions.**

### **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/youtube-caption-downloader.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install youtube_transcript_api
   ```

### **Usage**

1. **Run the Script:**
   Execute the Python script from your terminal:
   ```bash
   python youtube_caption_downloader.py
   ```
2. **Follow the Prompts:**
   - Enter the YouTube video URL.
   - Choose the desired language for the captions (`es` for Spanish, `en` for English).
   - Specify the desired filename for the output file.

### **How It Works**

1. **Extracts Video ID:** Parses the YouTube URL to extract the video ID.
2. **Downloads Captions:** Fetches captions in the specified language using the `youtube_transcript_api` library.
3. **Cleans Captions:** Removes unnecessary characters and formatting.
4. **Saves Captions:** Writes the cleaned captions to a text file.

### **Customization**

- **Language Support:** Extend the script to support more languages by adding them to the `valid_langs` list.
- **Cleaning Function:** Customize the `clean_text` function to tailor the cleaning process to your specific needs.
- **Error Handling:** Implement error handling to gracefully handle exceptions, such as network errors or invalid URLs.


**Note:** 
Please use this script responsibly and respect YouTube's terms of service. Avoid excessive use or automated scraping, as it may violate their terms.
