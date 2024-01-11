import os
import shutil
from sklearn.model_selection import train_test_split

def split_data(source_folder, destination_folder):
    # make test,train validation directories
    train_folder = os.path.join(destination_folder, 'train')
    test_folder = os.path.join(destination_folder, 'test')
    validation_folder = os.path.join(destination_folder, 'valid')
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)



    def move_files(files, source, destination):
        os.makedirs(destination, exist_ok=True)
       
 
        images_subfolder = os.path.join(destination, 'images')
        os.makedirs(images_subfolder, exist_ok=True)

        for file in files:
            shutil.move(os.path.join(source, file), os.path.join(images_subfolder, file))

    # Get the list of image files in the images folder
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg') or f.endswith('.png')]

    # Split the files into train, test, and validation sets
    train_files, test_validation_files = train_test_split(image_files, test_size=0.2, random_state=42)
    test_files, validation_files = train_test_split(test_validation_files, test_size=0.5, random_state=42)

    # Move image files to the 'images' subdirectory in their respective folders
    move_files(train_files, source_folder, train_folder)
    move_files(test_files, source_folder, test_folder)
    move_files(validation_files, source_folder, validation_folder)

    # Move corresponding text files to the 'labels' subdirectory
    for folder in [train_folder, test_folder, validation_folder]:
        images_subfolder = os.path.join(folder, 'images')
        labels_subfolder = os.path.join(folder, 'labels')
        os.makedirs(labels_subfolder, exist_ok=True)

        for image_file in os.listdir(images_subfolder):
            base_name, ext = os.path.splitext(image_file)
            text_file = base_name + '.txt'
            text_file_path = os.path.join(source_folder, text_file)

            if os.path.exists(text_file_path):
                shutil.move(text_file_path, labels_subfolder)

if __name__ == "__main__":

    Sample_Images= os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'Data', 'images')
    Splited_Data = os.path.join(Sample_Images, '..')
    
    split_data(Sample_Images, Splited_Data)
