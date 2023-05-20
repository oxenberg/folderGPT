from fastapi import FastAPI

from folderGPT.Database.file_database import FileDatabase
from folderGPT.Model.model import LLModel

app = FastAPI()
# model = LLModel(model_name="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")  # create the model
# fileDB = FileDatabase().add_folder("./files").update()  # update the database with the files in the folder


@app.get("/")
def read_root():
    return {"Hello": "World"}

#
# @app.get("/generate/{text}")
# def generate(text: str):
#     generated_text = model.generate(text)
#     return {"generated_text": generated_text}
#
#
# @app.get("/update/{path}")
# def update(path: str):
#     try:
#         fileDB.add_folder(path).update()
#     except Exception as e:
#         return {"status": "failed", "error": str(e)}
#     return {"status": "updated"}
