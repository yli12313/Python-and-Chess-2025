# Python-and-Chess-2025
This is a repository that will hold my project submission to PyCon 2025 in Pittsburgh, PA.

This is a program that will take .pgn files of your chess games and re-play them at scale. The original thought was to build an automated python script used to analyze Bobby Fisher's chess games at scale, where he played the Sicilian. I incorporated Stockfish annotations too, but they were not interpretable so it was removed. An abstract was submitted to PyCon 2025 with respect to this project. If it gets accepted, then I will keep working on this project. Until then, this project will be considered DONE. 

To run the notebook (`dev_notebook.ipynb`), make sure you have the following packages in a python or conda virtual environment:

- `python-chess`
- `IPython`
- `time`

Make sure to delete the games in `chess_games\losses` and put the games you want to analyze in this folder.
