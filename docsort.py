import os
import subprocess
import threading
import sys
import time
import pyautogui




def get_creation_date(file_path):
    # Get the creation timestamp of the file
    creation_timestamp = os.path.getctime(file_path)
    # Convert the timestamp to a readable format (date only)
    creation_date = time.strftime('%d-%m-%Y', time.localtime(creation_timestamp))
    return creation_date

def run_subprocess(file_path):
    process = subprocess.Popen(file_path, shell=True)
    process.wait()

def check_input(file_path, dirname):

    old_file_path = file_path
    creation_date = get_creation_date(file_path)

    print("\nEnter - next (no changes)")
    print("1 - Offer Letter")
    print("2 - Permanent Employment Contract")
    print("3 - Fixed-term Employment Contract")
    print("4 - NOC Employment Contract")
    print("5 - WTD Side Letter")
    print("6 - FTC Extension")
    print("7 - FTC Bonus Confirmation")
    print("8 - Retention Bonus")
    print("9 - Employment Contract Addendum")
    print("10 - Probation Completion Letter")
    print("11 - Confirmation of Resignation")
    print("12 - Maternity Letter")
    print("13 - Flexible Working Request")
    print("14 - HR Starter Forms")
    print("15 - Secondment Conversion")


    
    choice = input("\nPick: ")
    if choice == "1":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Offer Letter - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "2":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Permanent Employment Contract - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "3":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Fixed-term Employment Contract - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "4":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - NOC Employment Contract - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "5":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - WTD Side Letter - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "6":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - FTC Extension - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "7":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - FTC Bonus Confirmation - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "8":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Retention Bonus - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "9":
        file_name, file_extension = os.path.splitext(file_path)
        reason = input("\nType reason: ")
        new_file_name = f"{os.path.basename(dirname)} - Employment Contract Addendum - " + reason + " - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "10":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Probation Completion Letter - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "11":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Confirmation of Resignation - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "12":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Maternity Letter - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "13":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Flexible Working Request - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nOld: {file_path}\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "14":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - HR Starter Forms - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nNew: {new_file_path}")
        time.sleep(2)
        return True
    elif choice == "15":
        file_name, file_extension = os.path.splitext(file_path)
        new_file_name = f"{os.path.basename(dirname)} - Secondment Conversion - " + creation_date + file_extension
        new_file_path = os.path.join(dirname, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed file:\nNew: {new_file_path}")
        time.sleep(2)
        return True
    else:
        return True



def iterate_directory(root_path):
    # Iterate over the directory recursively
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_name = os.path.basename(file_path)
            dirname = dirpath
            print("Opening file:", file_name)
            stop_event = threading.Event()
            t = threading.Thread(target=run_subprocess, args=(file_path,))
            t.start()
            time.sleep(2)
            pyautogui.hotkey('alt', 'tab')
            check_input(file_path, dirname)
            
            
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            print("Entering directory:", subdir_path)
            # Recursively iterate through subdirectories
            iterate_directory(subdir_path)


if __name__ == "__main__":

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
    
    # Get the current directory
    root_path = os.getcwd() + '\\data'

    # Start iterating over the directory
    iterate_directory(root_path)
