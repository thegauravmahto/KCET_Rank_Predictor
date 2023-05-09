from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def calculate_final_marks(board_score, kcet_marks):
    max_board_score = 300
    max_kcet_marks = 180
    ipe_percentage = 0.50
    kcet_percentage = 0.50

    normalized_board_score = (board_score / max_board_score) * 100
    normalized_kcet_marks = (kcet_marks/ max_kcet_marks) * 100
    
    final_marks = (normalized_board_score * ipe_percentage) + (normalized_kcet_marks * kcet_percentage)
    return round(final_marks)

def read_csv_and_find_rank(filename, final_marks):
    df = pd.read_csv(filename)
    matching_row = df[df['TMarks'] == final_marks]
    return matching_row.iloc[0]['TRank']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        board_score = float(request.form['board_score'])
        kcet_marks = float(request.form['kcet_marks'])

        final_marks = calculate_final_marks(board_score, kcet_marks
    )
        filename = 'data.csv'
        rank = read_csv_and_find_rank(filename, final_marks)

        return render_template('results.html', final_marks=final_marks, rank=rank)

    return render_template('index.html',port=5000)

if __name__ == '__main__':
    app.run(debug=True)
