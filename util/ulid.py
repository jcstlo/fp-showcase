from ulid import ULID


def create_ulid_filename(instance, filename):
    """
    random ULID filename to be used in django.db.models.ImageField.upload_to
    file will be uploaded to MEDIA_ROOT/<ULID>.<filename_ext>
    """
    filename_ext = filename.split(".")[-1]
    ulid = str(ULID())
    ulid_filename = f"{ulid}.{filename_ext}"
    print(f"ulid_filename = {ulid_filename}")
    return ulid_filename
