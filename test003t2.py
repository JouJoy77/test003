"""
Дано: два FTP ресурса
Требуется: Написать функцию на языке Python, которая копирует файлы с одного FTP-сервера, на другой.
"""

from ftplib import FTP


def copy_files_ftp(source_host, source_path, source_username, source_password,
                   destination_host, destination_path, destination_username, destination_password):
    """
    Copy files by FTP.

    Parameters
    ----------
    source_host
        Source address (from where to copy)
    source_path
        Path to the directory
    source_username
        Login username (source)
    source_password
        Login password (source)
    destination_host
        Destination address (where to copy)
    destination_path
        Path to the directory
    destination_username
        Login username (destination)
    destination_password
        Login password (destination)
    """
    try:
        source = FTP(source_host)
        source.login(user=source_username, passwd=source_password)

        destination = FTP(destination_host)
        destination.login(user=destination_username,
                          passwd=destination_password)

        source.cwd(source_path)
        destination.cwd(destination_path)

        file_list = source.nlst()
        for file_name in file_list:
            with open(file_name, "wb") as local_file:
                source.retrbinary("RETR " + file_name, local_file.write)

            with open(file_name, "rb") as local_file:
                destination.storbinary("STOR " + file_name, local_file)

            print(f"File has been copied: {file_name}")

        source.quit()
        destination.quit()

    except Exception as e:
        print(f"Error: {e}")
