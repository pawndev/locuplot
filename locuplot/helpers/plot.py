import os

def save_plot(figure, path: str, filename: str, format: str):
    figure.savefig(os.path.join(path, filename), format=format)