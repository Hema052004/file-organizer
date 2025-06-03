# File Organizer

This is a simple Python script ('organize.py') that takes all files in a given folder
and sorts them into subfolders based on their file extension.
For example, 'report.pdf' goes into a 'PDF/' subfolder, 'image.jpg' goes into 'JPG/', 
and files without an extension go into 'NoExtension/'.

---

## How to Use

1. Clone this repository or download the 'organize.py' script.
2. Ensure you have Python 3.x installed.
3. Open a terminal/command prompt and navigate into the project folder.
4. Run:

  python organize.py
   

5. When prompted, enter the full path of the folder you’d like to organize.
   Example:
  
   C:\Users\YourName\Downloads
   

6. The script will create subfolders (if needed) and move each file accordingly.

---

## Example

Before running 'organize.py' on 'C:\Users\YourName\Downloads':


Downloads/
├─ report.pdf
├─ photo.jpg
├─ notes.txt
├─ README
└─ archive/           ← (already a folder, untouched)


After running 'python organize.py' and entering 'C:\Users\YourName\Download'`:


Downloads/
├─ PDF/
│   └─ report.pdf
├─ JPG/
│   └─ photo.jpg
├─ TXT/
│   └─ notes.txt
├─ NoExtension/
│   └─ README
└─ archive/           ← (untouched existing folder)


---

## Dependencies

 Uses only Python’s built-in modules: 'os' and 'shutil'

---

## Future Enhancements

- Handle duplicate filenames by appending a counter or timestamp.
- Recursively organize files in subfolders using 'os.walk()'.
- Provide a GUI front-end (Tkinter or PyQt5).
- Map multiple extensions to a single folder (e.g., '.jpg', '.png' → 'Images/')
