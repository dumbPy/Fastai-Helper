# Using Custom Dataset
import torch


class CustomDataset(torch.utils.data.Dataset):
    """Custom Dataset Class
    """

    def __init__(self, data):
        self.path = path
        # stores tuple of (path_to-file, label)
        self.dat = data

    def __getitem__(i):
        return self.data[i]

    @classmethod
    def foldermethod(path, is_multi=True, extension='.jpg', idlabelformat=False, idlabelparsefunc=None):
        """Pass path to folder containing train, val(optional), test(optional) folders.
        train/val/test folders contain label folders.
        If name is of format idlabel.jpg, then pass function to parse id and label.
        """
        from pathlib import Path
        data = []
        if Path(path).exists():
            if is_multi:
                labels = [l for l in Path(path).iterdir() if l.is_dir()]
                for label in labels:
                    data.append(*[(img, label.name) for img in label.iterdir() if img.is_dir() == Flase])
            else:
                if idlabelformat:
                    if not idlabelparsefunc:
                        raise NameParserNotGivenError
                    else:
                        for image in path.iterdir():
                            id, label = idlabelparsefunc(image.name)
                            data.append((image, label))