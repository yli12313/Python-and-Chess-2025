import chess.engine
import chess.pgn
import IPython
from settings import NAG_SYMBOLS
import time

def game_play(game_path, annotations):

    with open(game_path) as pgn:
        game = chess.pgn.read_game(pgn)
        board = game.board()

        white_move_count = 0
        black_move_count = 0

        engine = chess.engine.SimpleEngine.popen_uci("./stockfish-macos-m1-apple-silicon")

        for move in game.mainline_moves():
            if board.turn == chess.WHITE:
                white_move_count += 1
            else:
                black_move_count += 1

            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
                    
            combined_display = f"""
                <div><h1>{game.headers['White']} vs. {game.headers['Black']}; Result: {game.headers['Result']}</h1></div>
                <div>Move: {white_move_count}</div>
                <div>{board._repr_svg_()}</div>
                <div>Move: {move}, Score: {info['score']}</div>
            """

            IPython.display.display(IPython.display.HTML(combined_display))

            IPython.display.clear_output(wait=True)
            time.sleep(4)

        IPython.display.display(IPython.display.HTML(combined_display))
        print(game.headers["Termination"])
        engine.quit()