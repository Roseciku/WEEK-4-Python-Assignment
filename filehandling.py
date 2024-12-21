def read_and_modify_file(input_file, output_file):
    try:
        
        with open(input_file, 'r') as infile:
            content = infile.read()
            print(content)

       
        modified_content = content.replace("old_word", "new_word")

       
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print("File has been modified and saved successfully")
    
    except FileNotFoundError:
        print(f"The file {input_file} was not found. Please check the filename.")
    except OSError:
        print(f"An OS error occurred while handling the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_modify_file('input.txt', 'output.txt')


#Error Handling

def add_file_to_read():
    file_name=input('Enter the file you want to read:')

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
            print("File was not found.Please check the filename.")

    except OSError:
            print("An OS error occurred. Please try again.")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")


add_file_to_read()