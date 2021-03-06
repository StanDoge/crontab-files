import os
import re
import datetime

WORKSPACE = "/home/standoge/Descargas"
FILES = f"{WORKSPACE}/miscellaneous"
DOCS = f"{WORKSPACE}/docs"
IMGS = f"{WORKSPACE}/images"
LOGS_PATH = f"{WORKSPACE}/logs"
SNAPSHOTS = f"{WORKSPACE}/logs/snapshots"
DOC_PATTERN = re.compile(r"[a-z\ ]*(\.pdf|\.txt|\.docx)")
IMG_PATTERN = re.compile(r"[a-z\ ]*(\.jpg|\.png|\.jpeg|\.mp4)")


def directories() -> None:
    """Creates directories to move all files that will be filtered in workspace
    path.
    """

    os.mkdir(LOGS_PATH) if not os.path.exists(LOGS_PATH) else print(
        "Logs directory already exist"
    )
    os.mkdir(SNAPSHOTS) if not os.path.exists(SNAPSHOTS) else print(
        "Snapshot already exist"
    )
    os.mkdir(FILES) if not os.path.exists(FILES) else print(
        "Miscellaneous already exist"
    )
    os.mkdir(DOCS) if not os.path.exists(PDF) else print("Pdfs already exist")
    os.mkdir(IMGS) if not os.path.exists(IMGS) else print("Images already exist")


def filter() -> None:
    """Filter between files and directories using const WORKSPACE value as path
    also this const is used as relative path to make others paths to logs
    and snapshots.
    """

    with os.scandir(WORKSPACE) as sentinel:
        for e in sentinel:
            router(e) if e.is_file() else print(f"dir -> {e.name}")


def log() -> str:
    """Return logs_file_path
    Use it as destiny for each moves operation file creating a directory for logs
    files and also creating these files, each one has the date when was created.
    """

    logs_file_path: str = f"{LOGS_PATH}/log-{datetime.date.today()}"
    os.system(
        f"cd {LOGS_PATH} && touch log-{datetime.date.today()}"
    ) if not os.path.exists(logs_file_path) else print("File for logs already exist")
    return logs_file_path


def rename_log(file_source:str, file_name:str, logs:str, file_destiny:str) -> None:
    """
    Using os.rename to move files renaming them and then make a log to have a register
    for the files moved and where was moved also adding date and hours when this was.

    Parameters:
        file_source(str) : file's origin path.
        file_name(str)   : file's name.
        logs(str)        : log's file name.
        file_destiny(str): path where the file would be moved.
    """

    os.rename(file_source, file_destiny + "/" + file_name)
    os.system(
        f"echo {file_source} moved to {file_destiny} >> {logs} {datetime.datetime.now()}"
    )


def router(file:object) -> None:
    """
    Filter where goes each file using RegExp patterns to know their extension.

    Parameters:
        file(object): Output from <scandir> function.
    """

    directories()
    log_path: str = log()

    if re.search(DOC_PATTERN, file.name):
        rename_log(file.path, file.name, log_path, DOCS)

    elif re.search(IMG_PATTERN, file.name):
        rename_log(file.path, file.name, log_path, IMGS)

    else:
        rename_log(file.path, file.name, log_path, FILES)


def snapshot() -> None:
    """List directories in workspace after the files was moved regarding they extension.
    Then, we can see the state of workspace after to be filtered and cleanned.
    """

    snapshot_dir: str = os.listdir(f"{WORKSPACE}")
    os.system(
        f'''echo {snapshot_dir} {datetime.datetime.now()} 
        >> {SNAPSHOTS}/snapshot-{datetime.date.today()}'''
    )
