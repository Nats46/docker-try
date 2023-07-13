from fastapi import APIRouter,File,UploadFile
import shutil
from fastapi.responses import FileResponse

router=APIRouter(prefix='/file',tags=['File'])


@router.post('/file',)
def get_file(file:bytes=File(...)):
    content = file.decode('utf-8')
    lines=content.split('\6')
    return {'lines':lines}

@router.post('/uploadfiles')
def get_upload_files(upload_files:UploadFile=File(...)):
    path = f"D:/intern/project/files/filestore/{upload_files.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_files.file,buffer)
    return{
        'filename':path,
        'type': upload_files.content_type
    }

@router.get('/download/{name}',response_class=FileResponse)
def download_file(name:str):
    path = f"D:/intern/project/files/filestore/{name}"
    return path