from folderGPT.Database.file_database import FileDatabase
from folderGPT.Model.model import LLModel
from folderGPT.utils import ProjectLogger

if __name__ == "__main__":
    ProjectLogger().info("Starting program")
    model = LLModel(model_name= "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

    generated_text = model.generate("hello world, what colot is my cat?")
    print(generated_text)
    ProjectLogger().info("Closing program")

    # fileDB = FileDatabase()
    # fileDB.add_folder("./files")
    # fileDB.update()
