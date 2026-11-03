import io
import tarfile

def make_archive(folder):
    buffer=io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
        tar.add(folder)
    return buffer.getvalue()

def extract_archive(data, dest):
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        tar.extractall(dest, filter="data")
