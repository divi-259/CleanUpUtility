# CleanUpUtility
A Utility which can run in the background and clean up redundant files and empty folders.

# How to use?
1. Copy main.py in your local system.
2. Run this file in using command "python main.py" in command prompt.
3. Give the full path to folder where you want to delete redundant image files and empty folders.
4. Or if you will press enter, it will automatically take the current folder as default
5. All Image files and empty folders will be deleted.

Note: If you are a little cautious about directly using this deletion script, then you can first comment the os.remove()  or shutil.rmtree() lines and then run the script to check the files that are going to get deleted. After that you can actually run the original script to delete those files.
