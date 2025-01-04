import chess.svg
import IPython
from settings import NAG_SYMBOLS
import time

def game_play(game_path, annotations):
    with open(game_path) as pgn:
        game = chess.pgn.read_game(pgn)
        board = game.board()

        node = game
        white_move_count = 0
        black_move_count = 0

        for move in game.mainline_moves():
            node = node.variation(0)

            if board.turn == chess.WHITE:
                white_move_count += 1
            else:
                black_move_count += 1
                
                if black_move_count in annotations:
                    node.nags.add(annotations[black_move_count])

            board.push(move)

            combined_display = f"""
                <div><h1>{game.headers['White']} vs. {game.headers['Black']}; Result: {game.headers['Result']}</h1></div>
                <div>Move: {white_move_count}</div>
                <div>{board._repr_svg_()}</div>
            """
            IPython.display.display(IPython.display.HTML(combined_display))

            if node.nags:
                nag_symbols = [NAG_SYMBOLS.get(nag, f"${nag}") for nag in node.nags]
                print(f"{move}: {' '.join(nag_symbols)}")

            IPython.display.clear_output(wait=True)
            time.sleep(1.85)

        IPython.display.display(IPython.display.HTML(combined_display))
        print(game.headers["Termination"])