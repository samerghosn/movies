import os
import codecs
import re
import common


def rewrite_file(text_file, file_content):
    """
  empty file and fill concat data inside it
  :param text_file: the text file object
  :param file_content: content of the file
  """
    try:
        text_file.seek(0)
        text_file.truncate()
        text_file.write(file_content)
        text_file.close()
    except Exception:
        print ("Error writing to file")

def restructure_file(file_name):
    """
    read the file and put all the text on 1 single line
    remove the numbers and new lines
    """
    text_file = codecs.open(file_name, "r+", encoding="UTF-8")
    try:
        the_file = text_file.read()
    except Exception:
        text_file = open(file_name, "r+")
        the_file = text_file.read()

    # remove the italic outlines and other values can be added here
    for extra_char in ['<i>', '</i>']:
        the_file = the_file.replace(extra_char, '')

    # Cleaning text and lower casing all words
    for char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '-', '>', '.', '\"', '?', ',', '(', ')',
                 '!', '<', ']', '[', '#']:
        the_file = the_file.replace(char, ' ')

    the_file = the_file.lower()
    the_file = the_file.replace('\n', ' ').replace('\r', '')
    the_file = re.sub(' +', ' ', the_file)

    # append the category from parent folder
    cat_entry = file_name.split('\\')[-2]
    the_file += "|" + cat_entry

    # empty the file and rewrite the cleaned text
    rewrite_file(text_file, the_file)


def scan_dir(dir_name):
    """
    scan the directory and work on each file
    """
    for root, dirs, files in os.walk(dir_name):
        for file_name in files:
            print("Scanning file {}".format(file_name))
            restructure_file(os.path.join(root, file_name))


if __name__ == "__main__":
    # process_dir(parent_folder)
    project_root = os.path.dirname(__file__)
    directory = project_root + "\\" + common.parent_folder

    scan_dir(directory)
